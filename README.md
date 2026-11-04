# AI Study Assistant

An AI-powered study assistant built with Python, Streamlit, and the OpenAI API. The application helps students understand concepts, ask follow-up questions, and generate multiple-choice quizzes.

This is my first project in my AI Engineering learning journey, where I explored LLM integration, conversation history, structured outputs, and AI application testing.

## Features

### 1. AI Tutor
- Answers questions in a conversational chat interface.
- Explains concepts using simple language and real-world examples.
- Maintains conversation context for follow-up questions.
- Designed to support Grade 10 students.

### 2. Quiz Generator
- Generates multiple-choice quizzes on user-provided topics.
- Uses structured outputs to produce machine-readable quiz data.
- Displays questions and answer options in the Streamlit interface.
- Calculates the student's score after submission.

### 3. Quiz Validation
- Checks whether a quiz contains the expected number of questions.
- Verifies the number of options per question.
- Checks whether the correct answer matches one of the options.
- Includes automated tests using pytest.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| OpenAI API | LLM integration |
| Streamlit | Web interface |
| JSON Schema | Structured quiz generation |
| pytest | Automated testing |

## Project Structure

```text
ai-study-assistant/
├── app.py
├── quiz.py
├── quiz_validation.py
├── test_quiz.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- An OpenAI API key
- An internet connection

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-study-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet, add:

```text
openai
streamlit
pytest
```

### 4. Configure your API key

Create an API key from the [OpenAI API dashboard](https://platform.openai.com/api-keys).

Set it as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Keep your API key private. Never commit it to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Running Tests

Run the automated tests using:

```bash
pytest -v
```

The tests check whether the quiz validation function correctly handles valid and invalid quiz data.

## What I Learned

- Connecting a Python application to an LLM using an API.
- Writing system instructions and user prompts.
- Maintaining conversation history using response IDs.
- Generating structured outputs using JSON Schema.
- Building interactive AI applications with Streamlit.
- Validating AI-generated content.
- Writing automated tests with pytest.
- Handling API errors and improving application reliability.

## Future Improvements

- Add RAG to answer questions from uploaded study materials.
- Display references and citations from source documents.
- Improve quiz evaluation and content accuracy.
- Add persistent conversation history.
- Deploy the application for students to access online.

## Learning Resources

- [OpenAI API Quickstart](https://developers.openai.com/api/docs/quickstart)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

---

Built as part of my hands-on journey into AI Engineering.
