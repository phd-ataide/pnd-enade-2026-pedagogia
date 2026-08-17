# -*- coding: utf-8 -*-
import json

dicas = {
    "sobre_prova": {
        "titulo": "Como funciona o PND 2026",
        "paragrafos": [
            "O Prova Nacional Docente (PND) substitui o ENADE tradicional para os cursos de licenciatura, incluindo Pedagogia. A edição 2026 está prevista para 20 de setembro de 2026, com resultados divulgados em 15 de dezembro de 2026.",
            "A prova tem duração total de 5 horas e 30 minutos e é dividida em dois grandes blocos: Formação Geral Docente (30 questões objetivas + 1 questão discursiva) e Componente Específico da área (50 questões objetivas), no caso de Pedagogia com forte presença de situações-problema e estudos de caso.",
            "As questões do Componente Específico raramente pedem definição pura de conceito: elas apresentam uma situação escolar concreta (um professor, uma turma, um dilema pedagógico) e pedem que você identifique a alternativa que melhor traduz a ação/teoria pedagogicamente correta diante daquela situação.",
            "Este exame de 2025 (usado como base deste aplicativo) confirma esse padrão: praticamente todas as 50 questões do Componente Específico trazem um cenário narrativo antes da pergunta.",
        ],
    },
    "metodo_3_degraus": {
        "titulo": "O Método dos 3 Degraus para questões de situação-problema",
        "paragrafos": [
            "Cursinhos preparatórios e especialistas em provas desse formato (ENADE/PND, concursos de licenciatura) recomendam um método de leitura em 3 degraus para não se perder no texto longo das questões:",
        ],
        "passos": [
            {
                "nome": "1º Degrau — Identifique o cenário e o problema real",
                "texto": "Leia o enunciado procurando responder: quem são os personagens (professor, aluno, gestor)? O que está acontecendo (a ação, a fala, a decisão)? Qual é o problema ou tensão pedagógica ali descrito? Não se prenda a detalhes decorativos da história — foque no núcleo do dilema.",
            },
            {
                "nome": "2º Degrau — Traduza o cenário para um conceito teórico",
                "texto": "Pergunte-se: que autor, teoria ou legislação essa situação está ilustrando? (Ex.: uma criança que só resolve o problema com ajuda de um adulto → ZDP de Vygotsky. Um diretor que decide sozinho sem consultar o colegiado → violação da gestão democrática.) A banca quase sempre está testando se você reconhece a teoria 'disfarçada' de história.",
            },
            {
                "nome": "3º Degrau — Elimine por oposição, não só por acerto",
                "texto": "Leia as 4 alternativas e elimine primeiro as que contradizem diretamente o conceito identificado no 2º degrau, ou que representam a prática/postura claramente equivocada (bancária, punitiva, excludente, tecnicista). Frequentemente 2 das 4 alternativas são absurdas e fáceis de descartar; a decisão real está entre as outras 2 — compare-as quanto a qual é mais completa, atual e alinhada à legislação/teoria vigente.",
            },
        ],
    },
    "gestao_tempo": {
        "titulo": "Gestão do tempo nas 5h30 de prova",
        "paragrafos": [
            "5 horas e 30 minutos parecem muito tempo, mas 81 itens (30 + 50 + 1 discursiva) exigem ritmo. Uma distribuição sugerida por especialistas em provas longas:",
        ],
        "tabela_tempo": [
            {"etapa": "Leitura geral da prova e organização", "tempo": "10 min"},
            {"etapa": "Formação Geral Docente (30 questões objetivas)", "tempo": "70-80 min (~2,5 min/questão)"},
            {"etapa": "Questão discursiva (redação)", "tempo": "40-50 min"},
            {"etapa": "Pausa curta (água, banheiro, respirar)", "tempo": "10 min"},
            {"etapa": "Componente Específico (50 questões, mais longas)", "tempo": "150-160 min (~3 min/questão)"},
            {"etapa": "Revisão final (questões marcadas para revisão)", "tempo": "20-30 min"},
        ],
        "dica_extra": "Marque mentalmente (ou no rascunho) as questões em que você hesitou, e siga adiante sem gastar mais que 3-4 minutos em uma única questão na primeira passada. Muitos candidatos perdem tempo demais em 1 ou 2 questões difíceis e acabam não terminando a prova. Volte às marcadas apenas na revisão final.",
    },
    "guia_discursiva": {
        "titulo": "Guia para a questão discursiva",
        "paragrafos": [
            "A questão discursiva do PND é dissertativo-argumentativa e normalmente traz 2 a 3 textos motivadores (reportagem, trecho de autor, gráfico) seguidos de 2 a 3 comandos específicos que você precisa atender, um a um, na sua redação.",
        ],
        "passos": [
            {"nome": "Passo 1 — Leia os comandos antes dos textos", "texto": "Leia primeiro os comandos (o que exatamente está sendo pedido) e só depois os textos motivadores — assim você já lê os textos filtrando o que é relevante para responder."},
            {"nome": "Passo 2 — Rascunhe a estrutura em 5 blocos", "texto": "Introdução (contextualize o tema com um conceito-chave) → Desenvolvimento 1 (atenda ao 1º comando) → Desenvolvimento 2 (atenda ao 2º comando) → Desenvolvimento 3 / proposta de intervenção (atenda ao 3º comando, se houver, geralmente pedindo uma ação/atividade concreta) → Conclusão (retome a importância do tema)."},
            {"nome": "Passo 3 — Nunca deixe um comando sem resposta", "texto": "Bancas de correção pontuam por comando atendido. Uma redação brilhante que ignora um dos 2-3 comandos perde pontos que uma redação mais simples, mas completa, não perderia. Responda a TODOS os comandos, mesmo que de forma breve."},
            {"nome": "Passo 4 — Cite os textos sem copiá-los", "texto": "Mostre que leu e articulou os textos motivadores com suas próprias palavras e com conceitos teóricos da Pedagogia — cópia literal de trechos é penalizada."},
            {"nome": "Passo 5 — Proposta de intervenção concreta", "texto": "Quando pedirem uma proposta de atividade/ação, seja específico (ex.: 'rodas de conversa intergeracionais com registro de histórias de vida da comunidade') e não genérico (ex.: apenas 'promover a conscientização')."},
        ],
    },
    "dia_da_prova": {
        "titulo": "Checklist do dia da prova",
        "checklist": [
            "Documento de identificação oficial com foto (o mesmo usado na inscrição).",
            "Chegue com pelo menos 1 hora de antecedência ao horário de fechamento dos portões.",
            "Leve água e, se permitido pelo edital, um lanche leve para o intervalo.",
            "Durma bem na noite anterior — não estude conteúdo novo nas últimas 24 horas.",
            "Vista-se em camadas (a temperatura da sala pode variar).",
            "Use o rascunho (se permitido) para anotar suas eliminações do Método dos 3 Degraus.",
            "Nas últimas questões, se o cansaço bater, use a técnica de eliminação: descarte primeiro as alternativas absurdas para reduzir a decisão a 2 opções.",
            "Revise a questão discursiva por último, com atenção à ortografia e à clareza — ela vale proporcionalmente muito na nota.",
        ],
    },
    "erros_comuns": {
        "titulo": "Erros comuns que cursinhos alertam para evitar",
        "lista": [
            "Confundir a teoria com o senso comum: a alternativa 'mais óbvia ao leitor comum' costuma ser a errada, porque a prova testa conhecimento técnico-pedagógico, não intuição.",
            "Escolher a alternativa que parece 'mais gentil' ou 'mais fácil', quando a teoria pede uma ação mais elaborada (ex.: mediação ativa em vez de 'deixar a criança aprender sozinha').",
            "Ignorar a legislação nas alternativas: muitas questões têm uma alternativa correta porque cita corretamente uma lei ou resolução, enquanto as outras trocam nomes de leis/anos.",
            "Não gerenciar o tempo: gastar mais de 5 minutos em uma única questão de situação-problema compromete o restante da prova.",
            "Marcar a resposta certa para a pergunta errada: em textos com 'Texto 1' e 'Texto 2' compartilhados por 2-3 questões, confundir a qual questão uma informação se refere.",
        ],
    },
}

with open("dicas.json", "w", encoding="utf-8") as f:
    json.dump(dicas, f, ensure_ascii=False, indent=2)

print("Dicas geradas com", len(dicas), "seções.")
