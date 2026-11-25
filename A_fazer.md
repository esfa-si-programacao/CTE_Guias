# A Fazer — Portal de Ajuda CTE Informático (9 Equipamentos)

> Estado atualizado em **23/11/2026** após a conclusão técnica das **Fases 1 e 2**:
> `cte-config.js` centralizado, pesquisa sem acentos com sinónimos e pesquisa global de sintomas/LEDs (`cte-search-index.js`), animações CSS realistas dos LEDs (`cte-leds.css` + `cte-diag.js`), diagnóstico móvel ≥ 44 px / 16 px + barra fixa (`cte-hub.css`), consolidação de `manuais.html` e `ajuda-ia.html` em `index.html` com seletor de intenção, arquivo do PNG de 4,15 MB do NAO e publicação limpa para Netlify (`netlify.toml` + `scripts/build_netlify.py`, `8,95 MB`, `0` links partidos).
> Experiência comparativa de vídeo/animação IA disponível em `Meta_Quest_3_VR/demo_video/comparar.html`.

---

## 1. Configuração imediata — editar apenas `cte-config.js`

As **10 páginas** (página inicial unificada `index.html` e os 9 equipamentos) leem agora a configuração central a partir de **`cte-config.js`**:

- [ ] **Contacto global do CTE** (`CTE_CONFIG.contactoCTE`): preencher `nome`, `email`, `sala` e `horario`.
- [ ] **Formulário de requisição** (`CTE_CONFIG.urlRequisicao`): colar URL do formulário (ativa automaticamente o botão «Requisitar» no Passo 4 dos equipamentos; se algum equipamento tiver formulário próprio, usar `CTE_CONFIG.equipamentos.<chave>`).
- [ ] **Formulário de devolução** (`CTE_CONFIG.urlRegistoDevolucao`): colar URL (ativa «Registar devolução» quando os 6 itens da checklist estiverem marcados).
- [ ] **Ligar a Carta de Habilitação à requisição:** incluir no formulário de requisição um campo para o código de verificação de 6 caracteres gerado pelo quiz.
- [ ] **Cadernos NotebookLM em falta:** criar e colar em `CTE_CONFIG.notebooks` os links de `einstar`, `tuxedo`, `cricut` e `activpanel`.
- [ ] **Testar NotebookLM com conta Google de aluno:** confirmar se as contas escolares de alunos conseguem abrir os 5 cadernos já ativos sem bloqueio do Google Workspace.

---

## 2. Confirmações técnicas no terreno (14 marcadores `<!-- CONFIRMAR -->`)

### Robô NAO V6 (`INV-217`)
- [ ] **Versão NAOqi e porta (`9559` vs. `9561`):** confirmar na consola web interna (`http://<IP-do-NAO>`) e atualizar `Robot_NAO_V6/NAO_V6_Manual_Tecnico.html` (e Quiz/Manual de Utilizador se for `9561`).
- [ ] **Limitações do Robô Virtual (Choregraphe 2.8):** validar em sala os projetos 2 e 4 em `Robot_NAO_V6/NAO_V6_Manual_Utilizador.html#s8`.

### DJI Avata 2 (`INV-151`)
- [ ] **Registo de operador UAS (ANAC):** confirmar número institucional (`PRT...`) da escola vs. docente responsável e política interna para pavilhão/exterior (`DJI_Avata_Drone/DJI_Avata_2_Manual_Tecnico.html` e `DJI_Avata_2_Manual_Utilizador.html`).

### Meta Quest 3 VR (`INV-081` / `INV-082`)
- [ ] **Capacidade e gestão de contas:** confirmar 128 GB vs. 512 GB e modelo de contas Meta nos 10 kits (`Meta_Quest_3_VR/Meta_Quest_3_Manual_Tecnico.html`).
- [ ] **Lista de apps educativas instaladas:** adaptar a lista às aplicações efetivamente instaladas nos kits (`Meta_Quest_3_VR/Meta_Quest_3_Manual_Utilizador.html`).

### DJI RoboMaster TT (`INV-144`)
- [ ] **Ambiente de programação nos PCs do Estúdio 4C:** confirmar se está instalado Mind+, Python/VS Code (`djitellopy`) ou ambos (`DJI_RoboMaster_TT/RoboMaster_TT_Manual_Utilizador.html`).

### DJI Pocket 2 Creator Combo (`INV-152`)
- [ ] **Cartões microSD e numeração dos kits:** confirmar capacidade dos microSD (64/128 GB U3) e se os 4 kits estão numerados de 1 a 4 (`DJI_Pocket_2_Creator/DJI_Pocket_2_Manual_Tecnico.html`).

### Scanner 3D Einstar (`INV-228`)
- [ ] **Estação de trabalho com EXStar + GPU:** indicar o código exato do PC/Mac compatível no Estúdio SC - LMAS (`Scanner_3D_Einstar/Einstar_Manual_Tecnico.html` e `Einstar_Manual_Utilizador.html`).

### Estação AI Tuxedo Atlas XL (`INV-006`) & NAS QNAP (`INV-223`)
- [ ] **Hardware exato da Tuxedo (`INV-006`):** registar CPU, GPU(s), VRAM, RAM DDR5 e SSDs (`Tuxedo_AI_NAS_QNAP/Tuxedo_NAS_Manual_Tecnico.html` e `Tuxedo_NAS_Manual_Utilizador.html`).
- [ ] **Configuração RAID/ZFS do NAS (`INV-223`):** registar capacidade e nível RAID/ZFS das 8 baías SATA e 2 NVMe (`Tuxedo_AI_NAS_QNAP/Tuxedo_NAS_Manual_Tecnico.html`).
- [ ] **IPs fixos / hostnames reais no Estúdio 4C:** substituir os exemplos pelos IPs/hostnames reais da Tuxedo e do QNAP (`Tuxedo_AI_NAS_QNAP/Tuxedo_NAS_Manual_Utilizador.html`).

### Painéis Interativos Promethean ActivPanel LX 65" (`INV-186`)
- [ ] **Fixação nas 6 salas (`INV-186` / `INV-191`):** confirmar se STEM, TEC1, TEC2 e Hardware D3 estão nos suportes móveis com rodas `INV-191` e se as Oficinas O1 e O3 têm fixação de parede (`Promethean_ActivPanel_LX/ActivPanel_LX_Manual_Utilizador.html`).
- [ ] **RAM/armazenamento dos OPS-A e consola MDM ativa:** confirmar se os OPS-A são 4 GB/32 GB ou 8 GB/64 GB, qual a consola MDM usada (Radix VISO / Promethean Admin Tools / Google Admin) e a lista exata de apps educativas pré-instaladas (`Promethean_ActivPanel_LX/ActivPanel_LX_Manual_Tecnico.html` e `ActivPanel_LX_Manual_Utilizador.html`).

---

## 3. Publicação limpa e higiene do repositório

- [x] `Inventario_CTE_limpo.xlsx` (28,8 MB), `.docx` internos da raiz, `site.txt` e o PNG de 4,15 MB do NAO movidos para `_interno/` (ignorado em `.gitignore` e excluído do deploy Netlify).
- [x] `Robot_NAO_V6/outros/` e `Meta_Quest_3_VR/demo_video/` excluídos automaticamente da publicação Netlify e bloqueados no `.htaccess`.
- [ ] **Atenção ao histórico Git:** se o repositório GitHub (`esfa-si-programacao/CTE_Guias`) for público e `Inventario_CTE_limpo.xlsx` contiver dados internos sensíveis (valores, n.ºs de série, etc.), ponderar limpar o histórico Git (ex.: `git filter-repo`) ou tornar o repositório privado.
- [ ] **Desindexar `Robot_NAO_V6/outros/` do Git (opcional):** a pasta já não vai para a Netlify, mas continua rastreada no GitHub; para a manter só localmente, executar `git rm -r --cached Robot_NAO_V6/outros`.
- [ ] **Recursos ligados em «Para professores e equipa CTE»:** os ficheiros `*_Base_Conhecimento_NotebookLM.md` (nos 7 equipamentos) e os `.docx`/`.pptx` do NAO e Quest 3 mantêm-se publicados porque têm ligações ativas nas páginas. Caso decida retirá-los da web pública, remover primeiro as ligações nos respetivos `index.html`.

---

## 4. Experiência comparativa de vídeo/animação IA — Meta Quest 3 VR (por decidir)

> **Estado:** concluída e isolada em `Meta_Quest_3_VR/demo_video/` (excluída do Git em `.gitignore` e do deploy Netlify em `scripts/build_netlify.py`; a página oficial `Meta_Quest_3_VR/index.html` permanece intacta até à decisão).
> **Como abrir e comparar lado a lado:** `http://localhost/CTE_Guias/Meta_Quest_3_VR/demo_video/comparar.html` (com XAMPP) ou duplo clique em `Meta_Quest_3_VR/demo_video/comparar.html` no Explorador do Windows.

As 3 opções usam o mesmo guião técnico de **6 passos (~57 s)** baseado nas regras do CTE (*Zero sol nas lentes*, *Espaço 2 × 2 m + fitas*, *Ligar 3 s + roda IPD*, *2 toques Passthrough*, *Botão Meta 2 s + Boundary* e *Desligar, limpar e proteger*):

- **Opção 1 — Gemini Notebook / NotebookLM:** prompt otimizado pronto a colar em `Meta_Quest_3_VR/demo_video/prompt_notebooklm_quest3.txt` (e com botão «Copiar prompt» + link direto para o caderno do Meta Quest 3 em `comparar.html`). Replica o formato do vídeo do NAO (~5–6 MB por vídeo, com marca «Gemini Notebook» no final).
- **Opção 2 — Vídeo `.mp4` narrado em PT-PT + legendas `.vtt` gerados localmente com IA:** `Meta_Quest_3_VR/demo_video/Como_Usar_os_Meta_Quest_3.mp4` (`3,76 MB`, `57,3 s`, `720×1280` H.264) e `Como_Usar_os_Meta_Quest_3.vtt`. Combina 6 ilustrações IA em estilo caderno técnico (`demo_video/imgs/`), voz neural em Português Europeu (`pt-PT-RaquelNeural` via `edge-tts`), legendas sincronizadas e ecrã final com o logótipo das Escolas de Mangualde, sem marca de água. Scripts reutilizáveis em `scripts/gen_quest3_tts.py` e `scripts/build_quest3_demo_video.py`.
- **Opção 3 — Player interativo HTML/CSS + 6 ilustrações WebP IA (ultra-leve):** embutido na 3.ª coluna de `comparar.html`, usando as mesmas 6 ilustrações convertidas em WebP (`demo_video/webp/`, **`158,8 KB` no total** — 24× mais leve que o MP4). Funciona 100% offline, permite saltar diretamente para qualquer passo, arranca sem som (ideal para sala de aula) com botão opcional de narração PT-PT e respeita `prefers-reduced-motion`.

**Decisões pendentes desta experiência:**
- [ ] Testar as 3 opções em `Meta_Quest_3_VR/demo_video/comparar.html` e escolher o formato preferido (Opção 1, 2 ou 3).
- [ ] Integrar a opção escolhida no Passo 1 de `Meta_Quest_3_VR/index.html` e replicar para os restantes 5 equipamentos sem vídeo (Avata 2, RoboMaster TT, Pocket 2, Einstar e Tuxedo/NAS).
- [ ] Após integração, remover a pasta temporária `Meta_Quest_3_VR/demo_video/` (e limpar a exclusão temporária em `.gitignore` / `scripts/build_netlify.py`, bem como decidir se mantém os scripts `scripts/gen_quest3_tts.py` e `scripts/build_quest3_demo_video.py` como modelo reutilizável).

---

## 5. Propostas, correções e sugestões das análises ainda por fazer

Lista consolidada de tudo o que foi identificado nas análises e proposto ao longo do projeto, mas que ainda não foi implementado:

### 5.1. Correções técnicas e polimento de código
- [ ] **Legendas `.vtt` para o vídeo do Robô NAO V6:** criar `Robot_NAO_V6/Como_Ligar_o_Robo_NAO_e_Descobrir_o_Seu_IP.vtt` em PT-PT e descomentar o `<track>` em `Robot_NAO_V6/index.html`, permitindo ver o vídeo sem som em sala de aula.
- [ ] **Corrigir `aria-label` dos QR codes nos 6 infográficos A4:** os infográficos do NAO, Avata 2, Quest 3, RoboMaster TT, Pocket 2 e Einstar já incluem um QR SVG real, mas o bloco `<aside class="qr-box">` mantém o texto antigo `aria-label="Espaço para QR Code do portal online"` — atualizar para uma descrição acessível real e testar todos os 7 QRs com telemóvel.
- [ ] **Unificar o CSS e JS inline restantes (`cte-base.css` e `cte-hub.js`):** o portal já partilha `cte-config.js`, `cte-leds.css`, `cte-hub.css`, `cte-diag.js` e `cte-search-index.js`, mas as 36 páginas HTML ativas (hubs, manuais, infográficos e quizzes) ainda repetem CSS base inline e os 7 hubs repetem a lógica de checklist/diagnóstico; extrair para ficheiros partilhados reduz manutenção quando surgirem novos equipamentos.
- [ ] **Preparar marcador de vídeo no Tuxedo AI & NAS QNAP:** ao contrário dos outros 5 equipamentos sem vídeo, `Tuxedo_AI_NAS_QNAP/index.html` ainda não tem o bloco de vídeo previsto no Passo 1 (criar ao integrar a opção de vídeo escolhida).
- [ ] **Sincronizar ou descontinuar os `.docx` / `.pptx` do NAO:** os documentos editáveis em `Robot_NAO_V6/` ainda não têm replicadas algumas correções técnicas recentes das páginas web; decidir se vale a pena mantê-los atualizados ou usar apenas HTML + PDF.

### 5.2. Vídeos, fotografias e materiais visuais (Kit mínimo — Fase 3)
- [ ] **Aplicar a opção de vídeo/animação IA escolhida (ver Secção 4) aos 6 equipamentos em falta:** integrar nos Meta Quest 3 e replicar para Avata 2, RoboMaster TT, Pocket 2, Einstar e Tuxedo/NAS.
- [ ] **Fotografias reais anotadas de cada mala e dos botões principais:** fotografar cada mala aberta com números nas peças (e grandes planos de botões/portas) e descomentar os blocos `<!-- FASE 3 (P1) -->` já preparados nos 7 equipamentos (`nao_v6_mala.jpg`, `avata2_kit_mala.jpg`, `einstar_kit_mala.jpg`, etc.).
- [ ] **Cartões QR A6 plastificados para as 7 malas:** criar página/PDF pronto a imprimir com 1 cartão A6 por equipamento contendo QR para `#percurso`, QR para `#diagnostico` e n.º de inventário (`INV-...`).
- [ ] **Cartão visual «5 erros comuns» por equipamento:** 1 imagem/cartão por equipamento com comparação rápida «✗ Não fazer / ✓ Fazer assim» para afixar ou consultar antes da aula.
- [ ] **Esquemas clicáveis «botões e portas» (SVG interativo):** adaptar para a paleta do CTE (100% offline) o protótipo interativo do NAO já existente em `Robot_NAO_V6/outros/Ajuda_Completa_Robo_NAO.html` (botão do peito e pega segura) e, se resultar bem, replicar para RC Motion 3, comandos Touch Plus, gimbal da Pocket 2 e portas do Einstar/NAS.

### 5.3. Novas funcionalidades de portal, gestão e participação (Fase 4)
- [ ] **Validador docente do código da Carta de Habilitação:** página ou pequena ferramenta offline para professores confirmarem, a partir de nome, turma, data e equipamento, se o código de 6 caracteres gerado nos 7 quizzes é válido.
- [ ] **Progresso visual do percurso (passos 1 a 5) em `localStorage`:** estender a persistência já usada na checklist de devolução para marcar passos concluídos no percurso de cada equipamento (ex.: «Já viste o essencial ✓»).
- [ ] **Glossário partilhado com explicação rápida ao passar o rato / tocar:** explicações breves para termos técnicos (`RTH`, `Casting`, `Boundary`, `IPD`, `Gimbal`, `SDK`, `CUDA`, `ZFS`) sem obrigar a sair da página.
- [ ] **Botão «Isto ajudou? 👍 / 👎» no diagnóstico:** colocar no fim de cada solução de LED/sintoma uma ligação a um Google Form pré-preenchido com equipamento e caso, para identificar o que falta explicar melhor.
- [ ] **Galeria «Projetos da escola»:** secção com fotos/vídeos reais realizados por turmas e clubes com os equipamentos do CTE, para motivar outros professores a requisitar.
- [ ] **Selo «Novidade» configurável na página inicial:** flag simples em `cte-config.js` para destacar novos equipamentos quando forem adicionados ao portal.
- [ ] **Fichas de atividade A4 (aluno) e planos de aula 45/90 min (professor):** modelo comum para os 7 equipamentos, além de materiais específicos sugeridos (árvore de decisão ANAC «Posso voar aqui?» para Avata 2, ficha de higienização do Quest 3, cartões de desafio/cheat sheet Python do RoboMaster TT, storyboard e «6 planos de câmara» da Pocket 2, guia de superfícies do Einstar e cheat sheet Ollama/NAS do Tuxedo).
- [ ] **Modo offline instalável (PWA com *service worker* `network-first`):** permitir instalar o portal no telemóvel com o logótipo das Escolas de Mangualde e aceder ao percurso/diagnóstico sem Wi-Fi (ex.: exterior com o Avata 2), usando estratégia *network-first* e excluindo `.mp4` da pré-cache para evitar versões desatualizadas.

### 5.4. Sugestões avaliadas e deliberadamente adiadas (baixa prioridade)
- [ ] **Interruptor «Sou aluno / Sou professor» nas páginas de equipamento:** adiado porque as 7 páginas já recolhem a área docente em `<details><summary>Para professores e equipa CTE</summary>` e têm texto curto (~720–960 palavras); reavaliar apenas quando houver muitos planos de aula e recursos pedagógicos novos.
- [ ] **Modo escuro automático (`prefers-color-scheme`):** adiado por exigir validação de contraste em 36 páginas e porque as 7 fotografias atuais dos equipamentos (`.jpg`) têm fundo branco sólido, ficando visualmente agressivas sobre fundo escuro.
- [ ] **Podcasts / resumos em áudio (3–5 min) do NotebookLM:** prioridade baixa numa aula prática com o equipamento na mão face a vídeos curtos de 60 s e guias visuais; avaliar apenas se houver interesse específico de algum grupo de docentes.
