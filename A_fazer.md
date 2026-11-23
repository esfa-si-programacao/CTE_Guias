# A Fazer — Portal de Ajuda CTE Informático (7 Equipamentos)

> Lista global de tarefas pendentes e validações de terreno após a **Fase 1 técnica** (23/11/2026):
> `cte-config.js` centralizado, pesquisa sem acentos e com sinónimos, remoção de `manuais.html` (com redirect 301) e publicação limpa para Netlify (`netlify.toml` + `scripts/build_netlify.py`).

---

## 1. Configuração imediata — editar apenas `cte-config.js`

Todas as 9 páginas (página inicial, Ajuda IA e os 7 equipamentos) leem agora os dados a partir de **`cte-config.js`**:

- [ ] **Contacto global do CTE** (`CTE_CONFIG.contactoCTE`): preencher `nome`, `email`, `sala` e `horario`.
- [ ] **Formulário de requisição** (`CTE_CONFIG.urlRequisicao`): colar URL do formulário (ativa automaticamente o botão «Requisitar» no Passo 4 dos 7 equipamentos; se algum equipamento tiver formulário próprio, usar `CTE_CONFIG.equipamentos.<chave>`).
- [ ] **Formulário de devolução** (`CTE_CONFIG.urlRegistoDevolucao`): colar URL (ativa «Registar devolução» quando os 6 itens da checklist estiverem marcados).
- [ ] **Ligar a Carta de Habilitação à requisição:** incluir no formulário de requisição um campo para o código de verificação de 6 caracteres gerado pelo quiz.
- [ ] **Cadernos NotebookLM em falta:** criar e colar em `CTE_CONFIG.notebooks` os links de `einstar` e `tuxedo`.
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

---

## 3. Publicação limpa e higiene do repositório

- [x] `Inventario_CTE_limpo.xlsx` (28,8 MB), `.docx` internos da raiz e `site.txt` movidos para `_interno/` (ignorado em `.gitignore` e excluído do deploy Netlify via `netlify.toml` + `scripts/build_netlify.py`).
- [x] `Robot_NAO_V6/outros/` excluído automaticamente da publicação Netlify e bloqueado no `.htaccess`.
- [ ] **Atenção ao histórico Git:** se o repositório GitHub (`esfa-si-programacao/CTE_Guias`) for público e `Inventario_CTE_limpo.xlsx` contiver dados internos sensíveis (valores, n.ºs de série, etc.), ponderar limpar o histórico Git (ex.: `git filter-repo`) ou tornar o repositório privado.
- [ ] **Recursos ligados em «Para professores e equipa CTE»:** os ficheiros `*_Base_Conhecimento_NotebookLM.md` (nos 7 equipamentos) e os `.docx`/`.pptx` do NAO e Quest 3 mantêm-se publicados porque têm ligações ativas nas páginas. Caso decida retirá-los da web pública, remover primeiro as ligações nos respetivos `index.html`.
- [ ] **Validar fisicamente os QR codes SVG** já embutidos nos 7 `*_Infografico_Inicio_Rapido.html` (apontam para `#diagnostico`).

---

## 4. Próximas fases planeadas

### Fase 2 — Arquitetura partilhada e UX móvel
- [x] Animações CSS realistas dos LEDs (`cte-leds.css`) com pré-visualização ao vivo (`cte-diag.js`) e respeito por `prefers-reduced-motion` nos 7 equipamentos.
- [x] Pesquisa global de sintomas e LEDs em `index.html` via índice gerado automaticamente (`cte-search-index.js` + `scripts/generate_search_index.py`) com abertura direta (`?led=` / `?sym=`).
- [x] Consolidação de `ajuda-ia.html` como vista unificada em `index.html?vista=ia` (com redirects 301), seletor de intenção («1.ª vez / Algo não funciona / Ideias para a aula») e cartões curtos com 1 cor por área, nível e tempo.
- [x] Alvos tácteis ≥ 44 px, texto ≥ 16 px no diagnóstico móvel e barra fixa de atalhos rápidos (`cte-hub.css` + `cte-diag.js`) nos 7 equipamentos.
- [x] Arquivo de `Robot_NAO_V6/Guião_Rápido_do_Robo_Humanoide.png` (4,15 MB) em `_interno/Robot_NAO_V6/`, mantendo `NAO_V6_Guia_Inicio_Rapido_ecra.webp` (150 KB) e `PDF` (86 KB).
- [ ] *(Opcional)* Unificar o restante CSS inline repetido nos 36 ficheiros HTML (manuais, infográficos e quizzes) num `cte-base.css`.

### Fase 3 — Kit visual mínimo (com alunos, 6–8 semanas)
- [ ] 1 vídeo curto (60–90 s) legendado (`.vtt`) por equipamento (começar pelos mais requisitados: Quest 3, RoboMaster TT, Pocket 2, Avata 2; juntar `.vtt` ao vídeo já existente do NAO).
- [ ] Foto real anotada da mala aberta por equipamento (`nao_v6_mala.jpg`, `avata2_kit_mala.jpg`, etc. — blocos já preparados em comentário nos HTML).
- [ ] Cartão QR A6 plastificado para cada mala (`#percurso` + `#diagnostico` + n.º de inventário) e cartão «5 erros comuns».

### Fase 4 — Aprofundar (contínuo)
- [ ] Pequeno validador docente para o código de 6 caracteres da Carta de Habilitação.
- [ ] Botão «Isto ajudou? 👍 / 👎» no diagnóstico ligado a Google Form e galeria de projetos da escola.
- [ ] Fichas de atividade A4, planos de aula (45/90 min) e eventual PWA *network-first* (sem MP4 em precache).
