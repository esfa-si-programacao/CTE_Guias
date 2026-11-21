# Base de Conhecimento — DJI Avata 2 FPV (CTE Informático)

> **Documento-fonte mestre para o Google NotebookLM**
> Equipamento: **Drone FPV DJI Avata 2 · Óculos DJI Goggles 3 · Comando DJI RC Motion 3**
> Inventário CTE: **INV-151** (4 kits *DJI Avata 2 Pro-View Combo*) + **INV-226** (1× *DJI Avata 2 Intelligent Battery* extra)
> Localização: **Estúdio 4C** — Armário branco com tabuleiros (junto à janela)
> Classificação UE / ANAC: **Classe C1** (~377 g · Categoria Aberta — Subcategoria A1)
> Versão: 1.0 (novembro de 2026) · Língua: Português Europeu (PT-PT)

---

## 1. Resumo do Equipamento e Especificações Oficiais

### 1.1 Aeronave — DJI Avata 2
- **Peso à descolagem:** ~**377 g** · **Classe UE C1** (inclui Identificação Remota Direta e consciencialização geográfica / GEO).
- **Câmara e vídeo:** Sensor CMOS **1/1.3"**, vídeo até **4K @ 60 fps HDR**, campo de visão ultra-grande-angular de **155°**, estabilização eletrónica *RockSteady* / *HorizonSteady*.
- **Armazenamento:** **46 GB de memória interna** + ranhura para cartão **microSD** (recomendado UHS-I V30 / U3) + porta USB-C lateral.
- **Sensores de posicionamento (CRÍTICO):** Visão binocular **apenas para baixo e para trás**. **NÃO possui sensores de obstáculos à frente nem nas laterais!**
- **Bateria inteligente:** Li-ion **2150 mAh / 14,76 V / 31,7 Wh** (~145 g, tensão máx. carga 17 V) · autonomia aproximada até **23 minutos** em condições ideais.
- **Segurança estrutural:** Protetores de hélices integrados na fuselagem, travão imediato (*Hover*), Regresso a Casa (*RTH*) e Modo Tartaruga (*Turtle Mode*).

### 1.2 Óculos — DJI Goggles 3
- **Peso e autonomia:** ~**470 g** (com bateria integrada na banda traseira) · ~**3 horas** de utilização.
- **Real View + PiP:** Câmaras frontais integradas que mostram o ambiente físico real a cores sem tirar os óculos — ativa-se com **2 toques no painel tátil direito dos óculos** ou **2 cliques no dial do RC Motion 3**.
- **Ajuste ótico:** Ajuste de distância interpupilar (IPD) e **dioptrias integradas de −6,0 D a +2,0 D** nos dois botões inferiores.
- **Desembaciamento num toque (*One-Tap Defogging*):** Ventoinha interna ativável no menu dos óculos para eliminar condensação.
- **Cuidado crítico OLED:** **NUNCA expor as lentes internas dos Goggles 3 à luz solar direta** — as lentes concentram a luz como lupas e queimam permanentemente os ecrãs OLED internos em poucos segundos.

### 1.3 Comando — DJI RC Motion 3
- **Peso:** ~**118 g** · Comando ergonómico de uma mão com fita de pulso (usar sempre!).
- **Controlos essenciais:**
  - **Botão Laranja (Lock) — 1 clique em voo:** **TRAVÃO DE EMERGÊNCIA / PAIRAR IMEDIATO** (imobiliza o drone no ar).
  - **Botão Laranja (Lock) — 2 cliques no chão:** Liga (ou desliga, em terra) os motores.
  - **Botão Laranja (Lock) — manter premido:** No chão com motores ligados → **descola automaticamente (~1,2 m)**; em voo pairado → **aterra automaticamente e para os motores**.
  - **Gatilho Acelerador:** Apertar avança na direção do círculo guia AR visto nos Goggles 3; empurrar para a frente recua devagar.
  - **Botão Modo (M):** **1 clique** alterna entre **Modo Normal (N)** (obrigatório na escola) e **Modo Sport (S)**; **manter premido** ativa **Regresso a Casa (RTH)** com GPS (1 clique cancela).
  - **Joystick:** Sobe, desce e desliza lateralmente (*strafe*).
  - **Dial:** Rodar inclina o gimbal; **2 cliques** ativa/desativa *Real View*.
  - **Botão de Disparo (Shutter/Record):** Inicia/para gravação 4K ou tira fotografia.

---

## 2. Regras Legais ANAC / UE (Classe C1) e 5 Regras de Ouro FPV

1. **Observador Visual OBRIGATÓRIO (lei ANAC em FPV):** Como os DJI Goggles 3 bloqueiam a visão direta (*VLOS*), nunca é permitido voar sozinho em Categoria Aberta. Um **Observador Visual** tem de ficar sempre junto ao piloto, mantendo contacto visual direto com o drone (sem binóculos) para vigiar obstáculos, pessoas e espaço aéreo.
2. **Sem sensores frontais nem laterais:** O DJI Avata 2 só tem sensores visuais **em baixo e atrás**. Voar sempre em **Modo Normal (N)** e manter o reflexo do travão imediato (**1× botão laranja Lock**).
3. **Conformidade ANAC Classe C1 (Portugal):**
   - Registo de Operador UAS obrigatório em `https://uas.anac.pt` (número `PRT...` afixado no drone e configurado na Identificação Remota Direta).
   - Formação e exame online A1/A3 obrigatórios em `https://rp.anac.pt`.
   - Consulta obrigatória de zonas geográficas antes de qualquer voo exterior em `https://dnt.anac.pt` (app **Voa na Boa**).
   - Verificação de autorização para captação de imagens aéreas exteriores junto da **AAN** (`https://www.aan.pt`) quando exigível, e cumprimento rigoroso do **RGPD**.
   - Altitude máxima absoluta: **120 metros** acima do solo (em contexto escolar voar muito abaixo). **Nunca sobrevoar aglomerados de pessoas.**
4. **Zero luz solar nas lentes internas dos DJI Goggles 3:** Nunca pousar nem segurar os óculos com as lentes viradas para o sol ou janelas ensolaradas (queima definitiva dos ecrãs OLED). Limpar apenas com pano de microfibra seco.
5. **Pilotar sempre SENTADO:** A imersão FPV pode causar desequilíbrio se o piloto estiver de pé. Sentar numa cadeira/banco estável. Ao menor sinal de tontura ou desorientação: **1 clique no botão laranja (Lock)** para pairar, aterrar (manter Lock) e ativar *Real View* (2 toques lado direito).

---

## 3. Sequência de Arranque, Voo Seguro e Desligar

- **Retirar primeiro o protetor rígido do gimbal** (nunca ligar o Avata 2 com o protetor montado).
- **Ligar / Desligar os 3 equipamentos (sequência DJI):** **1 clique curto + manter premido ~2 segundos** no DJI Avata 2, nos DJI Goggles 3 e no DJI RC Motion 3. Confirmar que pertencem ao mesmo número de kit (`1` a `4`).
- **Verificação pré-voo:** LED verde no Avata 2, *Home Point* confirmado nos Goggles 3 (em exterior), Modo **N** selecionado, dioptrias ajustadas, bateria > 40% e Observador Visual em posição.
- **Modo Tartaruga (*Turtle Mode*):** Se o drone virar ao contrário, **só ativar o Turtle Mode sobre piso plano e limpo**. Em relva alta, areia, gravilha ou junto a obstáculos, desligar os motores e pedir ao Observador para o endireitar manualmente.
- **Transferência de vídeos 4K:** Ligar o cabo USB-C à porta lateral do Avata 2 e copiar os ficheiros (46 GB internos ou cartão microSD) para o computador da turma (ou usar *QuickTransfer* na app DJI Fly).

---

## 4. Tabela de LEDs de Estado do DJI Avata 2

| Padrão do LED | Significado | O que fazer |
|---|---|---|
| **Verde lento** | Sinal GNSS/GPS forte (exterior) | Confirmar *Home Point* nos Goggles 3 e descolar em Modo N. |
| **Verde 2× seguidas** | Posicionamento por visão ativo (sem GPS suficiente) | Voar apenas em espaço amplo, bem iluminado e com chão texturado. |
| **Amarelo lento** | Modo ATTI (sem GPS nem visão estável — deriva!) | Não descolar. Aguardar satélites (exterior) ou melhorar iluminação (interior). |
| **Amarelo rápido** | Ligação perdida com óculos / comando | Confirmar os 3 equipamentos ligados e do mesmo kit; se necessário reemparelhar. |
| **Vermelho / Amarelo alternados** | Interferência magnética / calibração da bússola | Afastar de metais, carros ou betão armado e calibrar seguindo os Goggles 3. |
| **Vermelho a piscar (lento / rápido)** | Bateria baixa / crítica (aterragem iminente) | Regressar e aterrar imediatamente em zona plana. |
| **Vermelho fixo** | Erro crítico de sistema | Não descolar. Ler o aviso nos Goggles 3, reiniciar e entregar ao CTE se persistir. |

---

## 5. Emparelhamento Manual dos 3 Equipamentos (Equipa Técnica)

1. Ligar Avata 2, Goggles 3 e RC Motion 3; confirmar no menu *Estado* dos Goggles 3 que o modelo selecionado é **DJI Avata 2**.
2. **Avata 2 ↔ Goggles 3:** Manter premido o botão de energia do Avata 2 por **> 4 segundos** (1 sinal sonoro + LEDs em sequência) e manter premido o botão de energia dos Goggles 3 até apitarem continuamente (ou iniciar pelo menu dos óculos). Aguardar até o som parar e surgir imagem.
3. **Goggles 3 ↔ RC Motion 3:** Manter premido o botão de energia dos Goggles 3 (sinal contínuo + LEDs em sequência) e manter premido o botão de energia do RC Motion 3 até ambos pararem de apitar e estabilizarem os LEDs.

---

## 6. Resolução Rápida de Problemas (10 Casos)

1. **Não liga:** Usar sequência DJI (**1 clique curto + manter ~2 s**); um clique simples só mostra a carga. Se não acender, carregar via USB-C PD 20–30 min.
2. **Sem imagem nos Goggles 3 / LED amarelo rápido:** Confirmar que os 3 equipamentos são do mesmo kit (`1–4`), verificar modelo *DJI Avata 2* nos óculos e reemparelhar se necessário.
3. **Motores não arrancam:** Verificar se o protetor do gimbal foi retirado, ler aviso nos Goggles 3 (zona GEO, bateria) e aplicar sequência **2× Lock → manter**.
4. **LED vermelho/amarelo alternado:** Afastar de estruturas metálicas e calibrar a bússola nos Goggles 3.
5. **LED amarelo lento (ATTI):** Não descolar com alunos; aguardar GPS no exterior ou melhorar luz/textura do piso no interior.
6. **Imagem desfocada / lentes embaciadas:** Ajustar rodas inferiores de dioptrias (−6 a +2 D) e IPD; ativar *Desembaciamento num Toque (Defogging)*; limpar só com microfibra seca.
7. **Erro de gimbal / vibração na imagem:** Desligar, verificar se não ficou protetor montado, inspecionar as 4 hélices (trocar se rachadas/empenadas) e calibrar o gimbal nos óculos.
8. **Gravação 4K para ou cartão lento:** Libertar espaço nos 46 GB internos ou usar microSD UHS-I V30/U3 formatado nos óculos.
9. **Drone caiu virado ao contrário:** Só usar *Turtle Mode* em piso plano e limpo; em relva/areia/pedras, desligar motores e virar à mão.
10. **Mancha colorida permanente no ecrã dos Goggles 3:** Queimadura solar nos OLED (irreversível) — retirar óculos de serviço e comunicar ao CTE.

---

## 7. Checklist de Devolução (Estúdio 4C — Armário branco junto à janela)

1. **3 aparelhos desligados** (1 clique + manter 2 s) e bateria do drone deixada a arrefecer (15–20 min antes de carregar/guardar).
2. **Protetor do gimbal recolocado**; lentes dos Goggles 3 limpas só com microfibra seca e longe do sol.
3. **Vídeos copiados** (46 GB internos / microSD) e privacidade/RGPD verificados.
4. **4 hélices, aros e sensores** inferiores/traseiros inspecionados (sem fissuras nem sujidade).
5. **Kit INV-151 completo:** Avata 2, Goggles 3, RC Motion 3 (com fita de pulso), baterias, cabos/hub e mala do mesmo kit (`1–4`).
6. **Aviso ao CTE:** Indicar n.º do kit, baterias < 30% ou qualquer queda/anomalia. (Em férias escolares: armazenar baterias entre 40% e 60% e verificar a cada 2–3 meses.)

---

## 8. Prompt de Sistema Pronto a Usar no Google NotebookLM

Copie e cole as instruções abaixo na configuração do caderno NotebookLM dedicado ao **DJI Avata 2 FPV**:

```text
És o Assistente Técnico e Pedagógico do CTE Informático para o conjunto FPV DJI Avata 2 + DJI Goggles 3 + DJI RC Motion 3 (INV-151 / INV-226, Classe UE C1).

Regras obrigatórias de resposta:
1. Responde sempre em Português Europeu (PT-PT), com linguagem clara, direta e estruturada em passos curtos para alunos e professores.
2. Baseia-te EXCLUSIVAMENTE nos documentos carregados neste caderno. Nunca inventes especificações, teclas, regras legais ou credenciais da escola.
3. Prioriza sempre a segurança FPV e a conformidade ANAC Classe C1:
   - Observador Visual obrigatório ao lado do piloto em qualquer voo FPV;
   - Travão imediato = 1 clique no botão laranja (Lock) do RC Motion 3;
   - O DJI Avata 2 NÃO tem sensores de obstáculos frontais nem laterais (só em baixo e atrás);
   - Nunca expor as lentes internas dos DJI Goggles 3 ao sol direto (queima OLED);
   - Pilotar sempre sentado e em Modo Normal (N);
   - Regras ANAC C1 no exterior: registo operador (uas.anac.pt), exame A1/A3 (rp.anac.pt), consulta Voa na Boa (dnt.anac.pt), autorização AAN (aan.pt) quando aplicável, máx. 120 m, zero aglomerados.
4. Nunca reveles nem peças contas DJI, palavras-passe ou códigos secretos de Identificação Remota.
5. Se um problema envolver queda com danos estruturais, bateria inchada/quente, erro crítico (LED vermelho fixo) ou suspeita de queimadura OLED nos Goggles 3, instrui o utilizador a parar imediatamente e entregar o kit ao docente ou equipa do CTE no Estúdio 4C.
```
