# AI_LLM-for-Data-Analysis (Shivaji.ai)

## Shivaji.ai — Local LLM for Data Analysis

**Shivaji.ai** is an open-source AI chatbot that helps you analyze CSV datasets using natural language. It runs **fully locally** using [Ollama](https://ollama.com/) and [FastAPI](https://fastapi.tiangolo.com/), ensuring **data privacy** with zero dependency on cloud APIs.

---

## Features

- Upload your own CSV file via a simple web UI
- Ask natural language questions like:  
  "What is this dataset about?" or "Plot the top 5 features of this dataset"
- Get **concise answers**, **explanatory analysis**, and **Python code** using `pandas` + `matplotlib`
- Fully private — uses **local LLMs** like `codellama` via Ollama
- Modular and open-source — easy to extend with more tools/models

---

## Tech Stack

| Layer         | Tech                      |
|---------------|---------------------------|
| Frontend      | React + Vite              |
| Backend       | FastAPI + Uvicorn         |
| LLM Runtime   | [Ollama](https://ollama.com/) (`codellama`) |
| Python Libs   | `pandas`, `matplotlib`, `python-multipart` |
| Communication | HTTP (upload + query endpoints) |

---

## Requirements

1. **Python 3.11+**

   ```bash
   pip install fastapi uvicorn pandas matplotlib python-multipart

