/**
 * Configuração central do Portal de Ajuda CTE Informático (Escolas de Mangualde).
 *
 * Edite APENAS este ficheiro para atualizar contactos, formulários de requisição/devolução
 * e ligações NotebookLM em todo o portal (página inicial, Ajuda IA e páginas dos 9 equipamentos).
 */
window.CTE_CONFIG = {
  // 1. Contacto global do CTE (exibido no rodapé e no diagnóstico quando preenchido)
  contactoCTE: {
    nome: "",     // ex.: "Equipa CTE Informático"
    email: "",    // ex.: "cte@escolasdemangualde.pt"
    sala: "",     // ex.: "Estúdio 4C / Oficinas CTE"
    horario: ""   // ex.: "2.ª a 6.ª, 09:00–17:00"
  },

  // 2. Formulários globais (usados por omissão em todos os equipamentos)
  urlRequisicao: "",        // URL do formulário de requisição de equipamento
  urlRegistoDevolucao: "",  // URL do formulário de registo de devolução (pode ser o mesmo)

  // 3. Validade da checklist de devolução no navegador (em horas)
  checklistValidadeHoras: 4,

  // 4. Ligações NotebookLM (Ajuda IA) por equipamento
  notebooks: {
    nao: "https://notebook.google.com/notebook/452e2b41-31ec-4870-af6f-6f955c408fa5/preview",
    avata2: "https://notebook.google.com/notebook/7e02c760-40c7-4cf1-a673-5e48e83a7505/preview",
    quest3: "https://notebook.google.com/notebook/33afbc15-9471-4332-996d-c35ea62004d6/preview",
    robomaster: "https://notebook.google.com/notebook/e3067140-32a5-4401-bc80-1ca6734cd525/preview",
    pocket2: "https://notebook.google.com/notebook/f520d382-dd9d-4cdb-a1f6-e05ca99b6f42/preview",
    einstar: "",    // colar aqui o link do NotebookLM quando estiver criado
    tuxedo: "",     // colar aqui o link do NotebookLM quando estiver criado
    cricut: "",     // colar aqui o link do NotebookLM quando estiver criado
    activpanel: ""  // colar aqui o link do NotebookLM quando estiver criado
  },

  // 5. (Opcional) Substituições específicas por equipamento.
  // Deixe vazio ("") para herdar automaticamente os URLs globais definidos acima.
  equipamentos: {
    nao:        { urlRequisicao: "", urlRegistoDevolucao: "" },
    avata2:     { urlRequisicao: "", urlRegistoDevolucao: "" },
    quest3:     { urlRequisicao: "", urlRegistoDevolucao: "" },
    robomaster: { urlRequisicao: "", urlRegistoDevolucao: "" },
    pocket2:    { urlRequisicao: "", urlRegistoDevolucao: "" },
    einstar:    { urlRequisicao: "", urlRegistoDevolucao: "" },
    tuxedo:     { urlRequisicao: "", urlRegistoDevolucao: "" },
    cricut:     { urlRequisicao: "", urlRegistoDevolucao: "" },
    activpanel: { urlRequisicao: "", urlRegistoDevolucao: "" }
  },

  /**
   * Devolve a configuração efetiva para a página de um equipamento.
   * @param {string} key - Chave do equipamento (nao, avata2, quest3, robomaster, pocket2, einstar, tuxedo, cricut, activpanel)
   * @param {object} [fallback] - Valores de salvaguarda caso algum campo não exista
   */
  getEquipConfig: function(key, fallback) {
    var base = fallback || {};
    var eq = (this.equipamentos && this.equipamentos[key]) || {};
    var hasNb = !!(this.notebooks && Object.prototype.hasOwnProperty.call(this.notebooks, key));
    var c = this.contactoCTE || base.contactoCTE || {};
    return {
      contactoCTE: {
        nome: c.nome || "",
        email: c.email || "",
        sala: c.sala || "",
        horario: c.horario || ""
      },
      urlRequisicao: eq.urlRequisicao || this.urlRequisicao || base.urlRequisicao || "",
      urlRegistoDevolucao: eq.urlRegistoDevolucao || this.urlRegistoDevolucao || base.urlRegistoDevolucao || "",
      urlNotebookLM: hasNb ? (this.notebooks[key] || "") : (base.urlNotebookLM || ""),
      checklistValidadeHoras: this.checklistValidadeHoras || base.checklistValidadeHoras || 4
    };
  }
};
