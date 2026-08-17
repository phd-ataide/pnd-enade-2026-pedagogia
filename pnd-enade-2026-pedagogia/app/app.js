/* =========================================================================
   PND/ENADE 2026 — Pedagogia UniFECAF — App de estudos (standalone)
   Toda a lógica do app: navegação, trilha, dicas, teoria, quiz e progresso.
   Dados (OFFICIAL, PRACTICE, TRILHA, TEORIA, DICAS, DISCURSIVA) são injetados
   antes deste script como constantes globais.
   ========================================================================= */

(function(){
"use strict";

var EXAM_DATE = new Date("2026-09-20T08:00:00");
var STORAGE_KEY = "pnd2026_pedagogia_unifecaf_v1";

/* ---------------------------------------------------------------------
   Progresso (localStorage)
--------------------------------------------------------------------- */
function loadProgress(){
  try{
    var raw = localStorage.getItem(STORAGE_KEY);
    if(!raw) return defaultProgress();
    var p = JSON.parse(raw);
    return Object.assign(defaultProgress(), p);
  }catch(e){
    console.warn("Não foi possível ler o progresso salvo, iniciando novo.", e);
    return defaultProgress();
  }
}
function defaultProgress(){
  return {
    trilhaChecklist: {},
    quizHistory: [],
    temaStats: {},
    createdAt: null
  };
}
var PROGRESS = loadProgress();
function saveProgress(){
  try{
    localStorage.setItem(STORAGE_KEY, JSON.stringify(PROGRESS));
  }catch(e){
    console.warn("Não foi possível salvar o progresso (localStorage indisponível).", e);
  }
}
function registrarTema(temaKey, correta){
  if(!PROGRESS.temaStats[temaKey]) PROGRESS.temaStats[temaKey] = {correct:0, total:0};
  PROGRESS.temaStats[temaKey].total += 1;
  if(correta) PROGRESS.temaStats[temaKey].correct += 1;
}
function registrarQuiz(entry){
  PROGRESS.quizHistory.push(entry);
  saveProgress();
}

/* ---------------------------------------------------------------------
   Util
--------------------------------------------------------------------- */
function el(tag, cls, html){
  var e = document.createElement(tag);
  if(cls) e.className = cls;
  if(html !== undefined) e.innerHTML = html;
  return e;
}
function fmtPct(c,t){ return t>0 ? Math.round((c/t)*100) : 0; }
function shuffle(arr){
  var a = arr.slice();
  for(var i=a.length-1;i>0;i--){
    var j = Math.floor(Math.random()*(i+1));
    var tmp=a[i]; a[i]=a[j]; a[j]=tmp;
  }
  return a;
}
function pickRandom(arr, n){
  return shuffle(arr).slice(0, Math.min(n, arr.length));
}
function corTema(pct){
  if(pct >= 70) return "var(--verde)";
  if(pct >= 45) return "var(--amarelo)";
  return "var(--vermelho)";
}
function escapeHtml(s){
  return String(s == null ? "" : s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}
function nl2br(s){
  return escapeHtml(s).replace(/\n/g,"<br>");
}

/* ---------------------------------------------------------------------
   Navegação entre views
--------------------------------------------------------------------- */
var VIEWS = ["inicio","trilha","dicas","teoria","simulado","praticar","banco","progresso"];
var currentView = "inicio";

function goTo(view, opts){
  currentView = view;
  VIEWS.forEach(function(v){
    document.getElementById("view-"+v).classList.toggle("hidden", v!==view);
  });
  var navBtns = document.querySelectorAll("#mainnav button");
  navBtns.forEach(function(b){
    b.classList.toggle("active", b.getAttribute("data-view")===view);
  });
  window.scrollTo({top:0, behavior:"instant"});
  if(view === "inicio") renderInicio();
  if(view === "trilha") renderTrilha();
  if(view === "dicas") renderDicas();
  if(view === "teoria") renderTeoria();
  if(view === "simulado" && !(opts && opts.keepState)) renderSimuladoSetup();
  if(view === "praticar" && !(opts && opts.keepState)) renderPraticarSetup();
  if(view === "banco") renderBanco();
  if(view === "progresso") renderProgresso();
}

/* ---------------------------------------------------------------------
   Countdown
--------------------------------------------------------------------- */
function diasRestantes(){
  var now = new Date();
  var diff = EXAM_DATE.getTime() - now.getTime();
  return diff;
}
function renderCountdownMini(){
  var diff = diasRestantes();
  var el2 = document.getElementById("countdown-mini");
  if(diff <= 0){ el2.innerHTML = "<b>É hoje!</b> Boa prova!"; return; }
  var dias = Math.floor(diff/(1000*60*60*24));
  el2.innerHTML = "<b>"+dias+"</b> dia(s) até o PND 2026";
}
setInterval(renderCountdownMini, 60000);

/* =========================================================================
   VIEW: INÍCIO (dashboard)
   ========================================================================= */
function renderInicio(){
  var root = document.getElementById("view-inicio");
  root.innerHTML = "";

  var diff = diasRestantes();
  var dias = Math.max(0, Math.floor(diff/(1000*60*60*24)));
  var horas = Math.max(0, Math.floor((diff%(1000*60*60*24))/(1000*60*60)));

  var hero = el("div","hero");
  hero.innerHTML =
    "<span class='badge' style='background:rgba(255,255,255,.18);padding:.2rem .6rem;border-radius:8px;font-size:.72rem;font-weight:700;letter-spacing:.04em'>PEDAGOGIA · UNIFECAF</span>"+
    "<h1 style='margin-top:.5rem'>Preparação PND / ENADE 2026</h1>"+
    "<p style='opacity:.92;max-width:640px'>Este aplicativo foi construído a partir da prova real do PND 2025 (Pedagogia), com banco próprio de questões comentadas, trilha de estudos, dicas de especialistas e simulados — tudo salvo apenas no seu navegador.</p>"+
    "<div class='count-grande'>"+
      "<div class='count-box'><span class='num'>"+dias+"</span><span class='lbl'>dias</span></div>"+
      "<div class='count-box'><span class='num'>"+horas+"</span><span class='lbl'>horas</span></div>"+
      "<div class='count-box'><span class='num'>80</span><span class='lbl'>questões oficiais</span></div>"+
      "<div class='count-box'><span class='num'>157</span><span class='lbl'>questões inéditas</span></div>"+
    "</div>"+
    "<div class='btn-row'>"+
      "<button class='btn' style='background:#fff;color:var(--azul)' onclick=\"App.goTo('trilha')\">Ver minha trilha de hoje</button>"+
      "<button class='btn' style='background:rgba(255,255,255,.2);color:#fff' onclick=\"App.goTo('simulado')\">Simulado oficial (80 questões)</button>"+
    "</div>";
  root.appendChild(hero);

  // stats gerais
  var totalResp = 0, totalCorretas = 0;
  Object.keys(PROGRESS.temaStats).forEach(function(k){
    totalResp += PROGRESS.temaStats[k].total;
    totalCorretas += PROGRESS.temaStats[k].correct;
  });
  var diasFeitos = Object.keys(PROGRESS.trilhaChecklist).filter(function(k){return PROGRESS.trilhaChecklist[k];}).length;

  var statsCard = el("div","card");
  statsCard.innerHTML = "<h2>Seu progresso</h2>";
  var statRow = el("div","stat-row");
  statRow.innerHTML =
    "<div class='stat'><div class='num'>"+diasFeitos+"/35</div><div class='lbl'>dias da trilha concluídos</div></div>"+
    "<div class='stat'><div class='num'>"+totalResp+"</div><div class='lbl'>questões respondidas</div></div>"+
    "<div class='stat'><div class='num'>"+fmtPct(totalCorretas,totalResp)+"%</div><div class='lbl'>acerto geral</div></div>"+
    "<div class='stat'><div class='num'>"+PROGRESS.quizHistory.length+"</div><div class='lbl'>simulados/quizzes feitos</div></div>";
  statsCard.appendChild(statRow);

  if(totalResp === 0){
    statsCard.appendChild(el("p", null, "<br>Você ainda não praticou nenhuma questão. Que tal começar com um <a href='#' onclick=\"App.goTo('praticar');return false;\">quiz temático rápido</a> ou seguir a <a href='#' onclick=\"App.goTo('trilha');return false;\">trilha de hoje</a>?"));
  } else {
    var fracos = temasMaisFracos(3);
    if(fracos.length){
      var box = el("div", null, "<br><b>Temas para reforçar agora:</b>");
      var ul = el("ul");
      fracos.forEach(function(f){
        ul.appendChild(el("li", null, f.tema + " — " + f.pct + "% de acerto ("+f.stats.correct+"/"+f.stats.total+")"));
      });
      box.appendChild(ul);
      statsCard.appendChild(box);
    }
  }
  root.appendChild(statsCard);

  var grid = el("div","grid2");

  var c1 = el("div","card");
  c1.innerHTML = "<h2>📅 Trilha de estudos</h2><p>Um plano dia a dia, de hoje até 20/09/2026, cobrindo Formação Geral e Componente Específico de Pedagogia.</p>";
  c1.appendChild(el("button","btn", "Ver trilha completa"));
  c1.querySelector("button").onclick = function(){ goTo("trilha"); };
  grid.appendChild(c1);

  var c2 = el("div","card");
  c2.innerHTML = "<h2>🎯 Praticar por tema</h2><p>157 questões inéditas em estilo PND/ENADE, organizadas em 14 temas de Pedagogia.</p>";
  c2.appendChild(el("button","btn verde","Praticar agora"));
  c2.querySelector("button").onclick = function(){ goTo("praticar"); };
  grid.appendChild(c2);

  var c3 = el("div","card");
  c3.innerHTML = "<h2>📝 Simulado oficial</h2><p>As 80 questões reais do PND 2025, com gabarito comentado — como um treino de prova completa.</p>";
  c3.appendChild(el("button","btn roxo","Fazer simulado"));
  c3.querySelector("button").onclick = function(){ goTo("simulado"); };
  grid.appendChild(c3);

  var c4 = el("div","card");
  c4.innerHTML = "<h2>💡 Dicas de prova</h2><p>Estratégias de cursinhos e especialistas: método dos 3 degraus, gestão do tempo e guia da discursiva.</p>";
  c4.appendChild(el("button","btn secundario","Ver dicas"));
  c4.querySelector("button").onclick = function(){ goTo("dicas"); };
  grid.appendChild(c4);

  root.appendChild(grid);
}

function temasMaisFracos(n){
  var arr = Object.keys(PROGRESS.temaStats).map(function(k){
    var s = PROGRESS.temaStats[k];
    return {tema:k, stats:s, pct: fmtPct(s.correct, s.total)};
  }).filter(function(x){ return x.stats.total >= 2; });
  arr.sort(function(a,b){ return a.pct - b.pct; });
  return arr.slice(0,n);
}

/* =========================================================================
   VIEW: TRILHA DE ESTUDOS
   ========================================================================= */
function renderTrilha(){
  var root = document.getElementById("view-trilha");
  root.innerHTML = "";
  root.appendChild(el("div","card","<h2>📅 Trilha de Estudos — "+TRILHA.length+" dias</h2><p>De "+fmtDataBr(TRILHA[0].data)+" até "+fmtDataBr(TRILHA[TRILHA.length-1].data)+" (dia da prova). Marque cada dia concluído para acompanhar seu avanço — tudo fica salvo neste navegador.</p>"));

  var todayIso = new Date().toISOString().slice(0,10);
  var semanaAtual = -1;

  TRILHA.forEach(function(dia){
    if(dia.semana !== semanaAtual){
      semanaAtual = dia.semana;
      var titulo = semanaAtual <= 5 ? ("Semana "+semanaAtual) : "Dia da prova";
      root.appendChild(el("div","semana-titulo", titulo));
    }
    var concluido = !!PROGRESS.trilhaChecklist[dia.data];
    var isHoje = dia.data === todayIso;
    var item = el("div","dia-item"+(isHoje?" hoje":"")+(concluido?" concluido":""));

    var check = el("div","checkbox", concluido ? "✓" : "");
    check.onclick = function(){
      PROGRESS.trilhaChecklist[dia.data] = !PROGRESS.trilhaChecklist[dia.data];
      saveProgress();
      renderTrilha();
    };
    item.appendChild(check);

    var pillClass = "tipo-"+dia.tipo;
    var conteudo = el("div","conteudo");
    conteudo.innerHTML =
      "<div class='data-tag'>Dia "+dia.dia+" · "+fmtDataBr(dia.data)+(isHoje?" · HOJE":"")+"<span class='tipo-pill "+pillClass+"'>"+dia.tipo+"</span></div>"+
      "<div class='foco'>"+escapeHtml(dia.foco)+"</div>";
    var ul = el("ul");
    dia.tarefas.forEach(function(t){ ul.appendChild(el("li",null,escapeHtml(t))); });
    conteudo.appendChild(ul);

    if(dia.categoriaPratica){
      var btn = el("button","btn pequeno verde","Praticar: "+dia.categoriaPratica);
      btn.style.marginTop = ".5rem";
      btn.onclick = function(){
        iniciarPraticaPorCategoria(dia.categoriaPratica, 10);
      };
      conteudo.appendChild(btn);
    }
    item.appendChild(conteudo);
    root.appendChild(item);
  });
}
function fmtDataBr(iso){
  var p = iso.split("-");
  return p[2]+"/"+p[1]+"/"+p[0];
}

/* =========================================================================
   VIEW: DICAS DE PROVA
   ========================================================================= */
function renderDicas(){
  var root = document.getElementById("view-dicas");
  root.innerHTML = "";

  var c1 = el("div","card");
  c1.innerHTML = "<h2>ℹ️ "+DICAS.sobre_prova.titulo+"</h2>";
  DICAS.sobre_prova.paragrafos.forEach(function(p){ c1.appendChild(el("p",null,escapeHtml(p))); });
  root.appendChild(c1);

  var c2 = el("div","card");
  c2.innerHTML = "<h2>🪜 "+DICAS.metodo_3_degraus.titulo+"</h2>";
  DICAS.metodo_3_degraus.paragrafos.forEach(function(p){ c2.appendChild(el("p",null,escapeHtml(p))); });
  DICAS.metodo_3_degraus.passos.forEach(function(p){
    var d = el("div","passo");
    d.innerHTML = "<b>"+escapeHtml(p.nome)+"</b><br>"+escapeHtml(p.texto);
    c2.appendChild(d);
  });
  root.appendChild(c2);

  var c3 = el("div","card");
  c3.innerHTML = "<h2>⏱️ "+DICAS.gestao_tempo.titulo+"</h2>";
  DICAS.gestao_tempo.paragrafos.forEach(function(p){ c3.appendChild(el("p",null,escapeHtml(p))); });
  var tbl = el("table","tempo-tabela");
  DICAS.gestao_tempo.tabela_tempo.forEach(function(row){
    var tr = el("tr",null,"<td>"+escapeHtml(row.etapa)+"</td><td>"+escapeHtml(row.tempo)+"</td>");
    tbl.appendChild(tr);
  });
  c3.appendChild(tbl);
  c3.appendChild(el("p",null,"<i>"+escapeHtml(DICAS.gestao_tempo.dica_extra)+"</i>"));
  root.appendChild(c3);

  var c4 = el("div","card");
  c4.innerHTML = "<h2>✍️ "+DICAS.guia_discursiva.titulo+"</h2>";
  DICAS.guia_discursiva.paragrafos.forEach(function(p){ c4.appendChild(el("p",null,escapeHtml(p))); });
  DICAS.guia_discursiva.passos.forEach(function(p){
    var d = el("div","passo");
    d.innerHTML = "<b>"+escapeHtml(p.nome)+"</b><br>"+escapeHtml(p.texto);
    c4.appendChild(d);
  });
  c4.appendChild(el("h3",null,"Exemplo real: tema da discursiva do PND 2025"));
  c4.appendChild(el("p",null,"<b>Tema:</b> "+escapeHtml(DISCURSIVA.tema)));
  var ulc = el("ul");
  DISCURSIVA.comando.forEach(function(x){ ulc.appendChild(el("li",null,escapeHtml(x))); });
  c4.appendChild(ulc);
  var detBtn = el("button","btn secundario pequeno","Ver estrutura sugerida e critérios de correção");
  var detBox = el("div","hidden");
  detBox.innerHTML = "<h3 style='margin-top:1rem'>Estrutura sugerida</h3>";
  var ole = el("ol");
  DISCURSIVA.estrutura_sugerida.forEach(function(x){ ole.appendChild(el("li",null,escapeHtml(x))); });
  detBox.appendChild(ole);
  detBox.appendChild(el("h3",null,"Critérios de correção"));
  var ulcc = el("ul");
  DISCURSIVA.criterios_correcao.forEach(function(x){ ulcc.appendChild(el("li",null,escapeHtml(x))); });
  detBox.appendChild(ulcc);
  detBtn.onclick = function(){ detBox.classList.toggle("hidden"); };
  c4.appendChild(detBtn);
  c4.appendChild(detBox);
  root.appendChild(c4);

  var c5 = el("div","card");
  c5.innerHTML = "<h2>✅ "+DICAS.dia_da_prova.titulo+"</h2>";
  DICAS.dia_da_prova.checklist.forEach(function(item, i){
    var row = el("div","checklist-item");
    var cid = "chk-diaprova-"+i;
    row.innerHTML = "<input type='checkbox' id='"+cid+"'><label for='"+cid+"'>"+escapeHtml(item)+"</label>";
    c5.appendChild(row);
  });
  root.appendChild(c5);

  var c6 = el("div","card");
  c6.innerHTML = "<h2>⚠️ "+DICAS.erros_comuns.titulo+"</h2>";
  var ul6 = el("ul");
  DICAS.erros_comuns.lista.forEach(function(x){ ul6.appendChild(el("li",null,escapeHtml(x))); });
  c6.appendChild(ul6);
  root.appendChild(c6);
}

/* =========================================================================
   VIEW: TEORIA (flashcards por tema)
   ========================================================================= */
var teoriaFiltroAtivo = null;
function renderTeoria(){
  var root = document.getElementById("view-teoria");
  root.innerHTML = "";
  root.appendChild(el("div","card","<h2>📚 Resumos e Flashcards de Teoria</h2><p>Toque em cada card para expandir. Filtre por tema para revisar rapidamente antes de um simulado.</p>"));

  var chipRow = el("div","chip-row");
  var chipTodos = el("span","chip"+(teoriaFiltroAtivo===null?" ativo":""), "Todos");
  chipTodos.onclick = function(){ teoriaFiltroAtivo = null; renderTeoria(); };
  chipRow.appendChild(chipTodos);
  TEORIA.forEach(function(bloco){
    var chip = el("span","chip"+(teoriaFiltroAtivo===bloco.categoria?" ativo":""), escapeHtml(bloco.categoria));
    chip.onclick = function(){ teoriaFiltroAtivo = bloco.categoria; renderTeoria(); };
    chipRow.appendChild(chip);
  });
  root.appendChild(chipRow);

  TEORIA.forEach(function(bloco){
    if(teoriaFiltroAtivo && bloco.categoria !== teoriaFiltroAtivo) return;
    var card = el("div","card");
    card.appendChild(el("h2",null,bloco.categoria));
    bloco.cards.forEach(function(c){
      var fc = el("div","flip-card");
      fc.innerHTML = "<h4>"+escapeHtml(c.titulo)+"</h4><span class='dica-toque'>toque para expandir</span><div class='corpo'>"+escapeHtml(c.texto)+"</div>";
      fc.onclick = function(){ fc.classList.toggle("aberto"); };
      card.appendChild(fc);
    });
    root.appendChild(card);
  });
}

/* =========================================================================
   VIEW: BANCO DE QUESTÕES OFICIAIS (navegação/estudo, sem cronômetro)
   ========================================================================= */
var bancoFiltro = "todos";
function renderBanco(){
  var root = document.getElementById("view-banco");
  root.innerHTML = "";
  root.appendChild(el("div","card","<h2>📖 Banco de Questões Oficiais Comentadas</h2><p>As 80 questões reais do PND 2025 (Pedagogia), com gabarito oficial do INEP e justificativa pedagógica própria. Use para estudar com calma — para treinar cronometrado, use o Simulado Oficial.</p>"));

  var card = el("div","card");
  var chipRow = el("div","chip-row");
  ["todos","Formação Geral Docente","Componente Específico (Pedagogia)"].forEach(function(f){
    var chip = el("span","chip"+(bancoFiltro===f?" ativo":""), f==="todos"?"Todos os blocos":f);
    chip.onclick = function(){ bancoFiltro = f; renderBanco(); };
    chipRow.appendChild(chip);
  });
  card.appendChild(chipRow);

  var lista = el("div","lista-questoes-oficiais");
  OFFICIAL.filter(function(q){ return bancoFiltro==="todos" || q.bloco===bancoFiltro; }).forEach(function(q){
    var item = el("div","item");
    item.innerHTML = "<span class='num'>Q"+q.num+"</span><span class='tema-lbl'>"+escapeHtml(q.tema)+"</span>"+(q.anulada?" <span class='tipo-pill tipo-prova'>ANULADA</span>":"");
    item.onclick = function(){ abrirQuestaoOficial(q.num); };
    lista.appendChild(item);
  });
  card.appendChild(lista);
  root.appendChild(card);

  var aviso = el("div","aviso-caveat");
  aviso.innerHTML = "<b>Gabarito conferido:</b> o gabarito destas 80 questões foi conferido item a item com o gabarito oficial divulgado pelo INEP (Caderno 1601, Tipo 01). As justificativas pedagógicas de cada resposta, porém, continuam sendo elaboração própria, com base na BNCC e na legislação educacional vigente — o INEP publica apenas a letra correta, não a justificativa. As questões <b>45 e 52 foram anuladas pelo próprio INEP</b> e são mantidas aqui só para consulta/estudo do tema, sem gabarito e fora da pontuação do Simulado Oficial.";
  root.appendChild(aviso);
}
function abrirQuestaoOficial(num){
  var q = OFFICIAL.find(function(x){ return x.num===num; });
  if(!q) return;
  var modal = document.getElementById("modal-questao");
  var body = document.getElementById("modal-questao-body");
  body.innerHTML = "";
  body.appendChild(el("span","badge-tag", "Q"+q.num+" · "+escapeHtml(q.bloco)));
  body.appendChild(el("h3",null,escapeHtml(q.tema)));
  body.appendChild(el("div","enunciado-texto", nl2br(q.enunciado)));
  ["A","B","C","D"].forEach(function(letra){
    var isCorreta = !q.anulada && letra === q.correta;
    var btn = el("div","alt-btn"+(isCorreta?" correta":""));
    btn.innerHTML = "<span class='letra'>"+letra+"</span><span>"+escapeHtml(q.alternativas[letra])+"</span>";
    body.appendChild(btn);
  });
  var jb = el("div","justificativa-box"+(q.anulada?" errou":""));
  jb.innerHTML = "<span class='rotulo'>"+(q.anulada?"⚠ Questão anulada pelo INEP":"Gabarito: "+q.correta)+"</span>"+escapeHtml(q.justificativa);
  body.appendChild(jb);
  modal.classList.remove("hidden");
}
function fecharModalQuestao(){
  document.getElementById("modal-questao").classList.add("hidden");
}

/* =========================================================================
   QUIZ ENGINE (compartilhado entre Simulado e Praticar)
   ========================================================================= */
var quizState = null; // {questoes, respostas, atual, modo, categoria, startedAt, imediato}

function construirQuizPratica(categorias, quantidade, imediato){
  var pool = PRACTICE.filter(function(q){
    return categorias.length===0 || categorias.indexOf(q.categoria) !== -1;
  });
  var selecionadas = quantidade >= pool.length ? shuffle(pool) : pickRandom(pool, quantidade);
  return {
    questoes: selecionadas,
    respostas: {},
    atual: 0,
    modo: "pratica",
    categoria: categorias.length===1 ? categorias[0] : (categorias.length===0 ? "Todos os temas" : (categorias.length+" temas selecionados")),
    startedAt: Date.now(),
    imediato: imediato,
    finalizado: false
  };
}

function iniciarPraticaPorCategoria(categoria, n){
  quizState = construirQuizPratica([categoria], n, true);
  goTo("praticar", {keepState:true});
  renderQuizAtivo("praticar");
}

/* ---------- SIMULADO SETUP ---------- */
function renderSimuladoSetup(){
  var root = document.getElementById("view-simulado");
  root.innerHTML = "";
  var card = el("div","card");
  card.innerHTML = "<h2>📝 Simulado Oficial — PND 2025 (Pedagogia)</h2>"+
    "<p>As <b>80 questões reais</b> da última prova, na ordem oficial: 30 de Formação Geral Docente + 50 do Componente Específico. Ideal para simular as condições da prova. As questões 45 e 52 foram anuladas pelo INEP e por isso não entram na pontuação (78 questões são de fato avaliadas).</p>";

  var opcoes = el("div","setup-opcoes");
  var op1 = el("label","opcao-radio ativa","<input type='radio' name='simmodo' value='completo' checked> <div><b>Prova completa</b><br><span style='font-size:.8rem;color:var(--cinza-600)'>78 questões pontuáveis (+ 2 anuladas), feedback apenas ao final (mais realista)</span></div>");
  var op2 = el("label","opcao-radio","<input type='radio' name='simmodo' value='parte1'> <div><b>Somente Formação Geral Docente</b><br><span style='font-size:.8rem;color:var(--cinza-600)'>30 questões (1-30)</span></div>");
  var op3 = el("label","opcao-radio","<input type='radio' name='simmodo' value='parte2'> <div><b>Somente Componente Específico</b><br><span style='font-size:.8rem;color:var(--cinza-600)'>50 questões (31-80)</span></div>");
  [op1,op2,op3].forEach(function(o){
    o.querySelector("input").onchange = function(){
      [op1,op2,op3].forEach(function(x){x.classList.remove("ativa");});
      o.classList.add("ativa");
    };
    opcoes.appendChild(o);
  });
  card.appendChild(opcoes);

  var startBtn = el("button","btn roxo","Iniciar simulado");
  startBtn.style.marginTop = "1rem";
  startBtn.onclick = function(){
    var modo = card.querySelector("input[name=simmodo]:checked").value;
    var questoes;
    if(modo==="parte1") questoes = OFFICIAL.filter(function(q){return q.num<=30;});
    else if(modo==="parte2") questoes = OFFICIAL.filter(function(q){return q.num>30;});
    else questoes = OFFICIAL.slice();
    // As questões anuladas pelo INEP não têm gabarito e não devem ser pontuadas.
    questoes = questoes.filter(function(q){ return !q.anulada; });
    quizState = {
      questoes: questoes, respostas:{}, atual:0, modo:"oficial",
      categoria: "Simulado Oficial", startedAt: Date.now(), imediato:false, finalizado:false
    };
    renderQuizAtivo("simulado");
  };
  card.appendChild(startBtn);
  root.appendChild(card);
}

/* ---------- PRATICAR SETUP ---------- */
function renderPraticarSetup(){
  var root = document.getElementById("view-praticar");
  root.innerHTML = "";
  var card = el("div","card");
  card.innerHTML = "<h2>🎯 Praticar por Tema</h2><p>157 questões inéditas, no estilo PND/ENADE, escritas especialmente para este app. Escolha um ou mais temas.</p>";

  var categorias = [];
  PRACTICE.forEach(function(q){ if(categorias.indexOf(q.categoria)===-1) categorias.push(q.categoria); });
  categorias.sort();

  var chipRow = el("div","chip-row");
  var selecionadas = [];
  var chipTodos = el("span","chip ativo","Todos os temas");
  chipTodos.onclick = function(){
    selecionadas = [];
    chipRow.querySelectorAll(".chip").forEach(function(c){c.classList.remove("ativo");});
    chipTodos.classList.add("ativo");
  };
  chipRow.appendChild(chipTodos);
  categorias.forEach(function(cat){
    var count = PRACTICE.filter(function(q){return q.categoria===cat;}).length;
    var chip = el("span","chip", escapeHtml(cat)+" ("+count+")");
    chip.onclick = function(){
      chipTodos.classList.remove("ativo");
      chip.classList.toggle("ativo");
      var idx = selecionadas.indexOf(cat);
      if(chip.classList.contains("ativo")){
        if(idx===-1) selecionadas.push(cat);
      } else {
        if(idx!==-1) selecionadas.splice(idx,1);
      }
      if(selecionadas.length===0) chipTodos.classList.add("ativo");
    };
    chipRow.appendChild(chip);
  });
  card.appendChild(chipRow);

  var row2 = el("div", null, "<b>Quantidade de questões:</b>");
  var qtdSelect = el("select");
  [5,10,15,20,30,999].forEach(function(n){
    var opt = el("option",null, n===999 ? "Todas disponíveis" : n+" questões");
    opt.value = n;
    if(n===10) opt.selected = true;
    qtdSelect.appendChild(opt);
  });
  row2.appendChild(qtdSelect);
  card.appendChild(row2);

  var row3 = el("div", null, "<br><b>Modo de feedback:</b>");
  var modoOpts = el("div","setup-opcoes");
  var m1 = el("label","opcao-radio ativa","<input type='radio' name='pratmodo' value='imediato' checked> <div><b>Imediato</b><br><span style='font-size:.8rem;color:var(--cinza-600)'>Mostra a justificativa após cada resposta (bom para aprender)</span></div>");
  var m2 = el("label","opcao-radio","<input type='radio' name='pratmodo' value='final'> <div><b>Só no final</b><br><span style='font-size:.8rem;color:var(--cinza-600)'>Como um mini-simulado, sem dicas no meio</span></div>");
  [m1,m2].forEach(function(o){
    o.querySelector("input").onchange = function(){
      [m1,m2].forEach(function(x){x.classList.remove("ativa");});
      o.classList.add("ativa");
    };
    modoOpts.appendChild(o);
  });
  row3.appendChild(modoOpts);
  card.appendChild(row3);

  var startBtn = el("button","btn verde","Começar a praticar");
  startBtn.style.marginTop = "1rem";
  startBtn.onclick = function(){
    var n = parseInt(qtdSelect.value,10);
    var imediato = card.querySelector("input[name=pratmodo]:checked").value === "imediato";
    quizState = construirQuizPratica(selecionadas, n, imediato);
    renderQuizAtivo("praticar");
  };
  card.appendChild(startBtn);
  root.appendChild(card);
}

/* ---------- QUIZ ATIVO (renderização compartilhada) ---------- */
function renderQuizAtivo(viewName){
  var root = document.getElementById("view-"+viewName);
  root.innerHTML = "";
  if(!quizState || quizState.questoes.length===0){
    root.appendChild(el("div","card","<p>Nenhuma questão disponível com esse filtro. Volte e ajuste as opções.</p>"));
    return;
  }
  if(quizState.finalizado){ renderResultado(viewName); return; }

  var q = quizState.questoes[quizState.atual];
  var respostaAtual = quizState.respostas[quizState.atual];

  var card = el("div","card");
  var header = el("div","quiz-header");
  header.innerHTML = "<span class='quiz-progress-txt'>"+quizState.categoria+" · Questão "+(quizState.atual+1)+" de "+quizState.questoes.length+"</span>";
  card.appendChild(header);

  var barra = el("div","progressbar");
  var fill = el("div"); fill.style.width = Math.round(((quizState.atual)/quizState.questoes.length)*100)+"%";
  barra.appendChild(fill);
  card.appendChild(barra);

  if(q.bloco) card.appendChild(el("span","badge-tag", "Q"+q.num+" · "+escapeHtml(q.bloco)));
  card.appendChild(el("h3",null,escapeHtml(q.tema || q.categoria)));
  card.appendChild(el("div","enunciado-texto", nl2br(q.enunciado)));

  var mostrarFeedback = (quizState.modo==="pratica" && quizState.imediato && respostaAtual !== undefined);

  ["A","B","C","D"].forEach(function(letra){
    var btn = el("button","alt-btn");
    btn.innerHTML = "<span class='letra'>"+letra+"</span><span>"+escapeHtml(q.alternativas[letra])+"</span>";
    if(respostaAtual !== undefined){
      btn.disabled = true;
      if(letra === respostaAtual) btn.classList.add("selecionada");
      if(quizState.modo==="pratica" && quizState.imediato){
        if(letra === q.correta) btn.classList.add("correta");
        else if(letra === respostaAtual) btn.classList.add("errada");
      }
    } else {
      btn.onclick = function(){
        quizState.respostas[quizState.atual] = letra;
        var acertou = letra === q.correta;
        registrarTema(q.tema || q.categoria, acertou);
        saveProgress();
        renderQuizAtivo(viewName);
      };
    }
    card.appendChild(btn);
  });

  if(mostrarFeedback || (respostaAtual !== undefined && quizState.modo==="pratica" && quizState.imediato)){
    var acertou = respostaAtual === q.correta;
    var jb = el("div","justificativa-box"+(acertou?"":" errou"));
    jb.innerHTML = "<span class='rotulo'>"+(acertou?"✔ Você acertou! ":"✘ Resposta correta: "+q.correta)+"</span>"+escapeHtml(q.justificativa);
    card.appendChild(jb);
  }

  var nav = el("div","btn-row");
  if(quizState.atual > 0){
    var prevBtn = el("button","btn secundario","← Anterior");
    prevBtn.onclick = function(){ quizState.atual--; renderQuizAtivo(viewName); };
    nav.appendChild(prevBtn);
  }
  if(quizState.atual < quizState.questoes.length - 1){
    var nextBtn = el("button","btn", respostaAtual!==undefined ? "Próxima →" : "Pular →");
    nextBtn.onclick = function(){ quizState.atual++; renderQuizAtivo(viewName); };
    nav.appendChild(nextBtn);
  } else {
    var finBtn = el("button","btn roxo","Finalizar e ver resultado");
    finBtn.onclick = function(){ finalizarQuiz(viewName); };
    nav.appendChild(finBtn);
  }
  card.appendChild(nav);
  root.appendChild(card);
}

function finalizarQuiz(viewName){
  quizState.finalizado = true;
  quizState.endedAt = Date.now();
  var total = quizState.questoes.length;
  var corretas = 0;
  quizState.questoes.forEach(function(q, i){
    if(quizState.respostas[i] === q.correta) corretas++;
  });
  registrarQuiz({
    ts: Date.now(),
    modo: quizState.modo,
    categoria: quizState.categoria,
    total: total,
    corretas: corretas,
    duracaoSec: Math.round((quizState.endedAt - quizState.startedAt)/1000)
  });
  renderQuizAtivo(viewName);
}

function renderResultado(viewName){
  var root = document.getElementById("view-"+viewName);
  root.innerHTML = "";
  var total = quizState.questoes.length;
  var corretas = 0;
  var porBloco = {};
  quizState.questoes.forEach(function(q, i){
    var acertou = quizState.respostas[i] === q.correta;
    if(acertou) corretas++;
    var chave = q.bloco || q.categoria;
    if(!porBloco[chave]) porBloco[chave] = {c:0,t:0};
    porBloco[chave].t++;
    if(acertou) porBloco[chave].c++;
  });
  var pct = fmtPct(corretas, total);

  var card = el("div","card");
  var rb = el("div","resultado-box");
  rb.innerHTML = "<div class='pct-grande'>"+pct+"%</div><div class='sub'>"+corretas+" de "+total+" questões corretas — "+quizState.categoria+"</div>";
  card.appendChild(rb);

  Object.keys(porBloco).forEach(function(bloco){
    var s = porBloco[bloco];
    var bp = fmtPct(s.c, s.t);
    var bar = el("div","tema-bar");
    bar.innerHTML = "<span class='nome'>"+escapeHtml(bloco)+"</span><span class='track'><div style='width:"+bp+"%;background:"+corTema(bp)+"'></div></span><span class='pct'>"+bp+"%</span>";
    card.appendChild(bar);
  });

  var btnRow = el("div","btn-row");
  var revBtn = el("button","btn secundario","Revisar todas as questões");
  revBtn.onclick = function(){ mostrarRevisaoCompleta(viewName); };
  btnRow.appendChild(revBtn);
  var novoBtn = el("button","btn","Fazer outro quiz");
  novoBtn.onclick = function(){
    quizState = null;
    goTo(viewName);
  };
  btnRow.appendChild(novoBtn);
  card.appendChild(btnRow);
  root.appendChild(card);
}

function mostrarRevisaoCompleta(viewName){
  var root = document.getElementById("view-"+viewName);
  root.innerHTML = "";
  var back = el("button","btn secundario pequeno","← Voltar ao resultado");
  back.onclick = function(){ renderResultado(viewName); };
  root.appendChild(back);

  quizState.questoes.forEach(function(q, i){
    var resp = quizState.respostas[i];
    var acertou = resp === q.correta;
    var card = el("div","card");
    card.style.borderLeft = "5px solid " + (acertou ? "var(--verde)" : (resp===undefined ? "var(--cinza-400)" : "var(--vermelho)"));
    card.innerHTML = "<span class='badge-tag'>"+(q.num?("Q"+q.num+" · "):"")+escapeHtml(q.tema||q.categoria)+"</span>";
    card.appendChild(el("div","enunciado-texto", nl2br(q.enunciado)));
    ["A","B","C","D"].forEach(function(letra){
      var btn = el("div","alt-btn");
      if(letra===q.correta) btn.classList.add("correta");
      else if(letra===resp) btn.classList.add("errada");
      btn.innerHTML = "<span class='letra'>"+letra+"</span><span>"+escapeHtml(q.alternativas[letra])+"</span>";
      card.appendChild(btn);
    });
    var jb = el("div","justificativa-box"+(acertou?"":" errou"));
    jb.innerHTML = "<span class='rotulo'>Gabarito: "+q.correta+(resp===undefined?" (não respondida)":"")+"</span>"+escapeHtml(q.justificativa);
    card.appendChild(jb);
    root.appendChild(card);
  });

  var back2 = el("button","btn secundario","← Voltar ao resultado");
  back2.onclick = function(){ renderResultado(viewName); };
  root.appendChild(back2);
}

/* =========================================================================
   VIEW: PROGRESSO
   ========================================================================= */
function renderProgresso(){
  var root = document.getElementById("view-progresso");
  root.innerHTML = "";

  var totalResp = 0, totalCorretas = 0;
  Object.keys(PROGRESS.temaStats).forEach(function(k){
    totalResp += PROGRESS.temaStats[k].total;
    totalCorretas += PROGRESS.temaStats[k].correct;
  });

  var card1 = el("div","card");
  card1.innerHTML = "<h2>📊 Meu Progresso</h2><p>Todos os dados abaixo estão salvos apenas neste navegador (localStorage) — ninguém mais tem acesso a eles.</p>";
  var statRow = el("div","stat-row");
  statRow.innerHTML =
    "<div class='stat'><div class='num'>"+totalResp+"</div><div class='lbl'>questões respondidas</div></div>"+
    "<div class='stat'><div class='num'>"+fmtPct(totalCorretas,totalResp)+"%</div><div class='lbl'>acerto geral</div></div>"+
    "<div class='stat'><div class='num'>"+PROGRESS.quizHistory.length+"</div><div class='lbl'>quizzes/simulados</div></div>";
  card1.appendChild(statRow);
  root.appendChild(card1);

  var card2 = el("div","card");
  card2.innerHTML = "<h2>Desempenho por tema</h2>";
  var temasOrdenados = Object.keys(PROGRESS.temaStats).map(function(k){
    return {tema:k, s: PROGRESS.temaStats[k], pct: fmtPct(PROGRESS.temaStats[k].correct, PROGRESS.temaStats[k].total)};
  }).sort(function(a,b){ return a.pct - b.pct; });
  if(temasOrdenados.length===0){
    card2.appendChild(el("p",null,"Nenhum dado ainda. Faça alguns quizzes em Praticar por Tema ou no Simulado Oficial."));
  } else {
    temasOrdenados.forEach(function(t){
      var bar = el("div","tema-bar");
      bar.innerHTML = "<span class='nome'>"+escapeHtml(t.tema)+"</span><span class='track'><div style='width:"+t.pct+"%;background:"+corTema(t.pct)+"'></div></span><span class='pct'>"+t.pct+"%</span>";
      card2.appendChild(bar);
    });
  }
  root.appendChild(card2);

  var card3 = el("div","card");
  card3.innerHTML = "<h2>Histórico de quizzes e simulados</h2>";
  if(PROGRESS.quizHistory.length===0){
    card3.appendChild(el("p",null,"Nenhum quiz realizado ainda."));
  } else {
    var lista = PROGRESS.quizHistory.slice().reverse().slice(0,25);
    lista.forEach(function(h){
      var d = new Date(h.ts);
      var pct = fmtPct(h.corretas, h.total);
      var row = el("div","tema-bar");
      var dataStr = d.toLocaleDateString("pt-BR")+" "+d.toLocaleTimeString("pt-BR",{hour:"2-digit",minute:"2-digit"});
      row.innerHTML = "<span class='nome'>"+dataStr+" — "+escapeHtml(h.categoria)+"</span><span class='track'><div style='width:"+pct+"%;background:"+corTema(pct)+"'></div></span><span class='pct'>"+h.corretas+"/"+h.total+"</span>";
      card3.appendChild(row);
    });
  }
  root.appendChild(card3);

  var card4 = el("div","card");
  card4.innerHTML = "<h2>⚙️ Dados</h2><p>Se quiser recomeçar o acompanhamento do zero (por exemplo, em um novo ciclo de estudos), você pode limpar todo o progresso salvo neste navegador.</p>";
  var resetBtn = el("button","btn vermelho","Limpar todo o progresso");
  resetBtn.onclick = function(){
    if(confirm("Tem certeza? Isso vai apagar todo o histórico de quizzes, a trilha marcada e as estatísticas por tema salvos neste navegador.")){
      PROGRESS = defaultProgress();
      saveProgress();
      renderProgresso();
    }
  };
  card4.appendChild(resetBtn);
  root.appendChild(card4);
}

/* ---------------------------------------------------------------------
   Inicialização
--------------------------------------------------------------------- */
function init(){
  if(!PROGRESS.createdAt){ PROGRESS.createdAt = Date.now(); saveProgress(); }
  renderCountdownMini();
  document.querySelectorAll("#mainnav button").forEach(function(b){
    b.onclick = function(){ goTo(b.getAttribute("data-view")); };
  });
  document.getElementById("modal-fechar").onclick = fecharModalQuestao;
  document.getElementById("modal-questao").onclick = function(e){
    if(e.target.id === "modal-questao") fecharModalQuestao();
  };
  goTo("inicio");
}

window.App = { goTo: goTo, iniciarPraticaPorCategoria: iniciarPraticaPorCategoria };
document.addEventListener("DOMContentLoaded", init);

})();
