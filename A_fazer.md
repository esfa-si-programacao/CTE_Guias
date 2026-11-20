# A Fazer — Portal CTE e Site de Ajuda do Robô NAO V6 (`INV-217`)

> Lista de tarefas pendentes, confirmações técnicas e materiais da **Fase 3** após a implementação das Fases 1 e 2 (20/11/2026).

---

## 1. Configuração imediata (bloco `CONFIG`)

Preencher o bloco `CONFIG` no topo do `<script>` de `Robot_NAO_V6/index.html` (enquanto estiverem vazios, os elementos respetivos permanecem ocultos):

- [ ] **Contacto do CTE** (`CONFIG.contactoCTE`):
  - `nome`: nome do docente / responsável CTE
  - `email`: endereço de e-mail de contacto
  - `sala`: localização / oficina (ex.: Oficinas CTE)
  - `horario`: horário de atendimento / requisição
- [ ] **Formulário de requisição** (`CONFIG.urlRequisicao`): URL do formulário para requisitar o NAO V6 (ativa o link no Passo 4 do percurso).
- [ ] **Formulário de devolução** (`CONFIG.urlRegistoDevolucao`): URL para registar a devolução (ativa o botão «Registar devolução» quando os 6 itens da checklist estiverem marcados).
- [ ] **Ligar a Carta de Condução à requisição (P5):** no formulário de requisição (Google Forms / Apps Script), adicionar um campo para o aluno indicar o **código de verificação de 6 caracteres** gerado pelo cartão de habilitação (`Robot_NAO_V6/NAO_V6_Quiz_Habilitacao.html`).

---

## 2. Confirmações técnicas e testes em escola

- [ ] **Versão do NAOqi e porta de ligação (`9559` vs. `9561`):** confirmar na consola web interna (`http://<IP-do-NAO>`) qual a versão exata do NAOqi instalada no `INV-217` (NAOqi ≤ 2.8.7.4 usa porta `9559`; NAOqi ≥ 2.8.7.7 usa porta `9561`) e atualizar o marcador `<!-- CONFIRMAR -->` em `Robot_NAO_V6/NAO_V6_Manual_Tecnico.html` (e, se for `9561`, atualizar também a explicação da pergunta 11 no Quiz e no Manual de Utilizador).
- [ ] **Software adotado no CTE:** decidir se as aulas usarão apenas **Choregraphe 2.8** ou se também haverá utilização de **Vittascience** (atualmente apenas o Choregraphe 2.8 está publicado).
- [ ] **Limitações do Robô Virtual no Choregraphe 2.8:** validar em sala o marcador `<!-- CONFIRMAR -->` na secção `#s8` de `Robot_NAO_V6/NAO_V6_Manual_Utilizador.html` (projetos 2 e 4 etiquetados como *«Requer NAO físico para testar»*).
- [ ] **Acesso ao Assistente IA (NotebookLM):** testar o link do NotebookLM com uma **conta Google de aluno** da escola para confirmar se o Google Workspace permite o acesso.

---

## 3. Materiais da Fase 3 (fotografias, capturas, legendas e projetos)

### 3.1 Fotografias reais do NAO do CTE (largura máx. 1200 px, JPG/WebP < 300 KB)
Os locais já estão preparados em comentários `<!-- FASE 3 (P1) -->` nos ficheiros HTML. Colocar os ficheiros em `Robot_NAO_V6/`:

- [ ] `nao_v6_foto.jpg` — Fotografia do NAO do CTE de corpo inteiro (substitui `nao_v6.jpg` no topo de `Robot_NAO_V6/index.html`).
- [ ] `nao_v6_botao_peito.jpg` — Botão do peito em grande plano (para o diagnóstico e Guia de Início Rápido).
- [ ] `nao_v6_tampa_ethernet.jpg` — Tampa traseira da cabeça aberta com a porta Ethernet (RJ45) visível (`NAO_V6_Manual_Utilizador.html#s7-2` e diagnóstico «Sem IP»).
- [ ] `nao_v6_mala.jpg` — Mala `INV-217` aberta com os 4 itens arrumados (checklist de devolução em `Robot_NAO_V6/index.html#devolucao`).

### 3.2 Capturas anotadas do Choregraphe 2.8 (< 300 KB cada, em `Robot_NAO_V6/`)
- [ ] `chor_connect_virtual.png` — Ligação ao Robô Virtual (`NAO_V6_Manual_Utilizador.html#s6`).
- [ ] `chor_box_library.png` — Biblioteca de caixas e diagrama de fluxo (`NAO_V6_Manual_Utilizador.html#s6`).
- [ ] `chor_antena_verde.png` — Ícone da Antena Verde na barra superior (`NAO_V6_Manual_Utilizador.html#s7-1`).
- [ ] `chor_fixed_ip.png` — Ligação por *Use fixed IP/hostname* (`NAO_V6_Manual_Utilizador.html#s7-1`).
- [ ] `chor_autonomous_life.png` — Ícone do coração (*Autonomous Life*) para o diagnóstico «Mexe-se sozinho».

### 3.3 Página dedicada aos mini-projetos (P2 — `Robot_NAO_V6/NAO_V6_Projetos.html`)
Para criar a página própria de projetos (e atualizar o atalho em `Robot_NAO_V6/index.html`):
- [ ] Capturas dos diagramas finais dos 5 projetos no Choregraphe 2.8.
- [ ] Projetos prontos a transferir (`projeto1_ola_cte.zip` … `projeto5_python.zip`).
- [ ] Um desafio extra *«E se…?»* por projeto para alunos que terminem mais cedo.

### 3.4 QR codes oficiais offline (P3)
- [ ] Gerar e validar QR code SVG para `https://aem-cte-ajuda.netlify.app/Robot_NAO_V6/#percurso` (para imprimir e colar na mala `INV-217`).
- [ ] Gerar e inserir QR code SVG definitivo para `https://aem-cte-ajuda.netlify.app/Robot_NAO_V6/#diagnostico` no espaço reservado de `Robot_NAO_V6/NAO_V6_Infografico_Inicio_Rapido.html`.

### 3.5 Legendas do vídeo tutorial (P4)
- [ ] Fornecer a transcrição em português do vídeo `Como_Ligar_o_Robo_NAO_e_Descobrir_o_Seu_IP.mp4` para criar `Robot_NAO_V6/Como_Ligar_o_Robo_NAO_e_Descobrir_o_Seu_IP.vtt` e ativar o `<track>` em `Robot_NAO_V6/index.html`.

---

## 4. Sincronização de documentos Office e evolução futura

- [ ] **Atualizar documentos editáveis / PDF:** replicar as correções de texto (terminologia «Robô», «Guia de Início Rápido», nota C13 dos projetos 2 e 4, e novas notas técnicas de BMS/limpeza/portas) nos ficheiros:
  - `Robot_NAO_V6/NAO_V6_Manual_Utilizador.docx`
  - `Robot_NAO_V6/NAO_V6_Manual_Tecnico.docx`
  - `Robot_NAO_V6/NAO_V6_Guia_Inicio_Rapido.docx` e `NAO_V6_Guia_Inicio_Rapido.pdf`
  - `Robot_NAO_V6/NAO_V6_Apresentacao_Sala_Aula.pptx`
- [ ] **Limpeza antes de publicar:** confirmar se a pasta `Robot_NAO_V6/outros/` (rascunhos e auditoria) deve ficar fora da publicação na Netlify.
- [ ] **Melhorias opcionais futuras:**
  - Replicar o novo formato compacto por percurso da página do NAO para `DJI_Avata_Drone/index.html` e `Meta_Quest_3_VR/index.html`.
  - Adaptar para a paleta do CTE (100% offline, sem CDNs) o simulador interativo do botão do peito ou o diagrama clicável de pega segura presentes nos rascunhos de `Robot_NAO_V6/outros/`.
