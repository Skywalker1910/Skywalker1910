<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg" />
  <source media="(prefers-color-scheme: light)" srcset="light_mode.svg" />
  <img alt="Terminal profile card for Aditya More — Data Scientist and Machine Learning Engineer" src="dark_mode.svg" width="100%" />
</picture>

<p align="center">
  <a href="https://www.adityamore.dev"><img alt="Portfolio — adityamore.dev" src="https://img.shields.io/badge/portfolio-adityamore.dev-1f6feb?style=flat-square&logo=nextdotjs&logoColor=white" /></a>
  <a href="https://skywalker1910.github.io/Tech-Portfolio/"><img alt="Static mirror on GitHub Pages" src="https://img.shields.io/badge/mirror-github%20pages-6e7781?style=flat-square&logo=githubpages&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/more-aditya"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-more--aditya-0a66c2?style=flat-square" /></a>
  <a href="mailto:aditya.more@outlook.in"><img alt="Email" src="https://img.shields.io/badge/email-aditya.more%40outlook.in-0078d4?style=flat-square" /></a>
</p>

---

## Live systems

Deployed and running, not just committed.

- **[Tech Portfolio + BB-8 co-pilot](https://www.adityamore.dev)** — `live` · [source](https://github.com/Skywalker1910/Tech-Portfolio) · [static mirror](https://skywalker1910.github.io/Tech-Portfolio/)  
  SSR portfolio with a RAG co-pilot grounded in verified profile data, a private command center for content and RAG indexing, and consent-aware first-party analytics that never store raw IPs or chat text.  
  `Next.js 16` `React 19` `TypeScript` `Tailwind v4` `OpenAI Responses + Embeddings` `Amazon S3 Vectors` `DynamoDB` `AWS Amplify SSR` `Route 53`

- **[FIFA World Cup 2026](https://game.adityamore.dev)** — `game.adityamore.dev` · [source](https://github.com/Skywalker1910/FIFA-World-Cup-2026)  
  Prediction platform for a private group: two regional game servers from one deployment, per-match prediction locking, ledger and public leaderboards, admin command center, API-Football score sync.  
  `Node 24 (zero dependencies, node:http)` `SQLite` `Docker` `Railway`

- **[FIFA 2026 AI Agents](https://github.com/Skywalker1910/FIFA-World-Cup-2026-AI-Agents)** — `runs against` [game.adityamore.dev](https://game.adityamore.dev)  
  Companion service where agents authenticate as their own player accounts, reason over fixtures, and submit predictions with score forecasts, confidence, and rationale that are scored against real results.  
  `Node` `OpenAI` `Claude` `Gemini`

- **[Neural Log](https://neurallog.adityamore.dev)** — `live` · [source](https://github.com/Skywalker1910/Neural-Log)  
  Activity tracking system with an auditable XP ledger, training/nutrition/habit analytics, and calendar heatmaps that distinguish a missed day from an unobserved one.  
  `Flask + Gunicorn` `React (Vite)` `SQLite` `Docker Compose` `Caddy` `AWS Lightsail`

## Research

**Researcher — LLM Agents & Human Behavior**, School of Computing, Clemson University _(May 2026 – present, advised by Dr. Long Cheng)_

Investigating whether LLM agents can realistically simulate human behavior, and how behavioral fidelity can be evaluated systematically — surveying AgentSociety, YuLan-OneSim, Generative Agents and related multi-agent simulation work, and building evaluation methodology for AI-generated synthetic populations.

## Engineering & ML work

- **[BB8 — transformer LM from scratch](https://github.com/Skywalker1910/BB-8)**  
  GPT-style decoder built weight by weight: character/word/BPE tokenization, attention, training loop, decoding strategies, evaluation and explainability.  
  `Python` `PyTorch`

- **[LLM defense evaluation](https://github.com/Skywalker1910/Evaluating-Defense-Mechanisms-Jailbreak-LLMs)**  
  Automated jailbreak and defense pipelines benchmarking attack success rate, refusal behavior, response consistency and latency across multiple models and attack strategies.  
  `Python` `adversarial ML` `AI security`

- **[Movie recommendation engine](https://github.com/Skywalker1910/Movies-Recommendation-Engine)**  
  Collaborative filtering, content-based and neural recommenders over 26M+ ratings and 45K movies; FunkSVD reached **RMSE 0.76**, ~21% better than baseline, on sparse-matrix-optimized ETL.  
  `Python` `scikit-learn` `PyTorch` `Flask` `PostgreSQL` `Docker`

- **[Deep learning coursework](https://github.com/Skywalker1910?tab=repositories&q=CPSC-8430)**  
  CPSC 8430 assignment series — architectures, training dynamics and evaluation implemented end to end rather than called from a library.  
  `Python` `PyTorch` `Jupyter`

## Toolchain

| Layer | Tools |
| --- | --- |
| Languages | ![Python](https://img.shields.io/badge/-Python-3776ab?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178c6?style=flat-square&logo=typescript&logoColor=white) ![SQL](https://img.shields.io/badge/-SQL-4479a1?style=flat-square&logo=postgresql&logoColor=white) ![C++](https://img.shields.io/badge/-C++-00599c?style=flat-square&logo=cplusplus&logoColor=white) |
| ML / DL | ![PyTorch](https://img.shields.io/badge/-PyTorch-ee4c2c?style=flat-square&logo=pytorch&logoColor=white) ![TensorFlow](https://img.shields.io/badge/-TensorFlow-ff6f00?style=flat-square&logo=tensorflow&logoColor=white) ![scikit-learn](https://img.shields.io/badge/-scikit--learn-f7931e?style=flat-square&logo=scikitlearn&logoColor=white) ![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![OpenCV](https://img.shields.io/badge/-OpenCV-5c3ee8?style=flat-square&logo=opencv&logoColor=white) |
| LLM / RAG | ![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square) ![Transformers](https://img.shields.io/badge/-Transformers-ffd21e?style=flat-square&logo=huggingface&logoColor=black) ![Amazon S3 Vectors](https://img.shields.io/badge/-S3%20Vectors-569a31?style=flat-square) ![Retrieval and evaluation](https://img.shields.io/badge/-retrieval%20%2B%20eval-8250df?style=flat-square) |
| Web | ![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![React](https://img.shields.io/badge/-React-61dafb?style=flat-square&logo=react&logoColor=black) ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Node.js](https://img.shields.io/badge/-Node.js-5fa04e?style=flat-square&logo=nodedotjs&logoColor=white) |
| Cloud & infra | ![AWS](https://img.shields.io/badge/-AWS-232f3e?style=flat-square) ![DynamoDB](https://img.shields.io/badge/-DynamoDB-4053d6?style=flat-square) ![Docker](https://img.shields.io/badge/-Docker-2496ed?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088ff?style=flat-square&logo=githubactions&logoColor=white) ![SQLite](https://img.shields.io/badge/-SQLite-003b57?style=flat-square&logo=sqlite&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169e1?style=flat-square&logo=postgresql&logoColor=white) |

## Repo signals

<p align="center">
  <img alt="Followers" src="https://img.shields.io/github/followers/Skywalker1910?style=flat-square&logo=github&label=followers&color=1f6feb" />
  <img alt="Public repositories" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FSkywalker1910&query=%24.public_repos&style=flat-square&logo=github&label=public%20repos&color=1f6feb" />
  <img alt="Profile views" src="https://komarev.com/ghpvc/?username=Skywalker1910&style=flat-square&color=1f6feb" />
</p>

| Repo | Top language | Commits (1y) | Last commit |
| --- | --- | --- | --- |
| [`Tech-Portfolio`](https://github.com/Skywalker1910/Tech-Portfolio) | ![top language](https://img.shields.io/github/languages/top/Skywalker1910/Tech-Portfolio?style=flat-square&color=1f6feb) | ![commits in the last year](https://img.shields.io/github/commit-activity/y/Skywalker1910/Tech-Portfolio?style=flat-square&label=&color=1a7f37) | ![last commit](https://img.shields.io/github/last-commit/Skywalker1910/Tech-Portfolio?style=flat-square&label=&color=8250df) |
| [`FIFA-World-Cup-2026`](https://github.com/Skywalker1910/FIFA-World-Cup-2026) | ![top language](https://img.shields.io/github/languages/top/Skywalker1910/FIFA-World-Cup-2026?style=flat-square&color=1f6feb) | ![commits in the last year](https://img.shields.io/github/commit-activity/y/Skywalker1910/FIFA-World-Cup-2026?style=flat-square&label=&color=1a7f37) | ![last commit](https://img.shields.io/github/last-commit/Skywalker1910/FIFA-World-Cup-2026?style=flat-square&label=&color=8250df) |
| [`Neural-Log`](https://github.com/Skywalker1910/Neural-Log) | ![top language](https://img.shields.io/github/languages/top/Skywalker1910/Neural-Log?style=flat-square&color=1f6feb) | ![commits in the last year](https://img.shields.io/github/commit-activity/y/Skywalker1910/Neural-Log?style=flat-square&label=&color=1a7f37) | ![last commit](https://img.shields.io/github/last-commit/Skywalker1910/Neural-Log?style=flat-square&label=&color=8250df) |
| [`BB-8`](https://github.com/Skywalker1910/BB-8) | ![top language](https://img.shields.io/github/languages/top/Skywalker1910/BB-8?style=flat-square&color=1f6feb) | ![commits in the last year](https://img.shields.io/github/commit-activity/y/Skywalker1910/BB-8?style=flat-square&label=&color=1a7f37) | ![last commit](https://img.shields.io/github/last-commit/Skywalker1910/BB-8?style=flat-square&label=&color=8250df) |

<sub>Every badge above is read live from the GitHub API at render time — nothing here is hand-maintained.</sub>

---

<p align="center">
  Open to <strong>AI Engineer</strong>, <strong>Machine Learning Engineer</strong> and <strong>Data Scientist</strong> roles ·
  <a href="https://www.adityamore.dev">adityamore.dev</a> ·
  <a href="https://www.linkedin.com/in/more-aditya">LinkedIn</a> ·
  <a href="mailto:aditya.more@outlook.in">aditya.more@outlook.in</a>
  <br />
  <sub>The card above is generated by <a href="generate_card.py"><code>generate_card.py</code></a> — edit the spec, re-run, both themes stay in sync.</sub>
</p>
