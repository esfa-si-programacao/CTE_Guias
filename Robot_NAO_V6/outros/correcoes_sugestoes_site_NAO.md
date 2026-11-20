# Site de ajuda do Robô NAO V6 — correções e melhorias a implementar

> **Site:** https://aem-cte-ajuda.netlify.app/ (portal) · https://aem-cte-ajuda.netlify.app/robot_nao_v6/ (página do NAO)
> **Público:** professores e alunos que requisitam o robô NAO V6 (INV-217) ao CTE Informático, para aulas e projetos.
> **Objetivo:** que o site seja o mais útil, simples, pedagógico, fácil de usar e atrativo possível para ajudar a usar o robô de forma eficaz e eficiente.
> **Análise feita em:** 20/11/2026, sobre a versão publicada.

---

## 0. Instruções para o agente (ler primeiro)

1. **Tecnologia:** site estático (HTML + CSS + JS simples), alojado na Netlify. **Não** introduzir frameworks, bundlers nem dependências externas. Cada página continua a ser um ficheiro HTML autónomo.
2. **Língua:** português europeu (PT-PT). Tratamento consistente em todo o site.
3. **Identidade visual:** manter a paleta atual (variáveis CSS já existentes):
   ```css
   --dark:#1F2A36; --dark2:#2C3B4B; --acc:#E8711C; --acc-soft:#FDF0E6;
   --teal:#1E7E8C; --teal-soft:#E6F4F6; --blue:#1D63B8; --blue-soft:#EBF3FC;
   --red:#C0392B; --red-soft:#FBE9E7; --green:#1E8449; --green-soft:#E8F6EF;
   --purple:#6C3483; --purple-soft:#F4ECF7; --amber:#B9770E; --amber-soft:#FEF9E7;
   --light:#F3F6F9; --line:#D5DCE3; --grey:#5B6672; --text:#1F2A36; --bg:#EEF2F6;
   ```
   Fonte: `system-ui, -apple-system, "Segoe UI", Calibri, Roboto, Arial, sans-serif`.
4. **Não inventar factos técnicos sobre o NAO.** Usar apenas o conteúdo que já existe no site, ou o que está escrito neste documento. Se algo tiver de ser confirmado, deixar um comentário `<!-- CONFIRMAR: ... -->` e não publicar o texto como facto.
5. **Não apagar documentos** (PDF, DOCX, PPTX, MP4, PNG). A reorganização muda a forma como são apresentados, não os ficheiros.
6. **Manter as âncoras existentes**, que são usadas noutros sítios:
   - `nao_v6_manual_utilizador`: `#s1` a `#s9`, `#s8-python`, `#s8-inter`, `#s9-1`, `#s9-2`
   - `nao_v6_manual_tecnico`: `#t1` a `#t7`, `#tsFilter`, `#tsTable`
7. **Manter os dados do diagnóstico** (`LED_INFO` e `SYM_INFO` em `robot_nao_v6/index.html`). O conteúdo está bom; muda só a apresentação (ver R4).
8. **Testar sempre em dois tamanhos:** telemóvel 375×812 e portátil 1366×768.
9. Trabalhar pela ordem das fases: **Fase 1** (correções), depois **Fase 2** (reorganização da página do NAO), depois **Fase 3** (melhorias que precisam de materiais do professor).
10. Valores que só o professor sabe (contactos, endereços de formulários) vão para um **bloco `CONFIG`** no topo do script (ver R1). Se um valor estiver vazio, o elemento correspondente fica escondido e não aparece um link partido.

---

## 1. Diagnóstico (resumo)

**O que está muito bem e deve manter-se:**
- A entrada por intenção ("Vou usar pela 1.ª vez", "Algo não está a funcionar").
- O diagnóstico interativo por cor do LED do peito e por sintoma (a melhor peça do site).
- A Carta de Condução (quiz), a checklist de devolução, os mini-projetos com nível e duração, e o vídeo de 1 minuto em formato vertical.
- O conteúdo adaptado ao contexto da escola: Wi-Fi escolar, plano B por Ethernet, robô único, desenvolver no virtual antes do real.

**Problema principal:** a página do NAO está construída como **repositório de ficheiros**, quando o utilizador chega com uma pergunta concreta ("como começo?", "porque é que não liga?").
- No telemóvel tem cerca de 10 000 px de altura (≈ 12 ecrãs). Num portátil, cerca de 4 560 px (≈ 6 ecrãs).
- A biblioteca tem **13 cartões para cerca de 5 conteúdos**: o Guia de Início Rápido existe em 4 versões, o vídeo e a IA aparecem 2 vezes cada, e os manuais aparecem em versão web e Word.
- No telemóvel, o vídeo só aparece no 8.º ecrã e a checklist de devolução no 9.º.
- No telemóvel, o topo (dados técnicos) ocupa quase todo o primeiro ecrã antes do primeiro botão útil. "INV-217" aparece 4 vezes.
- Não existe nenhuma fotografia nem captura de ecrã: há 0 imagens na página do NAO, nos dois manuais e no quiz, apenas ilustrações SVG.
- A página principal do NAO não tem nenhum contacto do CTE.

---

## FASE 1 — Correções (erros encontrados)

### C1. Ligação partida: documento-fonte do NotebookLM
- **Ficheiro:** `robot_nao_v6/index.html`
- **Problema:** `NAO_V6_Base_Conhecimento_NotebookLM.md` devolve **404**: o ficheiro não está publicado.
- **Fazer:** confirmar se o ficheiro existe na pasta `robot_nao_v6/`. Se existir, incluí-lo na publicação. Se não existir, retirar o cartão ou a linha correspondente.
- **Aceitação:** a ligação devolve 200, ou deixa de existir.

### C2. Ligação errada: guia oficial do utilizador NAO6
- **Ficheiro:** `robot_nao_v6/index.html`, secção "Ajuda Extra"
- **Problema:** `https://doc.aldebaran.com/2-8/nao_user/index.html` não existe e redireciona para o índice geral da documentação SoftBank (em `http`).
- **Fazer:** substituir por `https://doc.aldebaran.com/2-8/family/nao_user_guide/index.html`.
- **Acrescentar** a página oficial dos usos do botão do peito: `https://doc.aldebaran.com/2-8/family/nao_user_guide/chest_button_usages.html`, com o título "Botão do peito — o que faz cada toque (oficial)".
- **Aceitação:** as duas ligações abrem a página certa em `https`.

### C3. Ligação desadequada: canal RoboPhil
- **Ficheiro:** `robot_nao_v6/index.html`, secção "Ajuda Extra"
- **Problema:** as playlists de `https://www.youtube.com/@RoboPhil/playlists` são sobre exoesqueletos, notícias de robótica e feiras (por exemplo "Robot News", "Laevo Exoskeleton", "IREX 2015"). Não há tutoriais de NAO nem de Choregraphe.
- **Fazer:** retirar este cartão. Opcionalmente, pôr no lugar os tutoriais oficiais do Choregraphe, **só se** `https://doc.aldebaran.com/2-8/software/choregraphe/tutos/index.html` abrir corretamente (não foi possível confirmar).
- **Ligações confirmadas que ficam:** Choregraphe 2.8 (`https://doc.aldebaran.com/2-8/software/choregraphe/index.html`), Python SDK (`https://doc.aldebaran.com/2-8/dev/python/index.html`) e RoboCup SPL (`https://spl.robocup.org/`).

### C4. O quiz "Carta de Condução" pode ser adivinhado
- **Ficheiro:** `robot_nao_v6/nao_v6_quiz_habilitacao.html`
- **Problema:** nas 8 perguntas, a resposta certa é **sempre a opção mais comprida**, e a ordem das perguntas e das opções nunca é baralhada. Um aluno tira 8/8 escolhendo sempre a opção mais longa, e a Carta perde o valor.
- **Fazer:**
  1. Substituir o array `QUESTIONS` pelo **banco de 16 perguntas do Anexo A**: opções com tamanhos equilibrados e a certa nem sempre a mais longa.
  2. Em cada tentativa, **sortear 8 perguntas**: as **5 marcadas `critica: true`** entram sempre, mais 3 sorteadas entre as restantes 11.
  3. **Baralhar a ordem das perguntas e das opções** (Fisher–Yates). Guardar o índice da opção certa *depois* de baralhar.
  4. **Critério de aprovação:** acertar **todas as perguntas críticas** e ter **pelo menos 7/8** no total. Se falhar uma crítica, mostrar "Não aprovado: reveja a regra de segurança X" com a explicação, e o botão "Tentar de novo" (que sorteia novas perguntas).
  5. **Cartão de habilitação:** manter os campos Nome e Turma, a data e o "Visto do Professor". Os campos Nome e Turma passam a ser **obrigatórios** antes de imprimir, com mensagem de erro junto ao campo se estiverem vazios. Acrescentar um **código de verificação** curto (6 caracteres, por exemplo um hash simples de `nome + turma + data`, em maiúsculas), para o professor ou o CTE poderem pedir esse código na requisição.
  6. Manter as explicações imediatas depois de cada resposta (já existem e são boas).
- **Aceitação:** em 5 tentativas seguidas, a ordem das perguntas e das opções muda. A opção certa não é sistematicamente a mais longa. Falhar uma pergunta crítica impede a aprovação.

### C5. A checklist de devolução fica gravada sem prazo
- **Ficheiro:** `robot_nao_v6/index.html` (chave `localStorage` `nao-v6-hub-checklist`)
- **Problema:** as marcações ficam guardadas no browser para sempre. Num PC partilhado, o grupo seguinte encontra os itens já marcados.
- **Fazer:**
  1. Guardar também a hora (`{ itens: {...}, ts: Date.now() }`). Ao abrir a página, se tiverem passado mais de `CONFIG.checklistValidadeHoras` (4 h por defeito), limpar automaticamente.
  2. Quando os 6 itens estiverem marcados, mostrar a mensagem "Tudo pronto para devolver" e o botão **"Registar devolução"**, que abre `CONFIG.urlRegistoDevolucao` (formulário de requisições do CTE) num novo separador. Se o URL estiver vazio, o botão não aparece.
- **Aceitação:** marcações com mais de 4 h desaparecem. O botão só aparece com os 6 itens marcados e o URL definido.

### C6. O assistente IA exige sessão Google
- **Ficheiro:** `robot_nao_v6/index.html`
- **Problema:** o link do NotebookLM (`https://notebook.google.com/notebook/452e2b41-31ec-4870-af6f-6f955c408fa5/preview`) redireciona para o início de sessão Google. Quem não tiver sessão iniciada fica sem saber o que fazer.
- **Fazer:** acrescentar no cartão e no botão a nota "Requer conta Google da escola". Por baixo, pôr a alternativa: "Sem conta? Use o diagnóstico rápido" (link para `#diagnostico`).
- **Nota para o professor (não é tarefa do agente):** testar o acesso com uma conta de aluno da escola, porque pode depender das definições do Google Workspace.

### C7. Contraste insuficiente
- **Ficheiros:** `robot_nao_v6/index.html` (e as outras páginas do NAO, se usarem as mesmas cores)
- **Problema:**
  - os links de ação dos cartões ("Abrir →", "Ver vídeo →", "Fazer Quiz →", "Transferir →") estão em `#E8711C` com 12,5 px sobre `#FAFBFD`, com contraste **≈ 3:1**;
  - as etiquetas pequenas (11,5 px) em teal e verde ficam em ≈ 4,2:1.
  O mínimo WCAG AA é 4,5:1.
- **Fazer:**
  - criar `--acc-text:#B4530F` (≈ 4,8:1 sobre branco) e usá-la em **texto** laranja; manter `--acc` para fundos e botões com texto branco;
  - criar `--teal-text:#166874` e `--green-text:#17693A` para as etiquetas pequenas;
  - aumentar os links de ação para pelo menos 14 px.
- **Aceitação:** todo o texto tem contraste de pelo menos 4,5:1 (verificar com as ferramentas de programador do browser).

### C8. O selo "Powered by Netlify" tapa conteúdo
- **Problema:** no telemóvel, o selo flutuante no canto inferior direito tapava um botão do diagnóstico ("Cai ao andar") e o link "Ver vídeo".
- **Fazer:** acrescentar `padding-bottom: 96px` ao `body` (ou ao rodapé) em todas as páginas. Colocar o botão flutuante de ajuda (R6) no canto **inferior esquerdo**, para não colidir com o selo.

### C9. Imagem demasiado pesada
- **Ficheiro:** `robot_nao_v6/Guião_Rápido_do_Robo_Humanoide.png` (**4,3 MB**)
- **Fazer:** criar uma versão para ecrã (`.webp` ou `.jpg`, ≤ 500 KB, largura até 1600 px) e usá-la em "Ver imagem". Manter o PNG original como "Transferir para imprimir".

### C10. Nomes inconsistentes
- **Problema:** "Robot" e "Robô" alternam. O mesmo guia aparece como "Guia de Início Rápido", "Guia de Iniciação Rápida" e "Guião Rápido".
- **Fazer:** usar **"Robô"** no texto corrido (o nome comercial "NAO V6" mantém-se) e **"Guia de Início Rápido"** em todo o lado (títulos, botões, `<title>`, legendas). O nome dos ficheiros não muda.

### C11. Favicon e descrição da página
- **Fazer:** em todas as páginas do NAO, acrescentar:
  - um favicon (SVG simples de robô, inline em data URI);
  - `<meta name="description" content="Ajuda rápida para usar o robô NAO V6 do CTE: arranque, programação no Choregraphe, diagnóstico de problemas e devolução.">`;
  - as tags Open Graph (`og:title`, `og:description`), para a partilha no Classroom ficar reconhecível.

### C12. Vídeo sem capa
- **Ficheiro:** `robot_nao_v6/index.html`
- **Fazer:** em `<video>`, usar `src="Como_Ligar_o_Robo_NAO_e_Descobrir_o_Seu_IP.mp4#t=0.5"` para mostrar uma imagem real em vez de um rectângulo vazio. O vídeo é vertical (720×1280), por isso limitar a altura (`max-height: 480px; width: auto`) e centrá-lo.
- **Opcional (Fase 3):** legendas `.vtt` (ver P4).

### C13. Afirmação a corrigir no manual do utilizador
- **Ficheiro:** `robot_nao_v6/nao_v6_manual_utilizador.html`, secção `#s8`
- **Problema:** o texto diz que **todos** os 5 mini-projetos podem ser desenvolvidos primeiro no Robô Virtual. Os projetos 2 (sensores táteis da cabeça) e 4 (reconhecimento de voz e deteção de rosto) dependem de sensores, microfones e câmaras que o robô virtual do Choregraphe, tanto quanto se sabe, não simula.
- **Fazer:**
  - mudar a frase para "Todos podem ser **construídos** no Robô Virtual; os projetos 2 e 4 só podem ser **testados** no NAO físico.";
  - acrescentar uma etiqueta "Requer NAO físico para testar" nos projetos 2 e 4;
  - deixar `<!-- CONFIRMAR: limitações do robô virtual no Choregraphe 2.8 -->` para o professor validar.
- Aplicar a mesma correção no `NAO_V6_Manual_Utilizador.docx`, se for mantido sincronizado (tarefa manual do professor).

### C14. Portal geral: etiquetas internas e filtros
- **Ficheiro:** `index.html` (raiz)
- **Problema:** os nomes de pastas aparecem como etiquetas nos cartões (`Robot_NAO_V6/`, `DJI_Avata_Drone/`, `Meta_Quest_3_VR/`). Com só 3 equipamentos, os filtros por categoria acrescentam ruído.
- **Fazer:**
  - retirar as etiquetas com nomes de pastas;
  - mostrar os filtros só quando houver 6 ou mais equipamentos (lógica em JS: `if (cards.length < 6) filtros.hidden = true`).

---

## FASE 2 — Reorganizar a página do NAO (`robot_nao_v6/index.html`)

### R1. Bloco de configuração
No início do `<script>`:
```js
const CONFIG = {
  contactoCTE: { nome: "", email: "", sala: "", horario: "" }, // preencher
  urlRequisicao: "",          // formulário de requisição do NAO
  urlRegistoDevolucao: "",    // formulário de devolução (pode ser o mesmo)
  checklistValidadeHoras: 4
};
```
Cada elemento que depende de um destes valores fica escondido quando o valor está vazio.

### R2. Nova estrutura, por ordem

```
┌────────────────────────────────────────────────────────────┐
│ ← Portal CTE                                               │
├────────────────────────────────────────────────────────────┤
│ [FOTO/GIF do NAO]  Pôr o NAO a funcionar na tua aula        │
│                    Do primeiro arranque à devolução,        │
│                    em 5 passos.                             │
│                    [ Começar aqui ]  [ Algo não funciona? ] │
├────────────────────────────────────────────────────────────┤
│ O TEU PERCURSO                                             │
│ ① Ver vídeo → ② Carta → ③ Virtual → ④ NAO real → ⑤ Devolver │
├────────────────────────────────────────────────────────────┤
│ PRECISO DE…  [Algo não funciona] [Ideias de projetos] [IA] │
├────────────────────────────────────────────────────────────┤
│ DIAGNÓSTICO RÁPIDO (LED do peito · sintoma) + contacto CTE │
├────────────────────────────────────────────────────────────┤
│ DOCUMENTOS (5 linhas, formatos como links pequenos)        │
├────────────────────────────────────────────────────────────┤
│ CHECKLIST DE DEVOLUÇÃO (6 itens) + Registar devolução      │
├────────────────────────────────────────────────────────────┤
│ ▸ Para professores e equipa CTE   (recolhido)              │
│ ▸ Ficha do equipamento            (recolhido)              │
│ Saber mais (ligações oficiais)                             │
│ Rodapé: contacto CTE · voltar ao portal                    │
└────────────────────────────────────────────────────────────┘
[🛟 Ajuda]  ← botão flutuante, canto inferior esquerdo
```

### R3. Detalhe de cada secção

**3.1 Topo (hero)**
- Título: "Pôr o NAO a funcionar na tua aula". Subtítulo: "Do primeiro arranque à devolução, em 5 passos."
- Imagem: `<img src="nao_v6_foto.jpg" alt="Robô NAO V6 do CTE">`. Se a foto não existir (`onerror`), mostrar a ilustração SVG atual do robô. A imagem tem de aparecer **também no telemóvel**: hoje a ilustração fica escondida em ecrãs pequenos.
- Botão principal (só um, cheio): **"Começar aqui"** → `#percurso`. Botão secundário (contorno): **"Algo não funciona?"** → `#diagnostico`.
- **Retirar do topo** as caixas Idioma, Rede, Software e Mala e as repetições de INV-217 e H25600. Passam para a "Ficha do equipamento" (3.8).
- **Aceitação:** a 375×812, os dois botões ficam visíveis sem fazer scroll.

**3.2 `#percurso` — 5 passos**
Cartões numerados, em linha no portátil e em coluna no telemóvel:

| Passo | Título | Texto curto | Ação |
|---|---|---|---|
| 1 | Ver o vídeo | Ligar o NAO e descobrir o IP (1 min) | vídeo **embutido aqui** (C12) |
| 2 | Tirar a Carta de Condução | 8 perguntas de segurança, com cartão para imprimir | `nao_v6_quiz_habilitacao.html` |
| 3 | Programar no Robô Virtual | Instalar o Choregraphe 2.8 e testar sem o robô | `nao_v6_manual_utilizador.html#s5` (instalar) · `#s6` (virtual) |
| 4 | Testar no NAO real | Requisitar, ligar por Wi-Fi ou Ethernet e correr o programa | `CONFIG.urlRequisicao` (se definido) · `nao_v6_manual_utilizador.html#s7` · Guia de Início Rápido (infográfico) |
| 5 | Devolver | 6 verificações antes de entregar | `#devolucao` |

- A secção do vídeo que hoje está separada deixa de existir: o vídeo passa para o passo 1.
- A frase "faça o Quiz antes de mexer no robô" deixa de estar escondida e passa a ser o passo 2.

**3.3 "Preciso de…" — 3 atalhos**
- **Algo não funciona** → `#diagnostico`
- **Ideias de projetos** → `nao_v6_manual_utilizador.html#s8` (passa para `nao_v6_projetos.html` quando P2 existir)
- **Perguntar à IA** → NotebookLM, com a nota "Requer conta Google da escola" (C6)

A IA deixa de ter o banner grande e o cartão duplicado na biblioteca: fica só este atalho.

**3.4 `#diagnostico`**
- Manter os botões de LED e de sintoma e os dados `LED_INFO` e `SYM_INFO` **sem alterar o texto**.
- Botões de LED e sintoma: acrescentar `aria-pressed="true|false"` e `type="button"`.
- No fim de cada painel de resposta, acrescentar: **"Não resolveu?"** → "Veja a tabela completa (10 casos)" (`nao_v6_manual_tecnico.html#t5`) e "Contacte o CTE: {nome} · {email} · {sala}" (de `CONFIG.contactoCTE`; esconder se estiver vazio).

**3.5 `#documentos` — de 13 cartões para 5 linhas**
Uma linha por conteúdo; os formatos aparecem como links pequenos à direita:

| Conteúdo | Formatos (links) |
|---|---|
| Guia de Início Rápido | Ver online (`nao_v6_infografico_inicio_rapido`) · Imagem (versão leve, C9) · PDF · Word |
| Manual do utilizador e programação | Ver online (`nao_v6_manual_utilizador`) · Word |
| Apresentação para a 1.ª aula (10 diapositivos) | PowerPoint |
| Vídeo: ligar o NAO e descobrir o IP | Transferir MP4 |
| Carta de Condução | Fazer o quiz |

Cada link de formato indica o tipo e, nas transferências, o tamanho aproximado (por exemplo "PDF", "Word", "MP4 · 5,7 MB").

**3.6 `#devolucao` — checklist**
- Os mesmos 6 itens, com o comportamento de C5 (validade de 4 h e "Registar devolução").
- Manter "Limpar marcações".

**3.7 Para professores e equipa CTE (`<details>` recolhido)**
- Manual técnico e manutenção: Ver online · Word
- Documento-fonte e prompts para o NotebookLM (.md), se C1 o mantiver
- Ideias interdisciplinares: `nao_v6_manual_utilizador.html#s8-inter`

**3.8 Ficha do equipamento (`<details>` recolhido)**
INV-217 · Oficinas · unidade única · modelo H25600 · NAOqi 2.8 · idioma Português · rede Wi-Fi da escola ou Ethernet · software Choregraphe 2.8 + Robô Virtual · mala com 4 itens (NAO, carregador 25,2 V, cabo Ethernet RJ45, mala).

**3.9 Saber mais**
Ligações oficiais corrigidas (C2, C3), cada uma com uma linha a dizer para que serve.

**3.10 Rodapé**
Contacto do CTE (de `CONFIG`) · "← Voltar ao Portal CTE" · padding inferior (C8).

### R4. Regras de apresentação
- **Um único botão principal** (laranja cheio) por ecrã. Os restantes são secundários (contorno) ou links.
- Os botões dizem o **objetivo**, não o formato: "Começar aqui" e não "Abrir Infográfico A4 →".
- Etiquetas em maiúsculas pequenas: no máximo uma por cartão.
- **Aceitação (tamanho):** com os `<details>` fechados, a página deve ter **≤ 5 000 px** a 375 px de largura (hoje tem ~10 000) e **≤ 3 000 px** a 1366 px (hoje tem ~4 560).

### R5. Breadcrumb comum
Em todas as páginas do NAO (página principal, infográfico, manuais, quiz): `Portal CTE › Robô NAO V6 › <página>`. O quiz já tem um; usá-lo como modelo.

### R6. Botão flutuante "Ajuda" em todas as páginas do NAO
- Fixo no **canto inferior esquerdo**, redondo, com o texto "Ajuda" e um ícone de boia.
- Abre `index.html#diagnostico`; na própria página principal, faz scroll até lá.
- Tem de ter `aria-label="Algo não funciona? Abrir diagnóstico"`.

---

## FASE 3 — Melhorias que precisam de materiais do professor

> O agente prepara a estrutura (locais das imagens, nomes de ficheiros, `alt`); o professor fornece fotos, capturas e textos.

### P1. Fotografias e capturas de ecrã (maior impacto pedagógico)
Hoje não há **nenhuma** imagem real. Preparar locais para:
- `nao_v6_foto.jpg`: o NAO do CTE de corpo inteiro (topo da página principal);
- `nao_v6_botao_peito.jpg`: o botão do peito em grande plano (diagnóstico e infográfico);
- `nao_v6_tampa_ethernet.jpg`: a tampa atrás da cabeça aberta, com a porta Ethernet visível (manual `#s7-2` e diagnóstico "Sem IP");
- `nao_v6_mala.jpg`: a mala aberta com os 4 itens (checklist de devolução);
- capturas **anotadas** do Choregraphe 2.8, no manual: `chor_connect_virtual.png` (`#s6`), `chor_box_library.png` (`#s6`), `chor_antena_verde.png` e `chor_fixed_ip.png` (`#s7`), `chor_autonomous_life.png` (ícone do coração, diagnóstico "Mexe-se sozinho").
- Todas com `alt` descritivo, `loading="lazy"` e largura máxima de 1200 px (JPG ou WebP com menos de 300 KB).

### P2. Página própria para os mini-projetos (`nao_v6_projetos.html`)
Os projetos são o centro do uso em aula, mas estão na secção 8 de um manual com ~2 700 palavras. Criar uma página com um cartão por projeto:
- título, nível (Iniciante, Intermédio, Avançado), duração, objetivo ("O que vais aprender");
- passos curtos (tirados de `#s8`);
- uma imagem do diagrama final no Choregraphe (fornecida pelo professor);
- o projeto pronto a transferir (`projeto1_ola_cte.zip`…, fornecido pelo professor);
- o desafio "E se…?" para quem acaba mais cedo (o professor escreve um por projeto);
- a etiqueta "Requer NAO físico para testar" nos projetos 2 e 4 (C13).
O manual mantém a secção 8 resumida, com um link para esta página.

### P3. QR codes
Gerar QR codes (em SVG, sem serviços externos) para:
- `https://aem-cte-ajuda.netlify.app/robot_nao_v6/#percurso`, para colar na mala;
- `https://aem-cte-ajuda.netlify.app/robot_nao_v6/#diagnostico`, para pôr no infográfico plastificado (canto inferior, com a legenda "Algo não funciona? Leia este código").

### P4. Legendas do vídeo
Criar `Como_Ligar_o_Robo_NAO_e_Descobrir_o_Seu_IP.vtt` em português, a partir da transcrição fornecida pelo professor, e acrescentar `<track kind="captions" srclang="pt" label="Português" default>`. As legendas ajudam em salas com barulho e dão acessibilidade.

### P5. Ligar a Carta de Condução à requisição
Quando `CONFIG.urlRequisicao` estiver definido, o formulário de requisição deve pedir o **código de verificação** da Carta (C4.5). Esta tarefa é do lado do formulário (Google Forms ou Apps Script); o site só mostra o código de forma clara no cartão.

---

## 4. Verificação final (o agente deve confirmar tudo)

- [ ] Todas as ligações internas devolvem 200 (sem 404), incluindo as âncoras `#s5`, `#s6`, `#s7`, `#s8`, `#t5`.
- [ ] As ligações externas abrem a página certa em `https`.
- [ ] A 375×812, "Começar aqui" e "Algo não funciona?" estão visíveis sem scroll.
- [ ] Página do NAO: ≤ 5 000 px no telemóvel e ≤ 3 000 px no portátil, com os `<details>` fechados.
- [ ] O selo da Netlify não tapa nenhum botão nem link.
- [ ] Contraste ≥ 4,5:1 em todo o texto.
- [ ] Quiz: a ordem das perguntas e das opções muda entre tentativas; falhar uma pergunta crítica impede a aprovação; Nome e Turma são obrigatórios antes de imprimir.
- [ ] Checklist: limpa-se sozinha passadas 4 h; "Registar devolução" só aparece com os 6 itens marcados e o URL definido.
- [ ] Elementos dependentes de `CONFIG` ficam escondidos quando o valor está vazio (sem links partidos).
- [ ] O texto de `LED_INFO` e `SYM_INFO` não foi alterado.
- [ ] Sem erros na consola do browser.
- [ ] Lista final dos ficheiros alterados ou criados, para o professor publicar na Netlify.

---

## Anexo A — Banco de perguntas do quiz (16 perguntas)

Formato pronto para o `QUESTIONS` do quiz. `ans` é o índice (0–3) da opção certa **antes** de baralhar. As 5 perguntas com `critica: true` entram sempre no sorteio.

```json
[
  {
    "cat": "Segurança física",
    "critica": true,
    "q": "Como se deve levantar e transportar o NAO?",
    "opts": [
      "Pelos dois braços, para o manter bem equilibrado no ar.",
      "Com as duas mãos à volta do tronco, junto à cintura.",
      "Pela cabeça, que é a parte mais robusta do robô.",
      "Pelas pernas, mantendo-o virado para o chão."
    ],
    "ans": 1,
    "exp": "Segure sempre o NAO com as duas mãos à volta do tronco/cintura. Pegar pela cabeça, braços ou pernas pode danificar motores e engrenagens."
  },
  {
    "cat": "Proteção dos motores",
    "critica": true,
    "q": "Os motores estão rígidos e um braço ficou numa posição incómoda. O que deve fazer?",
    "opts": [
      "Dobrar o braço devagar até voltar ao lugar.",
      "Empurrar o ombro devagar até ouvir um pequeno estalido.",
      "Pôr o robô em descanso (Rest) e só depois mexer.",
      "Retirar a bateria com o robô ainda ligado."
    ],
    "ans": 2,
    "exp": "Nunca force uma articulação rígida. Liberte primeiro a rigidez dos motores: Rest no Choregraphe (ícone da Lua) ou 2 cliques rápidos no botão do peito."
  },
  {
    "cat": "Arranque e calibração",
    "critica": true,
    "q": "Porque não deve tocar no NAO nos cerca de 60 segundos depois de o ligar?",
    "opts": [
      "Os sensores táteis podem dar um pequeno choque.",
      "Está a calibrar o giroscópio usado no equilíbrio.",
      "A bateria ainda está a aquecer e pode desligar-se.",
      "Está a descarregar o idioma Português da Internet."
    ],
    "ans": 1,
    "exp": "Durante o arranque (até dizer 'Ognak Gnouk'), o NAO calibra a unidade inercial (giroscópio/IMU). Mexer-lhe nessa altura prejudica o equilíbrio ao andar."
  },
  {
    "cat": "Cabos",
    "critica": true,
    "q": "O Wi-Fi falhou e ligou o cabo Ethernet atrás da cabeça do NAO. Que cuidado é obrigatório?",
    "opts": [
      "Ligar também o carregador para a ligação ficar estável.",
      "Manter o robô sempre de pé para o cabo não dobrar.",
      "Não o pôr a andar enquanto o cabo estiver ligado.",
      "Desligar o Wi-Fi do computador antes de o pôr a andar."
    ],
    "ans": 2,
    "exp": "Com o cabo Ethernet (ou o carregador) ligado, faça apenas testes sem caminhada: fala, gestos, LEDs. Desligue o cabo antes de pôr o robô a andar."
  },
  {
    "cat": "Encerramento",
    "critica": true,
    "q": "Como se desliga o NAO antes de o arrumar na mala?",
    "opts": [
      "Premir o peito ~1 s e fechar logo a mala.",
      "Deixá-lo ligado em Rest dentro da mala, para arrancar mais depressa.",
      "Manter o peito premido ~8 s, que é o mais rápido e seguro.",
      "Em Crouch, premir o peito ~3 s e esperar os LEDs apagarem."
    ],
    "ans": 3,
    "exp": "Desligue em postura Crouch: mantenha o botão do peito premido ~3 s ('Gnuk Gnuk') e espere que TODOS os LEDs apaguem. Os 8 s são só para emergências."
  },
  {
    "cat": "Rede e endereço IP",
    "critica": false,
    "q": "Como descobre o endereço IP do NAO para o ligar ao Choregraphe?",
    "opts": [
      "Dando 1 clique curto no peito: o NAO diz o IP.",
      "Mantendo o botão do peito premido durante 8 s.",
      "Lendo a etiqueta dentro do compartimento da bateria.",
      "Tocando ao mesmo tempo nos sensores dos dois pés."
    ],
    "ans": 0,
    "exp": "Com o NAO ligado, 1 clique curto no botão do peito faz o robô dizer em voz alta o nome, o endereço IP e eventuais notificações."
  },
  {
    "cat": "Fluxo de trabalho",
    "critica": false,
    "q": "Só há um NAO na escola. Qual é a forma certa de trabalhar em aula?",
    "opts": [
      "Ligar todos os computadores ao NAO ao mesmo tempo.",
      "Programar só quando o robô estiver a carregar.",
      "Testar no Robô Virtual e só depois no NAO físico.",
      "Usar qualquer versão do Choregraphe, porque são iguais."
    ],
    "ans": 2,
    "exp": "O NAO V6 usa o Choregraphe 2.8. Cada grupo desenvolve e valida primeiro no Robô Virtual e só no fim transfere para o NAO físico."
  },
  {
    "cat": "Programação",
    "critica": false,
    "q": "Durante o teste, o NAO olha para os colegas e interrompe o programa. Qual é a causa provável?",
    "opts": [
      "A Vida Autónoma está ligada e deve ser pausada.",
      "O cabo Ethernet está desligado da cabeça.",
      "O idioma Português não suporta movimentos.",
      "O robô está em descanso (Rest) há demasiado tempo seguido."
    ],
    "ans": 0,
    "exp": "A Vida Autónoma (Autonomous Life) arranca ligada. No Choregraphe, clique no ícone do coração para a pausar antes de correr o programa da turma."
  },
  {
    "cat": "Superfície",
    "critica": false,
    "q": "Onde deve pôr o NAO a andar?",
    "opts": [
      "Numa alcatifa macia, para amortecer as quedas.",
      "Em cima de uma mesa grande, longe da beira.",
      "Em chão plano e firme, com cerca de 1,5 × 1,5 m livre.",
      "Em qualquer piso, desde que o Wi-Fi da sala esteja estável."
    ],
    "ans": 2,
    "exp": "Use apenas piso plano, liso e firme, com uma área livre de cerca de 1,5 × 1,5 m. Alcatifas e mesas aumentam muito o risco de queda."
  },
  {
    "cat": "Bateria",
    "critica": false,
    "q": "O LED do peito está vermelho a piscar lentamente. O que significa e o que faz?",
    "opts": [
      "Está a atualizar o sistema: não o desligue.",
      "Bateria crítica: pare, ponha em Rest e ligue o carregador.",
      "Acabou de arrancar e está pronto para trabalhar.",
      "Ligou-se ao Wi-Fi da escola com sucesso."
    ],
    "ans": 1,
    "exp": "Vermelho a piscar indica bateria crítica (abaixo de 20%). Pare o programa, ponha o robô em Rest e ligue o carregador oficial de 25,2 V."
  },
  {
    "cat": "Ligação ao Choregraphe",
    "critica": false,
    "q": "O Choregraphe não encontra o NAO na lista. Qual é o primeiro passo?",
    "opts": [
      "Reinstalar o Choregraphe numa versão mais antiga e compatível.",
      "Mudar o idioma do robô para Inglês e reiniciar.",
      "Desligar o robô com o peito premido durante 8 s.",
      "Usar 'Use fixed IP/hostname' com o IP que o NAO disse."
    ],
    "ans": 3,
    "exp": "Nas redes escolares a deteção automática falha muitas vezes. Na Antena Verde, use 'Use fixed IP/hostname' com o IP dito pelo NAO (porta 9559)."
  },
  {
    "cat": "Sobreaquecimento",
    "critica": false,
    "q": "As articulações estão quentes e perdem força. O que deve fazer?",
    "opts": [
      "Continuar a aula, mas com movimentos mais lentos.",
      "Pôr o NAO em descanso (Rest) durante 10 a 15 minutos.",
      "Desligá-lo com 8 s no peito e voltar a ligar logo.",
      "Colocá-lo junto a uma janela aberta e continuar."
    ],
    "ans": 1,
    "exp": "Em sobreaquecimento, coloque o NAO em Rest durante 10 a 15 minutos para os motores arrefecerem. Evite deixá-lo muito tempo de pé parado."
  },
  {
    "cat": "Fala",
    "critica": false,
    "q": "O programa corre, mas o NAO não fala em Português. O que falta?",
    "opts": [
      "Ligar o cabo Ethernet atrás da cabeça.",
      "Aumentar o volume do robô e o brilho dos LEDs dos olhos.",
      "Uma caixa 'Set Language' (Portuguese) no início.",
      "Pôr o robô em Crouch antes de cada frase."
    ],
    "ans": 2,
    "exp": "Acrescente a caixa 'Set Language' (Portuguese) no início do projeto. Para o reconhecimento de voz, fale de frente, a 50–100 cm, numa sala silenciosa."
  },
  {
    "cat": "Fim do programa",
    "critica": false,
    "q": "Em que posição deve terminar sempre um programa?",
    "opts": [
      "Numa postura estável: Stand ou Rest.",
      "Com os braços levantados, para se ver o fim.",
      "A meio de um passo, para retomar depois.",
      "Tanto faz, o robô corrige a posição sozinho."
    ],
    "ans": 0,
    "exp": "Termine sempre numa postura estável (Stand ou Rest). Valide isto no Robô Virtual antes de pedir o NAO físico."
  },
  {
    "cat": "Emergência",
    "critica": false,
    "q": "O NAO bloqueou totalmente e não responde a nada. O que deve fazer?",
    "opts": [
      "Retirar a bateria enquanto ainda está ligado.",
      "Dar cliques rápidos no peito até ele reagir.",
      "Deitá-lo no chão e esperar que se desbloqueie.",
      "Segurá-lo pelo tronco e premir o peito ~8 s."
    ],
    "ans": 3,
    "exp": "Segure firmemente o robô pelo tronco e mantenha o botão do peito premido cerca de 8 s até todos os LEDs apagarem. Espere 15 s, pouse-o em Crouch e volte a ligar."
  },
  {
    "cat": "Devolução",
    "critica": false,
    "q": "Na devolução, quando é obrigatório avisar o CTE?",
    "opts": [
      "Só se o robô tiver caído mais de três vezes.",
      "Se a bateria estiver abaixo de 30% ou houve anomalia.",
      "Nunca: basta deixar a mala fechada nas Oficinas.",
      "Só se a turma não tiver terminado o projeto."
    ],
    "ans": 1,
    "exp": "Avise sempre o CTE se a bateria ficar abaixo de 30% ou se houve qualquer anomalia (queda, ruído, peça solta), para o robô estar pronto para a turma seguinte."
  }
]
```

---

## Anexo B — Prompt sugerido para o Antigravity

> Lê o ficheiro `correcoes_sugestoes_site_NAO.md` na raiz deste projeto. Implementa primeiro a **Fase 1** (C1 a C14) e a seguir a **Fase 2** (R1 a R6), respeitando as instruções da secção 0: site estático, PT-PT, paleta atual, sem inventar factos técnicos, sem apagar documentos, mantendo as âncoras e o texto do diagnóstico. Para a Fase 3, prepara só a estrutura (locais das imagens, nomes de ficheiros, `alt`) e lista o que eu tenho de fornecer. Antes de alterar cada ficheiro, mostra-me o plano. No fim, percorre a lista da secção 4, diz-me o resultado de cada ponto e dá-me a lista dos ficheiros alterados ou criados, para eu publicar na Netlify.
