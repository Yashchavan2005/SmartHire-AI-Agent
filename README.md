# SmartHire AI Agent

## 📌 Project Description

SmartHire AI Agent is an AI-powered mock interview system developed using Python and Large Language Models (LLM).

It conducts technical interviews, evaluates student answers, provides intelligent feedback, calculates scores, and generates detailed interview reports.

The project uses **Llama 3.2 (1B) through Ollama** for local AI-powered answer evaluation.

## 🚀 Features

- AI-Based Technical Mock Interviews
- Full Interview Mode
- Topic-Wise Interview Mode
- LLM-Based Answer Evaluation
- Automatic Score Extraction
- Detailed Technical Feedback
- Improved Answer Suggestions
- Overall Performance Analysis
- Automatic Interview Report Generation
- Local LLM Integration Using Ollama

## 🛠️ Technologies Used

- Python
- Ollama
- Llama 3.2 (1B)
- Requests Library
- Large Language Models (LLM)
- Prompt Engineering

## 📂 Project Structure

```text
SmartHire_AI_Agent/
│
├── main.py
├── questions.py
├── interview_agent.py
├── llm_engine.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── reports/
│
└── .venv/
```

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open Project Folder

```bash
cd SmartHire_AI_Agent
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Ollama Setup

1. Install Ollama.
2. Download the Llama 3.2 model.

```bash
ollama pull llama3.2:1b
```

3. Start Ollama.

```bash
ollama serve
```

The project communicates with Ollama through:

```text
http://localhost:11434/api/generate
```

## ▶️ Run the Project

```bash
python main.py
```

## 💻 Interview Modes

**1. Full Interview**

Conducts a complete technical interview using all available questions.

**2. Topic-Wise Interview**

Allows students to select a specific technical topic and practice related questions.

## 📊 Interview Evaluation

The AI evaluates student answers based on:

- Technical Accuracy
- Conceptual Understanding
- Missing Technical Points
- Improved Answer
- Interview Suggestions

The system generates a score out of 10 for each answer.

## 📄 Report Generation

After completing the interview, the system automatically generates a text report containing:

- Student Information
- Total Questions Asked
- Total Score
- Average Score
- Overall Performance
- Question-Wise Analysis
- LLM Evaluation
- Improvement Suggestions

Reports are saved automatically inside the `reports/` folder.

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

1. Python Programming
2. Object-Oriented Programming
3. API Integration
4. LLM Integration
5. Prompt Engineering
6. AI Agent Development
7. Exception Handling
8. File Handling
9. Automated Report Generation

## 👨‍💻 Author

**Yash Kumar Chavan**

GitHub: Yashchavan2005

## 📌 Note

This project uses a locally running Ollama model. Ollama must be installed and the Llama 3.2 (1B) model must be available before running the application.
