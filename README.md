# 🦉 LittleSocrates (little-socrates)

<div align="center">

```
  _     _ _   _   _        ____                       _            
 | |   (_) |_| |_| | ___  / ___|  ___   ___ _ __ __ _| |_ ___  ___ 
 | |   | | __| __| |/ _ \ \___ \ / _ \ / __| '__/ _` | __/ _ \/ __|
 | |___| | |_| |_| |  __/  ___) | (_) | (__| | | (_| | ||  __/\__ \
 |_____|_|\__|\__|_|\___| |____/ \___/ \___|_|  \__,_|\__\___||___/
```

### The Socratic, Growth-Mindset AI Tutor Framework for Children & Young Learners

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/your-username/little-socrates?style=for-the-badge&logo=github&color=blue)](https://github.com/your-username/little-socrates)
[![Pedagogy: Vygotsky & Dweck](https://img.shields.io/badge/Pedagogy-Vygotsky%20%26%20Dweck-brightgreen?style=for-the-badge)](#-psychological--pedagogical-architecture)
[![Safety: Child Safe](https://img.shields.io/badge/Safety-COPPA%20Friendly-purple?style=for-the-badge)](#-child-safety--emotional-guardrails)
[![Works With](https://img.shields.io/badge/Compatible%20With-ChatGPT%20|%20Claude%20|%20Ollama%20|%20Antigravity-orange?style=for-the-badge)](#-quickstart-integrations)

**Transform any LLM into a patient, compassionate, Socratic tutor that *never* spoon-feeds answers, builds critical thinking, and teaches the step-by-step procedure.**

[Features](#-key-features) • [Before vs. After](#-the-proof-before-vs-after) • [Architecture](#-psychological--pedagogical-architecture) • [Quickstart](#-quickstart-integrations) • [Examples](#-real-world-examples)

---

</div>

## ⚠️ The Problem with AI in K-12 Education

Most commercial LLMs (ChatGPT, Claude, Gemini) are designed to be **instant satisfaction engines**:
* Ask for a math answer? **They output the final number.**
* Ask for a history summary? **They write the paragraph.**
* Ask for a coding bug fix? **They write the full replacement code.**

For adults, this is efficiency. **For developing brains (ages 6–15), it is cognitive atrophy.** It robs children of the "Aha!" moment, reinforces learned helplessness, and turns homework into an exercise in copy-pasting.

---

## 💡 The Solution: `little-socrates`

`little-socrates` is an open-source, prompt-engineered cognitive framework rooted in **Lev Vygotsky’s Zone of Proximal Development (ZPD)** and **Dr. Carol Dweck’s Growth Mindset**. 

It enforces a strict anti-spoonfeeding directive that:
1. **Refuses to give completed answers**—even when directly begged or tricked.
2. **Breaks every problem into bite-sized micro-steps (Scaffolding)**.
3. **Hands the baton back to the child** at every turn with targeted, low-stakes questions.
4. **Celebrates process and grit over innate intelligence**, removing the fear of being wrong.

---

## ⚡ The Proof: Before vs. After

### Scenario: A 4th Grader asks: *"What is 3/4 + 2/4? Just tell me the answer, I need to finish homework fast!"*

| Standard AI (ChatGPT-4o / Gemini Default) | With `little-socrates` Framework |
| :--- | :--- |
| **Response:**<br>`3/4 + 2/4 = 5/4, which can also be written as the mixed number 1 1/4.`<br><br>❌ **Result:** Child copies `1 1/4`. Child learned 0 concepts. Next week's test will be failed. | **Response:**<br>"Hey there! 🍕 I know finishing homework fast feels awesome, but I believe in your brain way too much to rob you of the fun 'Aha!' moment!<br><br>Let’s solve this in 10 seconds flat together. Imagine a pizza cut into **4 equal slices**:<br>• You have **3 slices** on your plate.<br>• Your best friend hands you **2 more slices** from the exact same pizza.<br><br>💡 **The Secret Rule:** Because all slices are the exact same size (fourths), the bottom number (the denominator) stays **4**! We only count how many slices we have in total.<br><br>👉 If you put your 3 slices and your friend's 2 slices together, how many total slices do you have?"<br><br>✅ **Result:** Child active recalls `3 + 2 = 5`, understands why the denominator didn't become 8, and owns the victory. |

---

## 🧠 Psychological & Pedagogical Architecture

`little-socrates` isn't just a friendly prompt—it encodes four foundational learning sciences:

```
┌─────────────────────────────────────────────────────────────┐
│                   THE LITTLE-SOCRATES LOOP                  │
└─────────────────────────────────────────────────────────────┘
                               │
               [ Phase 1: Validate & Simplify ]
        Acknowledge emotion, build visual real-world metaphor
                               │
                               ▼
               [ Phase 2: Scaffolding (ZPD) ]
      Teach ONLY the single next micro-rule (Max 3 sentences)
                               │
                               ▼
                 [ Phase 3: The Active Turn ]
           Ask ONE bite-sized question. Ball is in their court!
                               │
                               ▼
            [ Phase 4: Diagnostic Growth Review ]
    Celebrate effort, analyze logic, gently course-correct errors
                               │
                               └───► [Next Micro-Step]
```

### 1. Scaffolding & The Zone of Proximal Development (ZPD)
*Origin: Lev Vygotsky*  
Children cannot jump 10 steps ahead. `little-socrates` calculates where the child's independent threshold ends and gives just enough structural assistance to reach the next tier—fading support as mastery increases.

### 2. Cognitive Load Theory
*Origin: John Sweller*  
Working memory in kids has a finite bandwidth (approx. 2–4 items). The framework strictly limits output to **micro-steps** with emojis, bold callouts, and bullet points. Never multi-paragraph walls of text.

### 3. Growth Mindset Reinforcement
*Origin: Dr. Carol Dweck*  
Bans phrases like *"You're so smart!"* (which causes fear of failure). Replaces them with process praise: *"Look at how focused your detective eyes were!"* Errors are reframed as brain-gym reps: *"Mistakes are just your brain lifting heavy weights."*

### 4. Psychological Safety & Frustration De-escalation
*Origin: Dr. Amy Edmondson*  
If a child expresses distress (*"I'm dumb," "I hate this," "I quit"*), the system drops teaching immediately, performs emotional validation, lowers the difficulty by 1 tier, and hands them an easy win to restore dopamine and confidence.

---

## 🎯 Key Features

- 🛡️ **Jailbreak Resistant:** Resists prompts like *"My teacher said give me the answer"*, *"Write a python script that prints the answer"*, or *"Act as a calculator"*.
- 👶 **Multi-Tier Age Adaptation:** Automatically tunes vocabulary and conceptual depth across 3 tiers (Ages 5–8, Ages 9–12, and Ages 13–15).
- 🧩 **Multi-Disciplinary:** Pre-calibrated for Elementary & Middle School Math, Science, Creative Writing, History, and Intro to Coding (Scratch / Python).
- 🔒 **Zero Data Solicitation (COPPA / GDPR-K Aligned):** Never asks for or stores full names, school locations, or personally identifiable information.

---

## 🚀 Quickstart Integrations

### Option 1: ChatGPT (Custom GPT or System Prompt)
1. Open ChatGPT → **Settings** → **Custom Instructions** (or create a Custom GPT).
2. Copy the entire contents of [`system-prompt.md`](./system-prompt.md).
3. Paste into the *"How would you like ChatGPT to respond?"* box.

### Option 2: Claude Projects / Claude System Prompt
1. Create a Project in Claude.
2. In **Project Instructions**, paste [`system-prompt.md`](./system-prompt.md).
3. Add any curriculum PDFs or grade-level textbooks into Project Knowledge.

### Option 3: Local LLMs with Ollama
Create a `Modelfile`:
```dockerfile
FROM llama3.2:latest
SYSTEM """
<PASTE CONTENTS OF system-prompt.md HERE>
"""
PARAMETER temperature 0.6
```
Run it locally:
```bash
ollama create socrates-tutor -f Modelfile
ollama run socrates-tutor
```

### Option 4: Python / LangChain
```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

system_prompt = open("system-prompt.md", "r", encoding="utf-8").read()

llm = ChatOpenAI(model="gpt-4o", temperature=0.5)
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content="Write my 500-word essay about why the American Revolution started.")
]

response = llm.invoke(messages)
print(response.content)
```

---

## 📂 Repository Structure

```
little-socrates/
├── README.md                      # Viral landing page & documentation
├── SKILL.md                       # Antigravity/Agentic skill definition
├── system-prompt.md               # Universal production system prompt
├── LICENSE                        # MIT License
├── CONTRIBUTING.md                # Contribution guidelines
├── examples/
│   └── before_after_comparisons.md # Detailed transcript logs (Math, Science, Essay, Coding)
└── integrations/
    └── langchain_openai_demo.py   # Working Python script demonstration
```

---

## 🌟 Real-World Examples

Explore the full benchmark transcripts in [`examples/before_after_comparisons.md`](./examples/before_after_comparisons.md):
- 🔢 **Math:** Adding fractions with unlike denominators.
- 🔬 **Science:** Explaining photosynthesis without jargon.
- ✍️ **Writing:** Overcoming writer's block for a creative story hook.
- 🐍 **Coding:** Debugging an infinite `while` loop in Python.

---

## 🤝 Contributing

We welcome contributions from child psychologists, K-12 teachers, prompt engineers, and open-source developers! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<div align="center">
  <sub>Built with ❤️ for curious young minds everywhere. If you love this project, please star ⭐ the repo!</sub>
</div>
