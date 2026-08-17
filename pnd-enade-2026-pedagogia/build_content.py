# -*- coding: utf-8 -*-
"""
Gera o conteúdo estático do app (trilha de 34 dias, dicas de prova, resumos teóricos)
como estruturas Python que serão embutidas no HTML final via json.dumps.
"""
import json
import datetime

CATEGORIAS = [
    "Psicologia da Educação (Piaget, Vygotsky, Wallon)",
    "Legislação Educacional e Formação Docente",
    "Teorias de Currículo",
    "Planejamento de Ensino e Metodologias",
    "Metodologias Ativas e Tecnologias Digitais",
    "Alfabetização e Letramento",
    "BNCC e Educação Infantil",
    "EJA e Paulo Freire",
    "Educação Inclusiva",
    "Relações Étnico-Raciais e Educação Antirracista",
    "Gênero, Sexualidade e Diversidade",
    "Educação do Campo e Educação Ambiental",
    "Gestão Democrática e Escolar",
    "Avaliação da Aprendizagem",
]

# ---------------------------------------------------------------------------
# TRILHA DE ESTUDOS: de 17/08/2026 (hoje) a 20/09/2026 (dia da prova) = 34 dias de estudo + dia da prova
# ---------------------------------------------------------------------------
START = datetime.date(2026, 8, 17)
EXAM = datetime.date(2026, 9, 20)

plan_raw = [
    # (foco, tarefas[], tipo, categoria_pratica or None)
    ("Diagnóstico inicial e panorama do PND 2026", [
        "Leia o guia 'Como funciona o PND 2026' na aba Dicas de Prova.",
        "Faça um mini-diagnóstico: responda 10 questões aleatórias em Praticar por Tema, sem estudar antes.",
        "Releia a LDB (Lei 9.394/1996) — títulos sobre níveis e modalidades de ensino.",
    ], "estudo", "Legislação Educacional e Formação Docente"),
    ("BNCC: estrutura geral e competências", [
        "Estude a estrutura da BNCC: competências gerais, áreas de conhecimento, componentes curriculares.",
        "Relacione a BNCC à BNC-Formação (Resolução CNE/CP 2/2019).",
        "Pratique 10 questões de Legislação Educacional.",
    ], "estudo", "Legislação Educacional e Formação Docente"),
    ("Piaget: estágios do desenvolvimento cognitivo", [
        "Revise os 4 estágios piagetianos e os conceitos de assimilação, acomodação e equilibração.",
        "Pense em 2 exemplos de sala de aula para cada estágio.",
        "Pratique 10 questões de Psicologia da Educação.",
    ], "estudo", "Psicologia da Educação (Piaget, Vygotsky, Wallon)"),
    ("Vygotsky: mediação e Zona de Desenvolvimento Proximal", [
        "Estude ZDP, mediação simbólica e funções psicológicas superiores.",
        "Compare Piaget x Vygotsky em uma tabela própria (maturação x interação social).",
        "Pratique 10 questões de Psicologia da Educação.",
    ], "estudo", "Psicologia da Educação (Piaget, Vygotsky, Wallon)"),
    ("Wallon: afetividade e desenvolvimento integral", [
        "Estude os campos funcionais de Wallon (motor, afetivo, cognitivo) e a noção de sincretismo.",
        "Relacione o estágio do personalismo com situações de sala de aula na Educação Infantil.",
        "Pratique 10 questões mistas de Psicologia da Educação.",
    ], "estudo", "Psicologia da Educação (Piaget, Vygotsky, Wallon)"),
    ("Saberes docentes (Tardif) e formação de professores", [
        "Estude os tipos de saberes docentes segundo Tardif (disciplinares, curriculares, experienciais).",
        "Releia o Texto sobre PNLD e materiais didáticos (Questões 01-02 da prova oficial).",
        "Revise as 10 primeiras questões oficiais comentadas.",
    ], "estudo", "Legislação Educacional e Formação Docente"),
    ("Revisão da Semana 1 + Simulado temático", [
        "Refaça as questões que você errou nos dias 1 a 6 (veja 'Meu Progresso').",
        "Simulado temático: 20 questões misturando os temas da semana.",
        "Descanso ativo: releia seus resumos em voz alta por 15 minutos.",
    ], "revisao", None),

    ("Teorias de Currículo: tradicional, crítico e pós-crítico", [
        "Estude Tomaz Tadeu da Silva, Apple e Giroux — currículo como espaço de poder e ideologia.",
        "Compare com a visão tecnicista/tradicional (Tyler, Bobbitt).",
        "Pratique 10 questões de Teorias de Currículo.",
    ], "estudo", "Teorias de Currículo"),
    ("Gimeno Sacristán: currículo prescrito, moldado e em ação", [
        "Estude os níveis de concretização curricular de Gimeno Sacristán.",
        "Reflita: como a BNCC se transforma do currículo prescrito ao currículo em ação na sua futura sala de aula?",
        "Pratique 10 questões de Teorias de Currículo.",
    ], "estudo", "Teorias de Currículo"),
    ("Planejamento: plano de curso, plano de aula e sequência didática", [
        "Diferencie plano de curso, plano de aula e sequência didática (escalas de planejamento).",
        "Estude o conceito de transposição didática (Chevallard).",
        "Pratique 10 questões de Planejamento de Ensino.",
    ], "estudo", "Planejamento de Ensino e Metodologias"),
    ("Metodologias Ativas I: sala invertida, PBL e ABP", [
        "Estude sala de aula invertida, Aprendizagem Baseada em Problemas (PBL) e em Projetos (ABP).",
        "Liste 3 vantagens e 3 desafios de cada metodologia para a rede pública.",
        "Pratique 10 questões de Metodologias Ativas.",
    ], "estudo", "Metodologias Ativas e Tecnologias Digitais"),
    ("Metodologias Ativas II: gamificação, cultura maker e IA na educação", [
        "Estude gamificação, cultura maker e o uso pedagógico de Inteligência Artificial.",
        "Reflita sobre letramento midiático-informacional e combate a fake news na escola.",
        "Pratique 10 questões de Metodologias Ativas.",
    ], "estudo", "Metodologias Ativas e Tecnologias Digitais"),
    ("Interdisciplinaridade, multidisciplinaridade e transdisciplinaridade", [
        "Diferencie os três conceitos com exemplos concretos de projetos escolares.",
        "Revise as questões oficiais sobre interdisciplinaridade nos Anos Iniciais (tema mais recorrente da prova).",
        "Pratique 10 questões de Planejamento de Ensino.",
    ], "estudo", "Planejamento de Ensino e Metodologias"),
    ("Revisão da Semana 2 + Simulado temático", [
        "Refaça as questões erradas dos dias 8 a 13.",
        "Simulado temático: 20 questões misturando Currículo, Planejamento e Metodologias Ativas.",
        "Descanso ativo: caminhada de 20 minutos sem telas.",
    ], "revisao", None),

    ("Alfabetização x Letramento (Magda Soares)", [
        "Estude a distinção entre alfabetização e letramento segundo Magda Soares.",
        "Reveja os métodos de alfabetização (sintético, analítico, fônico) e o debate atual sobre eles.",
        "Pratique 10 questões de Alfabetização e Letramento.",
    ], "estudo", "Alfabetização e Letramento"),
    ("Psicogênese da escrita (Emilia Ferreiro)", [
        "Estude os níveis da psicogênese: pré-silábico, silábico, silábico-alfabético e alfabético.",
        "Pense em como identificar cada nível a partir de uma amostra de escrita infantil.",
        "Pratique 10 questões de Alfabetização e Letramento.",
    ], "estudo", "Alfabetização e Letramento"),
    ("BNCC na Educação Infantil: Campos de Experiência", [
        "Estude os 5 Campos de Experiência da BNCC para a Educação Infantil.",
        "Relacione cada campo a uma atividade lúdica concreta.",
        "Pratique 10 questões de BNCC e Educação Infantil.",
    ], "estudo", "BNCC e Educação Infantil"),
    ("Paulo Freire I: educação bancária x problematizadora", [
        "Estude a crítica de Freire à 'educação bancária' e a proposta da educação problematizadora.",
        "Releia o conceito de conscientização e o papel do diálogo.",
        "Pratique 10 questões de EJA e Paulo Freire.",
    ], "estudo", "EJA e Paulo Freire"),
    ("Paulo Freire II: investigação temática e palavras geradoras", [
        "Estude o método Paulo Freire: investigação, tematização e problematização; palavras geradoras.",
        "Revise as questões oficiais sobre EJA e cordel (tema forte da prova 2025).",
        "Pratique 10 questões de EJA e Paulo Freire.",
    ], "estudo", "EJA e Paulo Freire"),
    ("EJA: legislação e especificidades do público jovem e adulto", [
        "Estude a legislação da EJA na LDB e as Diretrizes Curriculares Nacionais da modalidade.",
        "Reflita sobre avaliação formativa e não comparativa na EJA (evitar infantilização do adulto).",
        "Pratique 10 questões mistas de EJA e Paulo Freire.",
    ], "estudo", "EJA e Paulo Freire"),
    ("Revisão da Semana 3 + Simulado temático", [
        "Refaça as questões erradas dos dias 15 a 20.",
        "Simulado temático: 20 questões misturando Alfabetização, Educação Infantil e EJA.",
        "Descanso ativo: 20 minutos de leitura não acadêmica.",
    ], "revisao", None),

    ("Educação Inclusiva: LBI e Atendimento Educacional Especializado", [
        "Estude a Lei 13.146/2015 (Lei Brasileira de Inclusão) e o funcionamento do AEE.",
        "Reveja o conceito de tecnologia assistiva e desenho universal para a aprendizagem.",
        "Pratique 10 questões de Educação Inclusiva.",
    ], "estudo", "Educação Inclusiva"),
    ("Educação bilíngue de surdos e Libras", [
        "Estude a Lei 14.191/2021 (educação bilíngue de surdos) e o papel do intérprete de Libras.",
        "Revise a Lei 12.764/2012 (Lei Berenice Piana — TEA) e o PDI (Plano de Desenvolvimento Individual).",
        "Pratique 10 questões mistas de Educação Inclusiva.",
    ], "estudo", "Educação Inclusiva"),
    ("Relações étnico-raciais: Leis 10.639/2003 e 11.645/2008", [
        "Estude a obrigatoriedade do ensino de história e cultura afro-brasileira e indígena.",
        "Reflita sobre racismo institucional, branquitude e currículo eurocêntrico.",
        "Pratique 10 questões de Relações Étnico-Raciais.",
    ], "estudo", "Relações Étnico-Raciais e Educação Antirracista"),
    ("Gênero, sexualidade, nome social e idadismo", [
        "Estude nome social na escola (Resolução MEC 1/2018) e educação para a sexualidade.",
        "Reveja o conceito de idadismo/etarismo e a Lei 14.986/2024 (perspectivas femininas no currículo).",
        "Pratique 10 questões de Gênero, Sexualidade e Diversidade.",
    ], "estudo", "Gênero, Sexualidade e Diversidade"),
    ("Educação do Campo e Educação Ambiental", [
        "Estude a Resolução CNE/CEB 1/2002 (Educação do Campo) e a Lei 9.795/1999 (Educação Ambiental).",
        "Diferencie educação ambiental crítica x conservadora.",
        "Pratique 10 questões de Educação do Campo e Educação Ambiental.",
    ], "estudo", "Educação do Campo e Educação Ambiental"),
    ("Gestão democrática, PPP e Conselho Escolar", [
        "Estude o princípio da gestão democrática (LDB, art. 3º e 14) e a construção coletiva do PPP.",
        "Reveja o papel do coordenador pedagógico como articulador da formação continuada.",
        "Pratique 10 questões de Gestão Democrática e Escolar.",
    ], "estudo", "Gestão Democrática e Escolar"),
    ("Revisão da Semana 4 + Simulado temático", [
        "Refaça as questões erradas dos dias 22 a 27.",
        "Simulado temático: 20 questões misturando Inclusão, Diversidade e Gestão.",
        "Descanso ativo: um dia sem estudar teoria nova — só revisão leve.",
    ], "revisao", None),

    ("Avaliação da aprendizagem (Luckesi)", [
        "Estude a distinção entre avaliação classificatória e avaliação diagnóstica/formativa (Luckesi).",
        "Revise instrumentos de avaliação: portfólio, autoavaliação, observação, feedback.",
        "Pratique 10 questões de Avaliação da Aprendizagem.",
    ], "estudo", "Avaliação da Aprendizagem"),
    ("Avaliação em larga escala: Ideb, Saeb e Indique", [
        "Estude como o Ideb é calculado (fluxo x proficiência) e o papel do Saeb.",
        "Reflita sobre os riscos da racionalidade técnica: 'ensinar para o teste'.",
        "Pratique 10 questões de Avaliação da Aprendizagem.",
    ], "estudo", "Avaliação da Aprendizagem"),
    ("SIMULADO COMPLETO — Parte 1 (questões 1 a 40)", [
        "Faça o Simulado Oficial cronometrado: responda as questões 1 a 40 sem consultar material.",
        "Use no máximo 2h45 (metade do tempo oficial de 5h30).",
        "Não corrija ainda — deixe a correção para o dia seguinte, com a mente descansada.",
    ], "simulado", None),
    ("SIMULADO COMPLETO — Parte 2 (questões 41 a 80) + correção geral", [
        "Complete as questões 41 a 80 do Simulado Oficial, também cronometradas (2h45).",
        "Corrija as duas partes e leia TODAS as justificativas, mesmo das que você acertou.",
        "Anote na aba Meu Progresso os 3 temas com mais erros para reforçar nos próximos dias.",
    ], "simulado", None),
    ("Reforço nos pontos fracos + preparação da discursiva", [
        "Volte a Praticar por Tema focando exatamente nos 3 temas mais fracos identificados ontem.",
        "Leia o Guia da Questão Discursiva na aba Dicas de Prova e treine um rascunho de redação em 30 minutos.",
        "Revise os flashcards de teoria dos autores que ainda geram dúvida.",
    ], "revisao", None),
    ("Revisão leve e organização para o dia da prova", [
        "Revisão leve: releia apenas seus resumos e flashcards, sem novas questões longas.",
        "Organize os documentos exigidos, o local/horário da prova e o trajeto até o local.",
        "Durma pelo menos 7-8 horas. Evite estudar conteúdo novo hoje.",
    ], "descanso", None),
]

assert len(plan_raw) == 34, len(plan_raw)

trilha = []
d = START
for i, (foco, tarefas, tipo, cat) in enumerate(plan_raw, start=1):
    semana = (i - 1) // 7 + 1
    trilha.append({
        "dia": i,
        "data": d.isoformat(),
        "semana": semana,
        "foco": foco,
        "tarefas": tarefas,
        "tipo": tipo,
        "categoriaPratica": cat,
    })
    d += datetime.timedelta(days=1)

# dia da prova
trilha.append({
    "dia": 35,
    "data": EXAM.isoformat(),
    "semana": 5,
    "foco": "DIA DA PROVA — PND 2026",
    "tarefas": [
        "Chegue ao local com pelo menos 1 hora de antecedência.",
        "Leve documento de identificação oficial com foto.",
        "Leia o Guia do Dia da Prova na aba Dicas de Prova antes de dormir hoje.",
        "Confie na sua preparação. Respire, gerencie o tempo e releia cada questão com calma.",
    ],
    "tipo": "prova",
    "categoriaPratica": None,
})

with open("trilha.json", "w", encoding="utf-8") as f:
    json.dump(trilha, f, ensure_ascii=False, indent=2)

print("Trilha gerada:", len(trilha), "dias, de", trilha[0]["data"], "a", trilha[-1]["data"])
