# -*- coding: utf-8 -*-
import json

teoria = [
    {
        "categoria": "Psicologia da Educação (Piaget, Vygotsky, Wallon)",
        "cards": [
            {"titulo": "Piaget — Estágios do desenvolvimento cognitivo",
             "texto": "Sensório-motor (0-2 anos): inteligência prática, ação sobre objetos. Pré-operatório (2-7): pensamento simbólico, egocentrismo, ausência de reversibilidade. Operatório concreto (7-11): raciocínio lógico sobre o concreto, conservação. Operatório formal (12+): pensamento abstrato e hipotético-dedutivo. Aprendizagem ocorre por assimilação (incorporar o novo aos esquemas existentes), acomodação (ajustar esquemas ao novo) e equilibração (busca de estabilidade cognitiva)."},
            {"titulo": "Vygotsky — Mediação e Zona de Desenvolvimento Proximal (ZDP)",
             "texto": "A aprendizagem é social antes de ser individual (funções psicológicas superiores se desenvolvem na interação). ZDP = distância entre o que a criança faz sozinha (nível real) e o que faz com ajuda de alguém mais experiente (nível potencial). O professor/colega mais experiente atua como mediador, oferecendo 'andaimes' (scaffolding) que são retirados gradualmente. Diferente de Piaget, para Vygotsky a interação social antecede e impulsiona o desenvolvimento."},
            {"titulo": "Wallon — Desenvolvimento integrado e afetividade",
             "texto": "Desenvolvimento ocorre pela integração de quatro campos funcionais: motor, afetivo, cognitivo e pessoa (formação do eu). Estágios: impulsivo-emocional, sensório-motor e projetivo, personalismo (crise de oposição, cerca de 3-6 anos, busca de autonomia e diferenciação), categorial, puberdade/adolescência. Conceito de sincretismo: indiferenciação inicial entre sujeito e meio, entre afetivo e cognitivo. Wallon valoriza a afetividade como constitutiva da aprendizagem, não como acessório."},
            {"titulo": "Tardif — Saberes docentes",
             "texto": "Maurice Tardif classifica os saberes mobilizados pelo professor em: saberes da formação profissional (pedagogia, didática), saberes disciplinares (conteúdos das áreas), saberes curriculares (programas, objetivos, métodos) e saberes experienciais (construídos na prática cotidiana, validados pela experiência). Nenhum saber isolado basta: a docência é um saber plural, construído na articulação entre teoria e prática."},
        ],
    },
    {
        "categoria": "Teorias de Currículo",
        "cards": [
            {"titulo": "Currículo tradicional (técnico)",
             "texto": "Influenciado por Bobbitt e Tyler: currículo como plano técnico e neutro, focado em eficiência, objetivos mensuráveis e organização racional dos conteúdos, próximo da lógica da administração industrial. Visão criticada por ignorar as relações de poder e ideologia presentes na seleção curricular."},
            {"titulo": "Teorias críticas do currículo (Apple, Giroux, Saviani)",
             "texto": "O currículo não é neutro: é um território de disputa de poder e reprodução (ou contestação) das desigualdades sociais. Michael Apple mostra como o currículo oculto reproduz a ideologia dominante; Henry Giroux defende o professor como intelectual transformador. Saviani propõe a Pedagogia Histórico-Crítica: a escola deve socializar o saber elaborado (científico) como instrumento de emancipação das classes populares."},
            {"titulo": "Teorias pós-críticas do currículo (Tomaz Tadeu da Silva)",
             "texto": "Ampliam a crítica além da classe social, incorporando gênero, raça, etnia e identidade cultural. O currículo é entendido como um discurso que produz identidades e diferenças (quem é 'incluído' e quem é 'normalizado'). Base para os debates sobre educação antirracista, de gênero e inclusiva na BNCC."},
            {"titulo": "Gimeno Sacristán — Níveis de concretização curricular",
             "texto": "Currículo prescrito (documentos oficiais, ex.: BNCC), currículo apresentado aos professores (materiais, livros didáticos), currículo moldado pelo professor (planejamento), currículo em ação (o que de fato ocorre em sala), currículo realizado (efeitos/aprendizagens) e currículo avaliado. Mostra que o currículo é reinterpretado em cada etapa — nunca é uma aplicação mecânica do documento oficial."},
        ],
    },
    {
        "categoria": "Planejamento de Ensino e Metodologias",
        "cards": [
            {"titulo": "Plano de curso, plano de aula e sequência didática",
             "texto": "Plano de curso: visão anual/semestral, objetivos gerais e conteúdos por período. Sequência didática: conjunto articulado de aulas sobre um mesmo objeto de conhecimento, com etapas progressivas. Plano de aula: detalhamento operacional de uma aula específica (objetivos, procedimentos, recursos, avaliação). São escalas diferentes de um mesmo planejamento, do mais geral ao mais específico."},
            {"titulo": "Transposição didática (Chevallard)",
             "texto": "Processo de transformação do saber científico/acadêmico em saber escolar, ensinável e adequado ao nível dos estudantes, sem perder o rigor conceitual. Envolve simplificação, contextualização e sequenciação didática do conteúdo especializado."},
            {"titulo": "Interdisciplinaridade x Multidisciplinaridade x Transdisciplinaridade",
             "texto": "Multidisciplinaridade: disciplinas tratam do mesmo tema lado a lado, sem diálogo entre si. Interdisciplinaridade: há efetiva integração e diálogo entre disciplinas na construção do conhecimento (tema mais cobrado na prova). Transdisciplinaridade: transcende os limites disciplinares, buscando uma compreensão unificada além das fronteiras entre as áreas."},
        ],
    },
    {
        "categoria": "Metodologias Ativas e Tecnologias Digitais",
        "cards": [
            {"titulo": "Sala de aula invertida, PBL e ABP",
             "texto": "Sala de aula invertida: o estudo do conteúdo básico ocorre antes da aula (vídeos, textos), e o tempo em sala é usado para aprofundamento e prática. Aprendizagem Baseada em Problemas (PBL): parte de um problema real/complexo para motivar a construção do conhecimento. Aprendizagem Baseada em Projetos (ABP): estudantes desenvolvem um projeto concreto ao longo do tempo, integrando conteúdos e competências."},
            {"titulo": "Gamificação, cultura maker e IA na educação",
             "texto": "Gamificação: uso de elementos de jogos (pontos, níveis, desafios) para engajar sem transformar a aula em jogo completo. Cultura maker: aprender fazendo, criando e prototipando (mão na massa). IA na educação: pode personalizar percursos e dar feedback, mas exige mediação crítica do professor e atenção a viés algorítmico e exclusão digital."},
            {"titulo": "Letramento midiático e combate a fake news",
             "texto": "Letramento midiático-informacional: capacidade de buscar, avaliar criticamente e produzir informação de forma responsável. Diante de fake news, a escola deve promover verificação de fontes, pensamento crítico e produção de conteúdo — nunca censura simples ou relativismo ('cada um com sua verdade')."},
        ],
    },
    {
        "categoria": "Alfabetização e Letramento",
        "cards": [
            {"titulo": "Alfabetização x Letramento (Magda Soares)",
             "texto": "Alfabetização: aprendizagem do sistema de escrita (codificação/decodificação). Letramento: uso social e funcional da leitura e escrita em práticas reais (ler uma bula, escrever uma carta). Magda Soares defende alfabetizar letrando: ensinar o código sem desconectá-lo dos usos sociais da linguagem."},
            {"titulo": "Psicogênese da língua escrita (Emilia Ferreiro)",
             "texto": "Pré-silábico: a criança não relaciona letras a sons, pode usar desenhos ou grafismos. Silábico: uma letra para cada sílaba (com ou sem valor sonoro convencional). Silábico-alfabético: fase de transição, mistura lógica silábica e alfabética. Alfabético: compreende a relação entre fonemas e grafemas de forma sistemática. Não são 'métodos de ensino', mas hipóteses que a própria criança constrói sobre a escrita."},
            {"titulo": "Métodos de alfabetização",
             "texto": "Sintético (fônico/silábico): parte das unidades menores (letras, sílabas) para depois formar palavras. Analítico (global): parte de unidades maiores com sentido (palavras, frases, textos) para depois decompor. O debate atual (BNCC/Política Nacional de Alfabetização) tende a valorizar o método fônico associado a práticas de letramento, sem abandonar o sentido e o contexto.'"},
        ],
    },
    {
        "categoria": "BNCC e Educação Infantil",
        "cards": [
            {"titulo": "Campos de Experiência da BNCC (Educação Infantil)",
             "texto": "1) O eu, o outro e o nós; 2) Corpo, gestos e movimentos; 3) Traços, sons, cores e formas; 4) Escuta, fala, pensamento e imaginação; 5) Espaços, tempos, quantidades, relações e transformações. Substituem a lógica de 'disciplinas' na Educação Infantil, organizando experiências integradas por meio do brincar e das interações."},
            {"titulo": "Direitos de aprendizagem na Educação Infantil",
             "texto": "Conviver, brincar, participar, explorar, expressar e conhecer-se. São a base sobre a qual se organizam os Campos de Experiência, reforçando que a criança pequena aprende primordialmente pela brincadeira e pela interação, não pela instrução formal/decodificação precoce."},
        ],
    },
    {
        "categoria": "EJA e Paulo Freire",
        "cards": [
            {"titulo": "Educação bancária x educação problematizadora (Freire)",
             "texto": "Educação bancária: o professor 'deposita' conteúdo em um aluno passivo, reprodutor. Educação problematizadora: dialógica, parte da realidade concreta dos educandos, estimula a reflexão crítica e a autonomia. Freire defende a superação da relação opressor-oprimido também na sala de aula."},
            {"titulo": "Método Paulo Freire: investigação, tematização, problematização",
             "texto": "Investigação: levantamento do universo vocabular e temático da comunidade (palavras geradoras ligadas à realidade dos educandos). Tematização: organização desses temas em unidades de ensino. Problematização: reflexão crítica sobre os temas, buscando a conscientização (compreensão crítica da própria realidade social para transformá-la)."},
            {"titulo": "EJA — especificidades",
             "texto": "A avaliação e a metodologia na EJA devem respeitar a condição adulta e os saberes de vida dos educandos, evitando compará-los a parâmetros etários do ensino regular infantil (infantilização) ou usar materiais/cartilhas descontextualizados da realidade do público jovem e adulto."},
        ],
    },
    {
        "categoria": "Educação Inclusiva",
        "cards": [
            {"titulo": "Lei Brasileira de Inclusão (Lei 13.146/2015)",
             "texto": "Também chamada Estatuto da Pessoa com Deficiência. Garante educação inclusiva em todos os níveis, adaptações razoáveis, acessibilidade e não discriminação. O Atendimento Educacional Especializado (AEE) complementa (não substitui) o trabalho do professor regente, eliminando barreiras à participação plena do estudante."},
            {"titulo": "Educação bilíngue de surdos (Lei 14.191/2021)",
             "texto": "Reconhece a Libras como primeira língua e o Português escrito como segunda língua para pessoas surdas. Requer intérpretes, tecnologia assistiva, presença de professores/instrutores surdos e envolvimento da família na aprendizagem da Libras."},
            {"titulo": "TEA e tecnologia assistiva (Lei 12.764/2012 — Berenice Piana)",
             "texto": "Institui a Política Nacional de Proteção dos Direitos da Pessoa com Transtorno do Espectro Autista. Na escola, exige Plano de Desenvolvimento Individual (PDI) construído com família e equipe multidisciplinar, uso de tecnologia assistiva para comunicação, e trabalho progressivo com habilidades sociais — sem excluir a família nem dispensar o professor regente."},
        ],
    },
    {
        "categoria": "Relações Étnico-Raciais e Educação Antirracista",
        "cards": [
            {"titulo": "Leis 10.639/2003 e 11.645/2008",
             "texto": "Tornam obrigatório o ensino de História e Cultura Afro-Brasileira e Indígena em todo o currículo (não apenas em datas comemorativas isoladas). Devem ser trabalhadas de forma contínua, crítica e interdisciplinar, evitando reduzir a temática a aspectos superficiais (comida, dança, vestimenta) desconectados da reflexão histórico-política sobre racismo e resistência."},
            {"titulo": "Racismo institucional e currículo eurocêntrico",
             "texto": "Racismo institucional: padrões, normas e práticas das instituições que produzem desvantagens sistemáticas para grupos raciais, muitas vezes de forma não intencional/velada. Currículo eurocêntrico: centra referências, autores e valores europeus/brancos como universais, invisibilizando saberes africanos, indígenas e afro-brasileiros — combatido por uma pedagogia antirracista e decolonial."},
        ],
    },
    {
        "categoria": "Gênero, Sexualidade e Diversidade",
        "cards": [
            {"titulo": "Nome social na escola (Resolução MEC nº 1/2018)",
             "texto": "Garante a estudantes trans e travestis o direito ao uso do nome social em todos os registros de convivência escolar cotidiana (chamada, crachá, diário de classe), independentemente de mudança do registro civil, como medida de respeito à identidade de gênero e combate à evasão escolar."},
            {"titulo": "Idadismo/Etarismo (Lei 14.986/2024 e OMS/OPAS)",
             "texto": "Idadismo: estereótipos, preconceito e discriminação baseados na idade — pode afetar tanto idosos quanto jovens. Na escola, gera silenciamento de vozes intergeracionais. A Lei 14.986/2024 trata das perspectivas femininas no currículo; o combate ao idadismo é reforçado pelo Estatuto do Idoso (Lei 10.741/2003) e por propostas de projetos intergeracionais (ex.: rodas de história oral)."},
        ],
    },
    {
        "categoria": "Educação do Campo e Educação Ambiental",
        "cards": [
            {"titulo": "Educação do Campo (Resolução CNE/CEB 1/2002)",
             "texto": "Reconhece a diversidade dos povos do campo (agricultores, assentados, ribeirinhos, quilombolas) e a necessidade de um currículo contextualizado, articulado ao calendário agrícola e às lutas por terra e trabalho (ex.: pautas do MST), afastando-se de um currículo urbano-cêntrico transplantado sem adaptação."},
            {"titulo": "Educação Ambiental crítica x conservadora (Lei 9.795/1999)",
             "texto": "Educação Ambiental conservadora: foco comportamental individual (reciclar, economizar água), sem questionar as causas estruturais. Educação Ambiental crítica: articula a questão ambiental às dimensões sociais, econômicas e políticas (justiça ambiental, consumo consciente, saberes de povos tradicionais), formando sujeitos capazes de agir coletivamente."},
        ],
    },
    {
        "categoria": "Gestão Democrática e Escolar",
        "cards": [
            {"titulo": "Gestão democrática (LDB art. 3º e 14)",
             "texto": "Princípio constitucional e legal que garante a participação de professores, funcionários, pais e estudantes nas decisões pedagógicas e administrativas da escola, por meio de colegiados (Conselho Escolar, Conselho de Classe, Grêmio, APM). Decisões unilaterais do diretor sem consulta ao colegiado contrariam esse princípio."},
            {"titulo": "Projeto Político-Pedagógico (PPP)",
             "texto": "Documento construído coletivamente pela comunidade escolar, com diagnóstico participativo (entrevistas, questionários), que expressa a identidade, os objetivos e as estratégias pedagógicas da escola. Não deve ser terceirizado, copiado de modelo pronto ou imposto de forma centralizada pela gestão."},
            {"titulo": "Coordenação pedagógica e formação continuada",
             "texto": "O coordenador pedagógico articula a equipe docente, promove formação continuada em serviço com reflexão crítica sobre a prática (relação teoria-prática), e apoia sistematicamente os projetos da escola — função de liderança pedagógica compartilhada, não apenas burocrática ou centralizadora."},
        ],
    },
    {
        "categoria": "Avaliação da Aprendizagem",
        "cards": [
            {"titulo": "Avaliação classificatória x diagnóstica/formativa (Luckesi)",
             "texto": "Avaliação classificatória: seletiva, pontual, usada para aprovar/reprovar (função de controle). Avaliação diagnóstica/formativa: contínua, processual, usada para identificar dificuldades e reorientar o ensino — não para punir. Luckesi defende que a avaliação deve servir à aprendizagem, não à exclusão."},
            {"titulo": "Instrumentos de avaliação processual",
             "texto": "Portfólio, observação, autoavaliação, registros descritivos, feedback/devolutiva qualitativa. Especialmente na Educação Infantil e nos Anos Iniciais, relatórios descritivos substituem notas/testes psicométricos, coerente com uma visão sociointeracionista do desenvolvimento."},
            {"titulo": "Avaliação em larga escala: Ideb e Saeb",
             "texto": "Ideb: combina fluxo escolar (aprovação) e proficiência (Saeb) em um indicador único por escola/rede. Saeb: sistema de avaliação nacional que gera os dados de proficiência. Risco: 'ensinar para o teste' (racionalidade técnica), empobrecendo o currículo. Uso correto: reavaliar periodicamente a proposta pedagógica e direcionar investimento e formação docente, não punir ou promover aprovação automática."},
        ],
    },
    {
        "categoria": "Legislação Educacional e Formação Docente",
        "cards": [
            {"titulo": "LDB — Lei 9.394/1996",
             "texto": "Lei de Diretrizes e Bases da Educação Nacional: organiza os níveis (Educação Básica e Superior) e modalidades (EJA, Educação Especial, Educação do Campo, Educação Profissional, Educação Indígena, Educação a Distância) da educação brasileira. Base legal para praticamente todos os temas cobrados na prova."},
            {"titulo": "BNC-Formação (Resolução CNE/CP 2/2019)",
             "texto": "Base Nacional Comum para a Formação Inicial de Professores da Educação Básica. Estabelece competências específicas para a formação docente, articuladas à BNCC, orientando os cursos de licenciatura (como Pedagogia) em todo o país — é a referência direta para o Componente 'Formação Geral Docente' do PND."},
            {"titulo": "PNLD — Programa Nacional do Livro e do Material Didático",
             "texto": "Programa que avalia, adquire e distribui livros e materiais didáticos gratuitamente às escolas públicas, por meio de etapas (Edital, Inscrição, Avaliação Pedagógica, Escolha, Negociação, Produção, Distribuição e Uso). Tema da questão 1 e 2 da prova oficial 2025."},
        ],
    },
]

with open("teoria.json", "w", encoding="utf-8") as f:
    json.dump(teoria, f, ensure_ascii=False, indent=2)

total_cards = sum(len(c["cards"]) for c in teoria)
print("Categorias de teoria:", len(teoria), "| Total de flashcards:", total_cards)
