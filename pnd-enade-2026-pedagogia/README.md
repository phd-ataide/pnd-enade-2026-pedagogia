# PND/ENADE 2026 — Pedagogia — App de Estudos

App de estudos standalone (HTML + CSS + JS, sem backend) para alunos de Pedagogia se
prepararem para o PND/ENADE 2026, construído a partir da prova real do PND 2025.

## Arquivo pronto para usar

`app.html` — é o app completo, já com todos os dados embutidos. Basta abrir no
navegador (duplo clique). É este arquivo que deve ser distribuído aos alunos.

## Estrutura do projeto (para continuar editando)

```
app/
  style.css              # todo o CSS do app
  app.js                 # toda a lógica JS (navegação, quiz, progresso, etc.)

official_questions.json   # as 80 questões oficiais do PND 2025 (Pedagogia),
                           # com gabarito já conferido com o INEP + justificativas próprias
                           # (questões 45 e 52 estão marcadas "anulada": true)
practice_questions.json   # 157 questões inéditas, estilo PND/ENADE, em 14 temas
trilha.json                # trilha de estudos dia a dia (35 dias, 17/08 a 20/09/2026)
teoria.json                 # resumos/flashcards de teoria, por tema
dicas.json                   # conteúdo da aba "Dicas de Prova"
discursiva_guide.json         # guia da questão discursiva (tema "idadismo")

build_app.py                # monta app.html a partir de tudo acima (CSS+JS+dados)
build_content.py             # gera trilha.json
build_teoria.py               # gera teoria.json
build_dicas.py                 # gera dicas.json

answer_key_original_reference.py  # rascunho original das justificativas (referência
                                    # histórica; os dados atuais já estão em
                                    # official_questions.json, não precisa editar este arquivo)
```

## Como editar

- Para mudar estilo/layout: edite `app/style.css`.
- Para mudar comportamento/telas: edite `app/app.js`.
- Para mudar/adicionar questões, trilha, dicas ou teoria: edite os `.json`
  diretamente (são só arrays/objetos simples), ou regenere via os scripts
  `build_content.py` / `build_teoria.py` / `build_dicas.py` se preferir editar
  o conteúdo em Python.

## Como gerar o app.html final de novo

Depois de qualquer alteração nos `.json`, `app/style.css` ou `app/app.js`, rode
a partir da raiz do projeto:

```bash
python3 build_app.py
```

Isso lê todos os arquivos acima e gera um novo `app.html` (arquivo único,
autocontido, sem dependências externas).

## Observações importantes

- O progresso de cada aluno é salvo só no navegador dele (localStorage) —
  não há servidor nem banco de dados. Isso significa que não existe um
  "painel do professor" agregando o progresso de todos os alunos; cada um
  vê apenas o próprio progresso.
- O gabarito de `official_questions.json` foi conferido item a item com o
  gabarito oficial do INEP (Caderno 1601, Tipo 01). As justificativas
  pedagógicas de cada resposta são elaboração própria (o INEP publica só a
  letra correta, não a explicação).
- Questões 45 e 52 foram anuladas pelo INEP: aparecem no "Banco Comentado"
  com selo "ANULADA", mas são excluídas da pontuação do Simulado Oficial.
