# 🤖 Prompt Enhancer

Prompt Enhancer is an AI-powered prompt enhancement agent built with Python and Ollama. It helps users transform raw or unclear prompts into clear, specific, structured, and effective prompts.

Instead of immediately rewriting every prompt, the agent first analyzes the user's intent and identifies missing context, ambiguous requirements, or unclear constraints. When necessary, it asks clarification questions, summarizes the gathered requirements, and requests confirmation before generating the final enhanced prompt.

## ✨ Features

* Analyze raw user prompts
* Identify ambiguity and missing requirements
* Ask clarification questions when necessary
* Summarize requirements for user confirmation
* Generate structured and effective enhanced prompts
* Use Ollama's API for AI-powered responses
* Maintain conversation context during the enhancement workflow
* Modular project structure for easier maintenance and future expansion

## 🛠️ Tech Stack

* **Language:** Python
* **LLM Provider:** Ollama
* **Model:** `gpt-oss:20b`
* **Libraries:** `ollama`, `python-dotenv`
* **Interface:** Command Line Interface (CLI)

## 🎯 Project Goal

The goal of this project is to build a reliable prompt enhancement workflow that prioritizes understanding the user's requirements before generating an improved prompt.

## 🔄 How It Works

1. The user enters a raw prompt.
2. The agent analyzes the prompt.
3. If important information is missing, it asks clarification questions.
4. The user provides answers.
5. The agent summarizes the requirements.
6. The user confirms or corrects the requirements.
7. The agent generates the final enhanced prompt.

## 📁 Project Structure

The project follows a modular architecture, separating the application entry point, AI provider, system instructions, agent logic, configuration, and utility functions. This makes the code easier to maintain and allows future integration with other LLM providers.

## 🚀 Future Improvements

* Support for multiple AI providers
* Structured response validation
* Web interface using FastAPI
* Persistent conversation history
* Additional prompt templates and enhancement strategies
