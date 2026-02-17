const startInput = document.querySelector("#start");
const endInput = document.querySelector("#end");
const startButton = document.querySelector("#start-btn");
const resetButton = document.querySelector("#reset-btn");
const errorEl = document.querySelector("#error");
const quizEl = document.querySelector("#quiz");
const summaryEl = document.querySelector("#summary");
const celebrateEl = document.querySelector("#celebrate");
const symbolToNameEl = document.querySelector("#symbol-to-name");
const nameToSymbolEl = document.querySelector("#name-to-symbol");
const tabSymbolBtn = document.querySelector("#tab-symbol");
const tabNameBtn = document.querySelector("#tab-name");
const paneSymbol = document.querySelector("#pane-symbol");
const paneName = document.querySelector("#pane-name");

const STORAGE_KEY = "elements-quiz-state";

const state = {
  start: 1,
  end: 1,
  rangeStart: 1,
  rangeEnd: 1,
  answers: {},
  started: false,
  activeTab: "symbol",
};

let elements = [];

function loadState() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return;
  try {
    const parsed = JSON.parse(raw);
    if (typeof parsed.start === "number") state.start = parsed.start;
    if (typeof parsed.end === "number") state.end = parsed.end;
    if (typeof parsed.rangeStart === "number") state.rangeStart = parsed.rangeStart;
    if (typeof parsed.rangeEnd === "number") state.rangeEnd = parsed.rangeEnd;
    if (typeof parsed.started === "boolean") state.started = parsed.started;
    if (parsed.answers && typeof parsed.answers === "object") {
      state.answers = parsed.answers;
    }
    if (typeof parsed.activeTab === "string") state.activeTab = parsed.activeTab;
  } catch (err) {
    console.warn("Failed to load saved state", err);
  }
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function setError(message) {
  errorEl.textContent = message;
}

function getSelectedElements() {
  return elements.slice(state.rangeStart - 1, state.rangeEnd);
}

function createQuestion(labelText, key, correctValue) {
  const wrapper = document.createElement("div");
  wrapper.className = "question";

  const label = document.createElement("label");
  label.textContent = labelText;

  const input = document.createElement("input");
  input.type = "text";
  input.value = state.answers[key] || "";
  input.autocomplete = "off";

  const feedback = document.createElement("span");
  feedback.className = "feedback";

  input.addEventListener("input", () => {
    state.answers[key] = input.value;
    updateSummary();
    saveState();
  });

  input.addEventListener("blur", () => {
    checkAnswer(input, feedback, correctValue);
  });

  // Clear feedback on focus so user can edit without seeing it
  input.addEventListener("focus", () => {
    feedback.textContent = "";
    feedback.className = "feedback";
  });

  wrapper.append(label, input, feedback);
  return wrapper;
}

function checkAnswer(input, feedback, correctValue) {
  const value = input.value.trim();
  if (!value) {
    feedback.textContent = "";
    feedback.className = "feedback";
    return;
  }

  if (value.toLowerCase() === correctValue.toLowerCase()) {
    feedback.textContent = "Correct";
    feedback.className = "feedback good";
    confetti(
        {
            colors: ['#0f0f0f', '#e4e2e2', '#ffd900']
        }
    );
  } else {
    feedback.textContent = `Correct answer: ${correctValue}`;
    feedback.className = "feedback bad";
  }
}

function renderQuestions() {
  const selection = getSelectedElements();
  symbolToNameEl.innerHTML = "";
  nameToSymbolEl.innerHTML = "";

  selection.forEach((element) => {
    const symbolQuestion = createQuestion(
      `What is the name for "${element.symbol}"?`,
      `name_${element.symbol}`,
      element.name
    );
    symbolToNameEl.append(symbolQuestion);

    const nameQuestion = createQuestion(
      `What is the symbol for "${element.name}"?`,
      `symbol_${element.symbol}`,
      element.symbol
    );
    nameToSymbolEl.append(nameQuestion);
  });

  quizEl.classList.remove("hidden");
  updateSummary();
}

function updateSummary() {
  if (!state.started) {
    summaryEl.textContent = "";
    celebrateEl.textContent = "";
    return;
  }

  const selection = getSelectedElements();
  let correctSymbolToName = 0;
  let correctNameToSymbol = 0;
  let answeredSymbolToName = 0;
  let answeredNameToSymbol = 0;

  selection.forEach((element) => {
    const nameKey = `name_${element.symbol}`;
    const symbolKey = `symbol_${element.symbol}`;

    const nameAnswer = (state.answers[nameKey] || "").trim();
    const symbolAnswer = (state.answers[symbolKey] || "").trim();

    if (nameAnswer) {
      answeredSymbolToName += 1;
      if (nameAnswer.toLowerCase() === element.name.toLowerCase()) {
        correctSymbolToName += 1;
      }
    }

    if (symbolAnswer) {
      answeredNameToSymbol += 1;
      if (symbolAnswer.toLowerCase() === element.symbol.toLowerCase()) {
        correctNameToSymbol += 1;
      }
    }
  });

  summaryEl.textContent =
    `Symbol -> Name: ${correctSymbolToName}/${selection.length} | ` +
    `Name -> Symbol: ${correctNameToSymbol}/${selection.length}`;

  const allAnswered =
    answeredSymbolToName === selection.length &&
    answeredNameToSymbol === selection.length;
  const allCorrect =
    correctSymbolToName === selection.length &&
    correctNameToSymbol === selection.length &&
    selection.length > 0;

  if (allAnswered && allCorrect) {
    celebrateEl.textContent = "All correct! Nice work.";
  } else {
    celebrateEl.textContent = "";
  }
}

function startStudying() {
  const startValue = Number.parseInt(startInput.value, 10);
  const endValue = Number.parseInt(endInput.value, 10);

  if (Number.isNaN(startValue) || Number.isNaN(endValue)) {
    setError("Please enter valid numbers.");
    return;
  }

  if (startValue < 1 || endValue > elements.length) {
    setError(`Range must be between 1 and ${elements.length}.`);
    return;
  }

  if (startValue > endValue) {
    setError("Start number must be less than or equal to end number.");
    return;
  }

  setError("");
  state.start = startValue;
  state.end = endValue;
  state.rangeStart = startValue;
  state.rangeEnd = endValue;
  state.answers = {};
  state.started = true;
  saveState();
  renderQuestions();
}

function resetQuiz() {
  state.start = 1;
  state.end = elements.length;
  state.rangeStart = 1;
  state.rangeEnd = elements.length;
  state.answers = {};
  state.started = false;
  state.activeTab = "symbol";
  saveState();
  quizEl.classList.add("hidden");
  summaryEl.textContent = "";
  celebrateEl.textContent = "";
  setError("");
  startInput.value = state.start;
  endInput.value = state.end;
}

function switchTab(tab) {
  state.activeTab = tab;
  saveState();

  if (tab === "symbol") {
    paneSymbol.classList.add("active");
    paneName.classList.remove("active");
    tabSymbolBtn.classList.add("active");
    tabNameBtn.classList.remove("active");
  } else {
    paneName.classList.add("active");
    paneSymbol.classList.remove("active");
    tabNameBtn.classList.add("active");
    tabSymbolBtn.classList.remove("active");
  }
}

async function init() {
  loadState();
  const response = await fetch("./data/elements.json");
  elements = await response.json();

  if (!state.end || state.end > elements.length) {
    state.end = elements.length;
    state.rangeEnd = elements.length;
  }

  startInput.value = state.start;
  endInput.value = state.end;
  startInput.max = elements.length;
  endInput.max = elements.length;

  startButton.addEventListener("click", startStudying);
  resetButton.addEventListener("click", resetQuiz);
  tabSymbolBtn.addEventListener("click", () => switchTab("symbol"));
  tabNameBtn.addEventListener("click", () => switchTab("name"));

  if (state.started) {
    renderQuestions();
    switchTab(state.activeTab);
  }
}

function setupBackToTop() {
  const backToTopBtn = document.querySelector("#back-to-top");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      backToTopBtn.classList.add("show");
    } else {
      backToTopBtn.classList.remove("show");
    }
  });

  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

init();
setupBackToTop();
