import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("AI Study Assistant")

mode = st.sidebar.radio(
    "Choose a mode",
    ["AI Tutor", "Quiz Generator"]
)

if mode == "AI Tutor":
    st.subheader("Chat with your AI tutor")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your tutor..."):
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        instructions=(
                            "You are a friendly AI tutor for Grade 10 students. "
                            "Explain concepts clearly with simple examples."
                        ),
                        input=prompt,
                        previous_response_id=st.session_state.get(
                            "previous_response_id"
                        )
                    )

                    answer = response.output_text
                    st.markdown(answer)
                except Exception as e:
                    st.error(f"Error: {e}")
                    answer = "Sorry, I couldn't process your request."

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.session_state.previous_response_id = response.id

else:
    st.subheader("Generate a quiz")

    topic = st.text_input("Enter a topic")
    generate = st.button("Generate Quiz")

    if generate and topic:
        with st.spinner("Creating your quiz..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                instructions=(
                    "Create exactly five multiple-choice questions "
                    "for Grade 10 students. Each question must have "
                    "four options and one correct answer."
                ),
                input=f"Create a quiz about {topic}.",
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "quiz",
                        "strict": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "questions": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "question": {
                                                "type": "string"
                                            },
                                            "options": {
                                                "type": "array",
                                                "items": {
                                                    "type": "string"
                                                }
                                            },
                                            "correct_answer": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "question",
                                            "options",
                                            "correct_answer"
                                        ],
                                        "additionalProperties": False
                                    }
                                }
                            },
                            "required": ["questions"],
                            "additionalProperties": False
                        }
                    }
                }
            )

        st.session_state.quiz = response.output_text
        st.session_state.quiz_topic = topic
        st.session_state.quiz_submitted = False

    if "quiz" in st.session_state:
        import json

        quiz = json.loads(st.session_state.quiz)
        answers = []

        with st.form("quiz_form"):
            for i, question in enumerate(quiz["questions"]):
                st.markdown(f"**{i + 1}. {question['question']}**")

                answer = st.radio(
                    "Select an answer",
                    question["options"],
                    index=None,
                    key=f"question_{i}"
                )

                answers.append(answer)

            submitted = st.form_submit_button("Submit Quiz")

        if submitted:
            score = 0

            for i, question in enumerate(quiz["questions"]):
                if answers[i] == question["correct_answer"]:
                    score += 1

            st.success(f"Your score: {score}/{len(quiz['questions'])}")