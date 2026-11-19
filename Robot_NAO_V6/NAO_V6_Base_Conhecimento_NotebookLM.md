# Robot NAO V6 (H25600) — Base de Conhecimento e Documento-Fonte Mestre (CTE Informático)

> **Contexto do Documento (Fonte Única de Verdade · Web, Manuais, Slides, Vídeos e NotebookLM)**
> - **Instituição / Espaço:** Centro Tecnológico Especializado (CTE) Informático
> - **Equipamento:** Robot Humanoide Programável **NAO V6 (NAO6)** — Modelo **H25600** (Aldebaran / SoftBank Robotics / United Robotics Group)
> - **Código de Inventário CTE:** `INV-217` (**1 unidade única** · Família: Programação e robótica · Local de referência: **Oficinas**)
> - **Idioma Configurado no Robô:** **Português**
> - **Conectividade na Escola:** **Wi-Fi da escola** ou **cabo de rede Ethernet (RJ45)**
> - **Software de Programação:** **Choregraphe Suite 2.8** (compatível com sistema **NAOqi 2.8**; inclui **Robô Virtual**; não requer chave de licença paga)
> - **Público-Alvo:** Professores (todas as áreas), alunos (iniciantes e programação/robótica) e equipa técnica/docentes responsáveis do CTE.
> - **Regra de Ouro Pedagógica do CTE:** Como existe **apenas 1 robô físico (`INV-217`)**, todos os alunos devem **programar e testar primeiro no Robô Virtual do Choregraphe** e transferir para o NAO real apenas após validação do programa.

---

## 1. Visão Geral e Indicadores-Chave (Para Infográficos e Slides)

O **NAO V6 (H25600)** é um robô humanoide autónomo e programável com **25 graus de liberdade** (articulações motorizadas que lhe permitem andar, gesticular, agarrar objetos leves com mãos de 3 dedos e interagir por voz, visão e toque). Executa o sistema operativo embebido **NAOqi 2.8** num processador interno Intel Atom quad-core, podendo funcionar de forma autónoma ou ligado em rede a computadores da escola.

### Cartão de Especificações Rápidas (NAO V6 · H25600)

| Característica | Valor Oficial (NAO V6 / H25600) |
| :--- | :--- |
| **Altura × Largura × Profundidade** | `574 mm × 275 mm × 311 mm` (~58 cm de altura) |
| **Peso Total** | `~5,5 kg` (com bateria instalada) |
| **Graus de Liberdade (Motores)** | `25` (cabeça, braços, mãos de 3 dedos, ancas, pernas e pés) |
| **Processador / Memória** | Intel Atom E3845 (Quad-Core 1,91 GHz) · `4 GB RAM` · `32 GB` armazenamento interno |
| **Bateria** | Iões de Lítio (`21,6 V` · `2,9 Ah` · `62,5 Wh`) |
| **Autonomia Média** | `~60 min` (movimento intenso/caminhada) a `~90 min` (uso normal/diálogo) |
| **Tempo de Carregamento** | `~90 minutos` (carregador `25,2 V DC · 2 A`) |
| **Conectividade** | Wi-Fi (`802.11 a/b/g/n`), Ethernet Gigabit (`RJ45`), Bluetooth (`4.0 BLE`) |
| **Idioma do CTE** | **Português** |

### 6 Atalhos Vitais para Memorizar
- **Tempo de arranque:** `~60 segundos` (não tocar nem mexer no robô até ele dizer **"Ognak Gnouk"**).
- **Descobrir o endereço IP:** **1 clique curto** no botão do peito (o NAO lê o IP em voz alta em Português).
- **Pausar/Retomar Vida Autónoma e libertar motores (*Rest*):** **2 cliques rápidos** no botão do peito.
- **Desligar em segurança:** **Manter premido ~3 segundos** no botão do peito até dizer **"Gnuk Gnuk"** e todos os LEDs apagarem.
- **Paragem de emergência (bloqueio total):** **Manter premido ~8 segundos** no botão do peito *(segurar sempre o robô pelo tronco antes!)*.
- **Regra do chão:** Utilizar o NAO preferencialmente no **chão plano e liso** — nunca perto da borda de uma mesa.

---

## 2. Conteúdo da Mala de Requisição (`INV-217`)

O conjunto requisitado no CTE (`INV-217`) é composto exclusivamente pelos **4 elementos** abaixo (sem acessórios adicionais):

1. **Robot Humanoide NAO V6 (`H25600`):** com a bateria Li-Ion já instalada no compartimento traseiro.
2. **Carregador / Fonte de Alimentação Oficial:** adaptador AC/DC (`25,2 V`) com cabo de corrente.
3. **Cabo de Rede Ethernet (RJ45):** para ligação direta ao computador ou ponto de rede da sala sempre que necessário.
4. **Mala de Transporte Acolchoada:** caixa rígida/moldada de proteção para transporte seguro dentro da escola.

> **Importante:** Confira estes 4 elementos no momento do levantamento e novamente antes da devolução.

---

## 3. Anatomia do Robot NAO V6 (Sensores, Portas, Botões e LEDs)

### 3.1. Mapa de Componentes Físicos

| Zona do Corpo | Componentes Principais | Para Que Servem na Prática |
| :--- | :--- | :--- |
| **Cabeça (Topo e Frente)** | **3 sensores táteis capacitivos** (frente, meio, trás) · **4 microfones omnidirecionais** · **2 altifalantes laterais** · **2 câmaras HD 5 MP** (testa + boca) · **LEDs** nos olhos, orelhas e topo da cabeça | Detetar toques na cabeça, ouvir comandos de voz e localizar quem fala, falar em Português, reconhecer rostos/objetos/marcas *NAOMark* e dar retorno visual colorido. |
| **Cabeça (Tampa Traseira)** | **Porta Ethernet (RJ45)** · **Porta USB** *(escondidas sob a tampa plástica traseira)* | Ligar o NAO por cabo de rede quando o Wi-Fi da escola não está disponível ou para configurar a rede. A porta USB destina-se a manutenção técnica/atualizações. **Nunca deixar o robô andar com cabos ligados atrás da cabeça.** |
| **Tronco (Frente)** | **Botão do Peito** (com LED RGB) · **2 sensores ultrassónicos (sonares)** · **IMU interna** (acelerómetro e giroscópio) | Ligar/desligar, anunciar o IP, ativar/pausar descanso, detetar obstáculos à frente e manter o equilíbrio durante o movimento. |
| **Tronco (Costas)** | **Tomada de carregamento (`25,2 V`)** · **Compartimento da bateria** | Ligar o carregador oficial para recarregar a bateria. **Nunca pôr o robô a caminhar com o carregador ligado.** |
| **Braços e Mãos** | **Mãos de 3 dedos motorizadas** · **3 sensores táteis em cada mão** | Fazer gestos, acenar, segurar objetos muito leves e reagir quando o aluno toca nas mãos. |
| **Pernas e Pés** | **2 para-choques (*bumpers*)** na frente dos pés · **4 sensores de pressão (FSR)** sob cada pé | Detetar colisões dos pés com obstáculos e medir o contacto/peso em cada pé para caminhar sem cair. |

---

### 3.2. Matriz Completa do Botão do Peito

| Estado do NAO | Ação no Botão do Peito | O Que Acontece |
| :--- | :--- | :--- |
| **Desligado** | **1 clique curto (~1 s)** | **Liga o robô.** Os LEDs pulsam durante ~60 s; ao terminar, diz **"Ognak Gnouk"**. |
| **Desligado** | **Manter premido (~4–5 s até ficar azul)** | Modo de recuperação / atualização de firmware *(uso exclusivo técnico — não usar em aula!)*. |
| **Ligado** | **1 clique curto** | O NAO **diz em voz alta o seu nome, endereço IP** e eventuais notificações/alertas. |
| **Ligado** | **2 cliques rápidos (*double-click*)** | Alterna entre **Vida Autónoma / Motores Ativos** e **Modo de Descanso (*Rest* — agacha-se e liberta os motores)**. |
| **Ligado** | **Manter premido (~3 s)** | **Encerramento seguro:** o NAO diz **"Gnuk Gnuk"**, assume postura segura, desliga motores e apaga todos os LEDs. |
| **Ligado (bloqueado)** | **Manter premido (~8 s)** | **Encerramento forçado de emergência:** corta imediatamente a energia. **Segurar sempre o robô pelo tronco** para não cair ao perder a rigidez! |

---

### 3.3. Código de Cores dos LEDs (Diagnóstico Visual Instantâneo)

| Cor / Padrão no Botão do Peito | Significado | Ação Recomendada |
| :--- | :--- | :--- |
| **Branco a pulsar suavemente** *(orelhas a encher)* | **A arrancar** (inicialização e calibração dos sensores) | Aguardar ~60 s **sem tocar nem mover o robô** até ouvir *"Ognak Gnouk"*. |
| **Branco fixo** | **Ligado e pronto** (operação normal) | Pronto para receber ligação ou executar programas. |
| **Verde fixo** | **Bateria saudável** (> 60% de carga) | Pode trabalhar normalmente. |
| **Amarelo / Laranja fixo** | **Bateria média/baixa** (20% a 60%) | Planear carregamento no final da aula. |
| **Vermelho a piscar lentamente** | **Bateria crítica (< 20%)** | Concluir a atividade, colocar em descanso (*Rest*) e ligar o carregador para evitar encerramento súbito. |
| **Branco com flashes curtos** *(verde / amarelo / vermelho)* | **Notificação do sistema** (info / aviso de temperatura / erro) | Dar **1 clique curto no botão do peito** para o NAO ler o aviso em voz alta. |
| **Azul a piscar** | **Ação de sistema / atualização** | Não desligar subitamente; aguardar conclusão ou chamar responsável do CTE. |

---

## 4. Regras de Ouro de Segurança Física (Obrigatórias no CTE)

O NAO V6 é um robô de precisão com 25 motores e engrenagens delicadas, sendo uma **unidade única na escola (`INV-217`)**. O cumprimento destas 7 regras é obrigatório para todos os utilizadores:

1. **Chão Primeiro — Nunca à Beira de Mesas:** Coloque o NAO sempre num **chão plano, limpo e antiderrapante** (ou, para testes estáticos sentados/agachados sem marcha, no centro de uma mesa muito ampla e sempre com um aluno ao lado). Nunca o deixe caminhar sobre mesas, alcatifas felpudas, pisos escorregadios ou perto de escadas e cabos.
2. **Segurar Sempre pelo Tronco/Cintura:** Para levantar ou mover o robô, use **as duas mãos firmemente à volta do tronco/cintura**. **NUNCA** segure nem levante o NAO pela cabeça, braços, pulsos, dedos ou pernas.
3. **Nunca Forçar Articulações Rígidas (*Stiffness ON*):** Se os motores estiverem ligados, **nunca tente dobrar braços, cabeça ou pernas à força** — parte as engrenagens internas. Antes de ajustar a postura à mão, dê **2 cliques no peito** (ou clique em *Rest* no Choregraphe) para libertar os motores.
4. **Cuidado com Dedos nas Articulações:** Os motores têm binário suficiente para entalar dedos. Mantenha sempre as mãos afastadas das juntas (pescoço, ombros, cotovelos, ancas e joelhos) enquanto o robô estiver ligado.
5. **Imobilidade Absoluta Durante o Arranque (~60 s):** Enquanto o NAO liga, calibra automaticamente o giroscópio/IMU. Não lhe toque, não o incline nem o levante até ouvir *"Ognak Gnouk"*.
6. **Zero Cabos em Movimento:** Nunca execute programas de marcha ou dança enquanto o **carregador** ou o **cabo Ethernet** estiverem ligados ao robô (risco de arrancar fichas internas ou provocar quedas).
7. **Vigiar o Aquecimento dos Motores:** Se o robô ficar muito tempo em pé sem se mexer ou executar movimentos intensos repetidos, os motores aquecem (especialmente joelhos e tornozelos). Sempre que estiver a programar/editar código no PC, coloque o NAO em modo **Descanso (*Rest*)** para poupar bateria e arrefecer os servos.

---

## 5. Passo a Passo: Da Mala ao Regresso em 6 Passos

### Passo 1 — Preparar o espaço e retirar o NAO da mala
1. Limpe uma área livre no chão (mínimo `1,5 × 1,5 m`, sem mochilas, cabos nem cadeiras).
2. Abra a mala `INV-217` e verifique os 4 componentes (robô, carregador, cabo Ethernet, mala).
3. Retire o NAO segurando com **as duas mãos pelo tronco**.

### Passo 2 — Posicionar em postura segura (*Crouch*)
1. Pouse o robô no chão em postura de agachamento estável (*Crouch*, joelhos dobrados e pés bem assentes) ou sentado.
2. Confirme que não tem o carregador ligado se pretender fazê-lo andar.

### Passo 3 — Ligar e aguardar calibração
1. Prima o **botão do peito 1 vez (~1 segundo)**.
2. **Afaste as mãos e aguarde cerca de 60 segundos** enquanto os LEDs pulsam.
3. O NAO está pronto quando os olhos acenderem de forma estável e ele disser **"Ognak Gnouk"**.

### Passo 4 — Obter o IP e gerir a Vida Autónoma (*Autonomous Life*)
1. Dê **1 clique curto no botão do peito**: o NAO anuncia o seu **endereço IP** em Português (ex.: *"O meu endereço IP é 192.168..."*). Aponte esse número.
2. **Atenção à Vida Autónoma:** Por defeito, o NAO arranca em modo *Autonomous Life* (olha para as pessoas, abana ligeiramente o corpo e responde espontaneamente).
   - Se for apenas demonstrar interação natural, pode mantê-la ligada.
   - **Se for programar no Choregraphe**, desative/pause a *Autonomous Life* no ícone do coração no Choregraphe (ou coloque em *Rest* com 2 cliques no peito) para evitar que o robô interrompa o programa dos alunos.

### Passo 5 — Ligar ao Choregraphe e executar o programa
1. Garanta que o projeto foi **primeiro testado no Robô Virtual**.
2. Ligue o Choregraphe ao NAO físico (por Wi-Fi da escola ou cabo Ethernet), valide que o espaço em volta está livre e clique em **Play**.
3. Nos intervalos entre testes, clique em **Rest** (descanso) para proteger os motores.

### Passo 6 — Desligar em segurança e arrumar na mala
1. Coloque o robô em postura segura (**Crouch** / **Rest**).
2. **Mantenha o botão do peito premido durante ~3 segundos** até o NAO dizer **"Gnuk Gnuk"**.
3. **Aguarde que TODOS os LEDs apaguem completamente** (cerca de 20–30 segundos) — nunca arrume o robô enquanto ainda houver luzes acesas!
4. Segure pelo tronco, encaixe suavemente o NAO na forma moldada da mala `INV-217`, arrume o carregador e o cabo Ethernet nos seus espaços e feche a mala.

---

## 6. Instalação e Guia Rápido do Choregraphe 2.8 + Robô Virtual

### 6.1. Versão Correta e Requisitos
- **Versão obrigatória:** **Choregraphe Suite 2.8** (ex.: `2.8.6` ou `2.8.7` — a única série compatível com o **NAO V6 / NAOqi 2.8**). *Atenção: o Choregraphe 2.1 (NAO V4/V5) e o 2.5 (Pepper) NÃO funcionam com o NAO V6.*
- **Sistemas suportados:** Windows 10/11 (64-bit), Ubuntu Linux e macOS (verificar compatibilidade em Macs Apple Silicon via emulação/máquina virtual, recomendando-se os PCs Windows do CTE).
- **Licença:** O Choregraphe 2.8 **não exige chave de licença paga** para programar o NAO V6 ou usar o Robô Virtual.

### 6.2. Como Instalar o Choregraphe 2.8 (Windows — Padrão das Salas do CTE)
1. **Obter o instalador:** Descarregue o pacote **Choregraphe Suite 2.8 (Windows 64-bit)** a partir do portal oficial da Aldebaran / United Robotics Group (ou utilize o instalador oficial guardado no repositório interno do CTE, caso o acesso à Internet esteja limitado).
2. **Executar com privilégios de administrador:** Clique com o botão direito no ficheiro `.exe` e escolha **Executar como administrador**.
3. **Seguir o assistente:** Aceite os termos, mantenha a pasta predefinida e aguarde a cópia dos ficheiros. Se o instalador pedir para instalar o **Microsoft Visual C++ Redistributable**, aceite (é necessário para o motor do Robô Virtual).
4. **Firewall do Windows:** Na primeira vez que abrir o Choregraphe, o Windows pedirá permissão na Firewall para `choregraphe` e `naoqi-bin` — selecione **Permitir acesso** (redes privadas e da escola), caso contrário o programa não conseguirá detetar o NAO nem iniciar o Robô Virtual.
5. **Confirmar funcionamento:** Ao abrir o Choregraphe, confirme que o painel **Robot View** (à direita) mostra o NAO V6 virtual em 3D.

### 6.3. Trabalhar Primeiro no Robô Virtual (Fluxo Obrigatório da Turma)
1. No menu superior, vá a **Connection → Connect to virtual robot** (ou use o robô virtual que arranca automaticamente).
2. Arraste caixas da **Box Library** (à esquerda) para a área central (**Flow Diagram**), ligue as entradas/saídas e prima **Play (▶)**.
3. Observe o comportamento no painel **Robot View**:
   - Verifique o texto falado no painel **Dialog** / consola de texto;
   - Verifique se os braços não atravessam o corpo nem desequilibram o robô;
   - Confirme que o programa termina numa postura segura (**Stand** ou **Crouch**).
4. Guarde o projeto (ficheiro `.crg` / pasta do projeto). Só depois de validado pelo professor é que o grupo liga ao NAO físico `INV-217`.

### 6.4. Ligar o Choregraphe ao NAO V6 Físico (Wi-Fi ou Cabo Ethernet)

#### Opção A — Via Wi-Fi da Escola
1. Confirme que o **computador e o NAO V6 estão ligados à mesma rede Wi-Fi** (mesma sub-rede).
2. Dê **1 clique curto no botão do peito** do NAO para ouvir o seu **endereço IP**.
3. No Choregraphe, clique no botão **Connect to** (ícone da antena verde na barra superior).
4. Se o NAO aparecer automaticamente na lista, selecione-o e clique em **Select**.
5. Se não aparecer na lista (comum quando a rede escolar bloqueia descoberta automática mDNS), clique em **"Use fixed IP/hostname"**, introduza o **IP anunciado pelo NAO** (porta `9559`) e clique em **Select**.

#### Opção B — Via Cabo Ethernet (Plano B Mais Fiável em Aula)
1. Com o NAO pousado e parado, abra suavemente a **tampa na parte de trás da cabeça**.
2. Ligue uma ponta do **cabo Ethernet (RJ45)** à porta de rede do NAO e a outra ponta:
   - a uma **tomada de rede da sala** (o NAO recebe IP automático da rede local); **OU**
   - **diretamente à porta Ethernet do computador/portátil** (o NAO atribui um endereço local do tipo `169.254.x.x` após alguns segundos).
3. Dê **1 clique curto no botão do peito** para ouvir o novo endereço IP Ethernet.
4. No Choregraphe, ligue usando esse IP (ou `nao.local`).
5. **Lembrete de segurança:** Com o cabo ligado, execute apenas testes **sem caminhada** (fala, gestos de braços, cabeça, LEDs, visão). Para andar, desligue primeiro o cabo e feche a tampa traseira da cabeça.

### 6.5. Os 5 Botões Essenciais da Barra do Choregraphe
1. **Conectar (Antena Verde):** escolher entre Robô Virtual e NAO físico.
2. **Play (▶) / Stop (■):** iniciar ou parar imediatamente o comportamento atual.
3. **Wake Up (Sol) / Rest (Lua):** acordar o robô (rigidez ON + postura *Stand*) ou colocá-lo em descanso seguro (agacha-se + rigidez OFF).
4. **Autonomous Life (Coração):** clicar para **desligar/pausar** durante as aulas de programação, evitando movimentos e respostas fora do programa.
5. **Controlo de Volume (Altifalante):** ajustar o volume da voz do NAO para a sala de aula.

---

## 7. 5 Mini-Projetos Progressivos para Sala de Aula

Estes projetos servem de base para o Guia de Programação e para os ficheiros exemplo (`.crg`) disponibilizados no portal:

### Projeto 1 — *"Olá, CTE!"* (Nível Iniciante · 15 min)
- **Objetivo:** Fazer o NAO apresentar-se em Português e acenar.
- **Caixas Choregraphe:** `Set Language` (*Portuguese*) → `Wake Up` → `Say` (*"Olá! Eu sou o NAO do CTE Informático."*) + `Animated Say` ou gesto de aceno → `Rest`.
- **Competências:** Sequência lógica, gestão de idioma Português e encerramento seguro em *Rest*.

### Projeto 2 — *"Sensores Táteis e Emoções com LEDs"* (Nível Iniciante · 25 min)
- **Objetivo:** O robô reage de forma diferente consoante o local onde o aluno toca.
- **Caixas Choregraphe:** `Tactile Head` (frente → olhos verdes + *"Olá, tudo bem?"*; meio → olhos azuis + *"A pensar..."*; trás → olhos amarelos + *"Cuidado atrás!"*) + `Eye LEDs` + `Say`.
- **Competências:** Eventos, entradas de sensores capacitivos e feedback visual/sonoro.

### Projeto 3 — *"Coreografia Segura na Timeline"* (Nível Intermédio · 40 min)
- **Objetivo:** Criar uma pequena sequência de movimentos (saudação ou exercício de braços) usando a *Timeline*.
- **Procedimento seguro:** Começar na caixa `Stand`, criar uma caixa `Timeline` com *keyframes* suaves (testando primeiro no Robô Virtual para garantir equilíbrio e ausência de colisões) e terminar em `Stand` ou `Rest`.
- **Competências:** Cinemática, controlo de articulações, interpolação temporal e segurança mecânica.

### Projeto 4 — *"Interação Inteligente (Voz ou Visão)"* (Nível Intermédio · 45 min)
- **Objetivo:** Escolher entre:
  - **Variante A (Voz):** usar `Speech Reco.` (com lista curta de palavras em Português: *"sentar"*, *"levantar"*, *"olá"*, *"parar"*) ligado a `Switch Case` para executar ações. *(Dica: manter a sala em silêncio relativo para melhorar a taxa de reconhecimento.)*
  - **Variante B (Visão):** usar `Face Detection` ou `NAO Mark` para o robô cumprimentar quando vê um rosto ou um cartão visual.
- **Competências:** Perceção artificial, decisão condicional e limitações reais de sensores em ambiente escolar.

### Projeto 5 — *"Primeiros Passos em Python no NAO V6"* (Nível Avançado · 45–60 min)
- **Nota técnica importante:** As caixas **Python Script** dentro do Choregraphe 2.8 executam em **Python 2.7** embebido no NAOqi 2.8 (com os proxies `ALTextToSpeech`, `ALMotion`, `ALRobotPosture`, `ALLeds`). Para projetos externos em Python 3, a equipa técnica pode usar comunicação via ponte/API local ou trabalhar diretamente nos módulos internos do Choregraphe.
- **Exemplo didático mínimo numa caixa Python do Choregraphe:**
```python
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.tts = self.session().service("ALTextToSpeech")
        self.leds = self.session().service("ALLeds")

    def onInput_onStart(self):
        self.tts.setLanguage("Portuguese")
        self.leds.fadeRGB("FaceLeds", 0.0, 0.8, 1.0, 0.5)
        self.tts.say("Olá! Este programa foi escrito em Python no CTE.")
        self.onStopped()
```

### Ideias Interdisciplinares para Professores (Além de Informática)
- **Línguas (Português / Inglês / Francês / Espanhol):** simulações de diálogos curtos, prática de pronúncia e dramatizações guiadas.
- **Educação Especial / Inclusão:** atividades de comunicação estruturada, reconhecimento de emoções e estímulo à interação social (com supervisão docente).
- **Ciências / Matemática:** demonstração de ângulos, coordenadas, sensores ultrassónicos e física do equilíbrio.
- **Eventos da Escola / Dias Abertos:** receção interativa de visitantes e apresentações curtas programadas pelos alunos do CTE.

---

## 8. Guia Técnico, Rede Escolar, Manutenção e Troubleshooting (Equipa CTE)

### 8.1. Página Web Interna do NAO (`http://<IP>`)
- Ao introduzir `http://<IP-do-NAO>` (ou `http://nao.local`) num navegador web (no mesmo segmento de rede), acede-se à consola web do robô.
- **Funções administrativas úteis:**
  - Configurar e gerir redes **Wi-Fi** guardadas;
  - Consultar nível exato da **bateria** e **temperatura de cada motor**;
  - Confirmar idioma predefinido (**Português**) e versão do **NAOqi 2.8**;
  - Gerir atualizações e reiniciar/desligar remotamente.
- **Política de segurança do portal online:** **Nunca publicar palavras-passe reais** (do robô ou da rede Wi-Fi da escola) nos manuais públicos online. Caso seja necessária autenticação na página web do NAO, indicar apenas: *"Solicite apoio ao docente/técnico responsável pelo CTE."*

### 8.2. Boas Práticas para a Rede Wi-Fi da Escola
As redes Wi-Fi escolares têm frequentemente medidas de segurança que afetam robôs autónomos:
- **Portal Cativo (*Captive Portal*):** o NAO não tem ecrã/navegador próprio para preencher formulários web de login. Deve ser ligado a uma rede Wi-Fi da escola sem portal cativo (ex.: rede técnica/equipamentos com WPA2-PSK ou MAC autorizado pelos serviços informáticos).
- **Isolamento de Clientes (*Client / AP Isolation*) ou VLANs diferentes:** se o PC do aluno estiver numa VLAN e o NAO noutra, o Choregraphe não consegue comunicar na porta TCP `9559`.
- **Diagnóstico rápido:** testar `ping <IP-do-NAO>` no PC. Se o Wi-Fi bloquear a comunicação durante uma aula, **passar imediatamente para o cabo Ethernet (RJ45)** incluído na mala.
- **Configurar novo Wi-Fi no NAO:** ligar o NAO por **cabo Ethernet**, obter o IP com 1 clique no peito, abrir `http://<IP>` no navegador do PC, aceder às definições de rede e guardar o Wi-Fi pretendido; depois desligar o cabo Ethernet e confirmar o novo IP Wi-Fi.

### 8.3. Manutenção Preventiva e Limpeza
- **Após aulas com várias turmas:** no Choregraphe (painel *Robot Applications*), remover comportamentos temporários instalados pelos alunos para evitar que fiquem ativos em arranque automático ou encham a memória.
- **Gestão de Bateria:**
  - Carregar sempre que a bateria desça abaixo de **20%–30%**.
  - Evitar deixar o NAO permanentemente ligado à corrente semanas seguidas.
  - **Férias escolares (> 2 semanas sem uso):** desligar totalmente o robô com **40% a 60% de bateria** e guardar em local seco (15 °C–25 °C).
- **Limpeza física:** apenas com o robô **totalmente desligado** e sem carregador. Usar pano de microfibra seco (ou muito ligeiramente humedecido com água pura) para o exterior plástico e pano seco suave nas lentes das câmaras. **Proibido** usar álcool, desinfetantes abrasivos, limpa-vidros ou ar comprimido diretamente nas juntas/microfones.
- **Inspeção periódica (mensal/trimestral):** verificar folgas anormais nas ancas/joelhos, estado das solas dos pés, integridade da ficha do carregador e do cabo Ethernet, e estado do interior da mala.

### 8.4. Tabela de Resolução Rápida de Problemas (*Troubleshooting*)

| N.º | Sintoma | Causas Mais Prováveis | Solução Passo a Passo |
| :-: | :--- | :--- | :--- |
| **1** | **Não liga ao carregar no botão do peito** | Bateria completamente descarregada ou carregador mal encaixado. | Ligar o carregador oficial atrás do tronco durante pelo menos 15 min e verificar se o LED do carregador/botão acende. Tentar ligar novamente (1 clique ~1 s). |
| **2** | **Diz que não tem ligação de rede / não anuncia IP** | Wi-Fi da escola indisponível, senha alterada ou portal cativo. | 1) Confirmar que o Wi-Fi da sala está ativo; 2) Como solução imediata, abrir a tampa atrás da cabeça e ligar o **cabo Ethernet (RJ45)**; 3) Dar 1 clique curto no peito para ouvir o IP Ethernet e aceder a `http://<IP>` se precisar reconfigurar o Wi-Fi. |
| **3** | **Choregraphe não encontra o NAO na rede** | PC e NAO em redes/VLANs diferentes, Firewall do Windows a bloquear, ou mDNS bloqueado. | 1) Usar **"Use fixed IP/hostname"** no Choregraphe com o IP falado pelo NAO (porta `9559`); 2) Permitir `choregraphe` na Firewall do Windows; 3) Verificar se PC e NAO estão na mesma sub-rede ou usar cabo Ethernet direto. |
| **4** | **Erro de incompatibilidade no Choregraphe** | Versão antiga do Choregraphe (2.1 ou 2.5) instalada no PC. | Instalar a versão **Choregraphe 2.8** (compatível com NAOqi 2.8 / NAO V6). |
| **5** | **O NAO mexe-se sozinho ou interrompe o meu programa** | **Vida Autónoma (*Autonomous Life*)** está ativa. | Clicar no ícone do **coração (*Autonomous Life*)** na barra do Choregraphe para a desligar/pausar durante a execução do projeto. |
| **6** | **O programa corre, mas os braços/pernas não se mexem** | Motores sem rigidez (*Stiffness OFF* / modo *Rest*). | Clicar em **Wake Up (Sol)** no Choregraphe (ou confirmar que o programa tem uma caixa `Wake Up` / `Stand` no início). |
| **7** | **Alerta de temperatura / articulação fica mole** | Sobreaquecimento dos motores (muito tempo em pé ou movimentos intensos). | Colocar imediatamente em **Descanso (*Rest*)** durante **10 a 15 minutos** para arrefecer. Não insistir com os motores quentes. |
| **8** | **O NAO desequilibra-se ou cai ao caminhar** | Piso inadequado (alcatifa/escorregadio), robô mexido durante o arranque (IMU descalibrada), ou postura na *Timeline* fora do centro de massa. | 1) Usar apenas piso plano e firme; 2) Reiniciar o NAO totalmente imóvel em *Crouch*; 3) Testar sempre a postura no Robô Virtual antes. |
| **9** | **Não fala em Português ou não reconhece a voz** | Caixa `Set Language` não definida para *Portuguese*, volume baixo, ou ruído excessivo na sala. | Adicionar `Set Language` (*Portuguese*) no início do projeto, subir o volume no Choregraphe e reduzir ruído de fundo (falar a ~50–100 cm de frente para a cabeça). |
| **10** | **Robô totalmente bloqueado e sem resposta** | Falha temporária de software/NAOqi. | 1) **Segurar firmemente o NAO pelo tronco** com uma mão; 2) Manter o **botão do peito premido ~8 segundos** até todos os LEDs apagarem; 3) Aguardar 15 segundos, colocar em *Crouch* no chão e voltar a ligar normalmente. |

### 8.5. Quando Parar Imediatamente e Reportar ao CTE
Suspenda a utilização, desligue o robô e contacte o docente/técnico responsável caso observe:
- Queda de altura (ex.: mesa) ou impacto forte;
- Estalidos metálicos, ruídos de engrenagem a patinar ou junta bloqueada/solta;
- Cheiro a queimado, fumo ou aquecimento anormal na zona da bateria;
- Danos visíveis no carregador, ficha traseira ou tampa da cabeça;
- Erros repetidos de arranque após reinício normal.

---

## 9. Checklist Obrigatória de Requisição e Devolução (`INV-217`)

### Na Entrega (Antes de Iniciar a Aula)
- [ ] Confirmar os **4 itens na mala `INV-217`**: Robot NAO V6, Carregador (`25,2 V`), Cabo Ethernet (RJ45) e Mala acolchoada.
- [ ] Verificar visualmente ausência de danos externos no robô e cabos.
- [ ] Confirmar que a área de trabalho no chão está livre de obstáculos e segura.
- [ ] Relembrar aos alunos as regras de segurança (pegar pelo tronco, não forçar juntas, testar primeiro no Robô Virtual).

### Na Devolução (Antes de Entregar no CTE / Oficinas)
- [ ] **Fechar/parar comportamentos** de teste e remover aplicações temporárias instaladas pelos alunos no NAO (se aplicável).
- [ ] **Desligar corretamente o robô:** posição *Crouch* → premir botão do peito ~3 s (*"Gnuk Gnuk"*) → **aguardar todos os LEDs apagarem completamente**.
- [ ] **Desligar todos os cabos** (carregador e Ethernet) e fechar bem a tampa traseira da cabeça.
- [ ] **Guardar os 4 itens na mala `INV-217`** com o robô bem encaixado na espuma moldada.
- [ ] **Reportar ao responsável do CTE:** avisar se a bateria ficou abaixo de **30%** (para colocar à carga) ou se ocorreu qualquer queda, alerta de temperatura ou anomalia técnica.

---

## 10. Prompts Prontos a Copiar para o Google NotebookLM / Gemini

Carregue este ficheiro (`NAO_V6_Base_Conhecimento_NotebookLM.md`) como fonte no **Google NotebookLM** ou no **Gemini** e utilize os *prompts* abaixo para gerar materiais coerentes em segundos:

### Prompt A — Infográfico Visual A4 de Início Rápido (Online + Plastificar na Mala)
> "Com base na fonte carregada sobre o Robot NAO V6 (H25600 · `INV-217`) do CTE Informático, cria a estrutura visual e o texto completo de um infográfico de iniciação rápida de 1 página A4 em português de Portugal para alunos e professores iniciantes. Organiza em 5 blocos claros: (1) Cabeçalho com 4 números-chave (58 cm / 5,5 kg, 60 s arranque, 1 clique = IP, 60–90 min autonomia); (2) Fluxo numerado de 1 a 6 da mala até desligar em segurança; (3) Quadro compacto dos atalhos do botão do peito e das cores dos LEDs; (4) 5 Regras de Ouro de Segurança em destaque vermelho/âmbar (chão primeiro, pegar pelo tronco, nunca forçar juntas rígidas, zero cabos a andar, simular primeiro no Robô Virtual); (5) Checklist de devolução dos 4 itens na mala `INV-217`. Usa frases curtas, diretas e ícones sugeridos."

### Prompt B — Apresentação de Sala de Aula (10 Diapositivos)
> "A partir do documento-fonte do Robot NAO V6 (`INV-217`) do CTE Informático, cria o plano detalhado de uma apresentação de 10 diapositivos em português de Portugal para o professor projetar antes da primeira aula com o NAO. Para cada diapositivo indica: Título, 3 a 4 tópicos curtos, sugestão visual/esquema e notas do orador. Estrutura: (1) Capa e identificação CTE `INV-217`; (2) O que é o NAO V6 (H25600); (3) Anatomia: sensores, câmaras e portas; (4) Regra de ouro na turma: Robô Virtual primeiro, NAO real depois; (5) Segurança — O que PODE e o que NUNCA fazer; (6) Ligar, aguardar 60 s e descobrir o IP (botão do peito + LEDs); (7) Ligar ao Choregraphe 2.8 (Wi-Fi escolar vs. Cabo Ethernet); (8) Controlar Vida Autónoma, Wake Up e Rest; (9) O primeiro programa em Português (*Olá, CTE!*); (10) Desligar com segurança e checklist de devolução da mala."

### Prompt C — Guiões para 5 Micro-Vídeos Tutoriais (60 a 120 segundos cada)
> "Com base na fonte do Robot NAO V6 (`INV-217`) do CTE Informático, escreve 5 guiões curtos e práticos em português de Portugal para micro-vídeos tutoriais (60 a 120 segundos cada), em formato de tabela com colunas: Tempo | Ação no Ecrã / Câmara | Narração (Voz-off). Os 5 vídeos são: Vídeo 1 — 'Abrir a mala, pegar corretamente e ligar o NAO (90 s)'; Vídeo 2 — '5 erros que NUNCA cometer com o NAO V6 (60 s)'; Vídeo 3 — 'Descobrir o IP e ligar ao Choregraphe por Wi-Fi ou cabo Ethernet (90 s)'; Vídeo 4 — 'Programar primeiro no Robô Virtual e testar no NAO (120 s)'; Vídeo 5 — 'Desligar em segurança e arrumar a mala INV-217 (60 s)'."

### Prompt D — Quiz de Habilitação ("Carta de Condução do NAO V6" · 7 Perguntas)
> "Com base no documento-fonte do Robot NAO V6 (`INV-217`) do CTE Informático, cria um questionário de 7 perguntas de escolha múltipla (4 opções cada + solução explicada) em português de Portugal para validar se um aluno está apto a manusear o NAO físico em segurança. Inclui obrigatoriamente perguntas sobre: por onde segurar o robô, o que nunca fazer quando a rigidez está ativa, porque não tocar durante os 60 s de arranque, como descobrir o endereço IP, o que fazer quando a Vida Autónoma interfere com o programa, qual a versão correta do Choregraphe e como desligar corretamente antes de arrumar na mala."

### Prompt E — Episódio Áudio / *Audio Overview* para Professores
> "Gera um resumo conversacional em português de Portugal (cerca de 4 minutos) dirigido a professores do ensino básico, secundário e profissional que ainda não conhecem o Robot NAO V6 (`INV-217`) do CTE Informático. Explica de forma acessível e entusiasta o que o robô consegue fazer em Português, porque é fácil organizar uma turma inteira com apenas 1 robô usando o Robô Virtual do Choregraphe 2.8, que cuidados básicos garantem zero avarias, e dá 3 ideias rápidas de atividades para diferentes disciplinas."
