from openai import OpenAI

client = OpenAI()

previous_response_id=None

while True:
    question = input("\nAsk your AI tutor (or type 'exit'): ")

    if question.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are a friendly AI tutor for Grade 10 students. "
            "Explain concepts clearly with simple examples."
            "You can also provide step-by-step solutions to problems and encourage students to ask follow-up questions. "
            "If the student asks for help with homework, provide guidance without giving away the final answer. "
            "You're mainly focused on students in Grade 10, so keep your explanations age-appropriate and engaging."
        ),
        input=question,
        previous_response=previous_response_id
    )

    print("\nAI Tutor:", response.output_text)

    previous_response_id = response.id