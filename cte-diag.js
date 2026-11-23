/**
 * Auxiliar partilhado de diagnóstico para os 7 equipamentos do CTE:
 * 1) Injeta a pré-visualização animada do padrão do LED no topo de #ledResult.
 * 2) Suporta links diretos a partir da pesquisa global (?led=<chave> ou ?sym=<chave>).
 */
(function() {
  var ledRes = document.getElementById("ledResult");
  var symRes = document.getElementById("symResult");
  var ledBtns = Array.prototype.slice.call(document.querySelectorAll("#ledButtons .led-btn"));
  var symBtns = Array.prototype.slice.call(document.querySelectorAll("#symButtons .sym-btn"));

  function extractLedPatternClass(btn) {
    if (!btn) return "";
    var orb = btn.querySelector(".led-orb");
    if (!orb) return "";
    var classes = (orb.className || "").split(/\s+/);
    for (var i = 0; i < classes.length; i++) {
      if (classes[i].indexOf("led-pat-") === 0) return classes[i];
    }
    return "";
  }

  function injectLedPreview(btn) {
    if (!ledRes || !btn) return;
    var patClass = extractLedPatternClass(btn);
    if (!patClass) return;

    var existing = ledRes.querySelector(".led-preview-bar");
    if (existing && existing.parentNode) existing.parentNode.removeChild(existing);

    var desc = btn.getAttribute("data-led-desc") || (btn.textContent || "").trim();
    var bar = document.createElement("div");
    bar.className = "led-preview-bar";

    var housing = document.createElement("span");
    housing.className = "led-housing";
    housing.setAttribute("aria-hidden", "true");

    var orb = document.createElement("span");
    orb.className = "led-orb led-orb-lg " + patClass;
    housing.appendChild(orb);

    var meta = document.createElement("span");
    meta.className = "led-preview-meta";

    var label = document.createElement("span");
    label.className = "led-preview-label";
    label.textContent = "Padrão do LED:";

    var descEl = document.createElement("span");
    descEl.className = "led-pattern-desc";
    descEl.textContent = desc;

    meta.appendChild(label);
    meta.appendChild(descEl);
    bar.appendChild(housing);
    bar.appendChild(meta);

    ledRes.insertBefore(bar, ledRes.firstChild);
  }

  ledBtns.forEach(function(btn) {
    btn.addEventListener("click", function() {
      injectLedPreview(btn);
    });
  });

  // Barra fixa de atalhos rápidos sob o cabeçalho (Começar, Diagnóstico, Carta, Documentos, Devolver)
  function injectJumpBar() {
    if (document.querySelector(".cte-jump-bar")) return;
    var hero = document.querySelector("header.hero");
    if (!hero || !hero.parentNode) return;

    var quizAnchor = document.querySelector('a[href*="Quiz_Habilitacao.html"]');
    var links = [
      { href: "#percurso", label: "Começar", cls: "" },
      { href: "#diagnostico", label: "Diagnóstico", cls: "is-diag" }
    ];
    if (quizAnchor) {
      links.push({ href: quizAnchor.getAttribute("href"), label: "Carta", cls: "is-quiz" });
    }
    if (document.getElementById("documentos")) {
      links.push({ href: "#documentos", label: "Documentos", cls: "" });
    }
    if (document.getElementById("devolucao")) {
      links.push({ href: "#devolucao", label: "Devolver", cls: "" });
    }

    var nav = document.createElement("nav");
    nav.className = "cte-jump-bar";
    nav.setAttribute("aria-label", "Atalhos desta página");

    var inner = document.createElement("div");
    inner.className = "cte-jump-inner";

    links.forEach(function(item) {
      var a = document.createElement("a");
      a.className = "cte-jump-link" + (item.cls ? " " + item.cls : "");
      a.href = item.href;
      a.textContent = item.label;
      inner.appendChild(a);
    });

    nav.appendChild(inner);
    hero.parentNode.insertBefore(nav, hero.nextSibling);
  }

  injectJumpBar();

  // Injetar pré-visualização no LED ativo inicial
  var initialActive = document.querySelector("#ledButtons .led-btn.active") || ledBtns[0];
  if (initialActive) {
    injectLedPreview(initialActive);
  }

  // Abertura direta por parâmetro URL (?led=... ou ?sym=...) vindo da pesquisa global
  function parseQueryParam(name) {
    try {
      if (typeof URLSearchParams === "function") {
        return new URLSearchParams(window.location.search).get(name) || "";
      }
    } catch (e) {}
    var m = new RegExp("[?&]" + name + "=([^&#]+)").exec(window.location.search || "");
    return m ? decodeURIComponent(m[1].replace(/\+/g, " ")) : "";
  }

  function highlightAndScroll(panel) {
    if (!panel) return;
    var prefersReduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var diagSec = document.getElementById("diagnostico") || panel;
    try {
      diagSec.scrollIntoView({ behavior: prefersReduced ? "auto" : "smooth", block: "start" });
    } catch (e) {
      diagSec.scrollIntoView();
    }
    panel.classList.remove("diag-highlight");
    void panel.offsetWidth;
    panel.classList.add("diag-highlight");
  }

  var ledParam = parseQueryParam("led");
  var symParam = parseQueryParam("sym");

  if (ledParam && ledBtns.length) {
    var targetLed = ledBtns.filter(function(b) { return b.getAttribute("data-led") === ledParam; })[0];
    if (targetLed) {
      targetLed.click();
      highlightAndScroll(ledRes);
    }
  } else if (symParam && symBtns.length) {
    var targetSym = symBtns.filter(function(b) { return b.getAttribute("data-sym") === symParam; })[0];
    if (targetSym) {
      targetSym.click();
      highlightAndScroll(symRes);
    }
  }
})();
