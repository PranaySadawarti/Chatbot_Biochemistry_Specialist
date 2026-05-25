# Chatbot_Biochemistry_Specialist 🧬

A fast and specialized **Biochemistry Chatbot** powered by **Groq API** and built with **FastAPI**.

---

## Overview

An intelligent AI assistant that provides accurate answers on Biochemistry topics including metabolism, enzyme kinetics, protein structure, molecular biology, biochemical pathways, and more.

---

## Features

- ⚡ Ultra-fast responses using Groq API
- 🧪 Specialized in Biochemistry
- 🌐 RESTful API with FastAPI + Swagger UI
- 💬 Simple chat endpoint
- 🔒 Secure API key handling via `.env`

---

## Tech Stack

- **Backend**: FastAPI
- **LLM**: Groq API
- **Language**: Python 3.10+
- **Server**: Uvicorn

---

## Quick Setup

```bash
git clone https://github.com/PranaySadawarti/Chatbot_Biochemistry_Specialist.git
cd Chatbot_Biochemistry_Specialist

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env
# Add your Groq API key in .env

## Run the app:
Bash
