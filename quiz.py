import json
from openai import OpenAI

client = OpenAI()

topic = input("Enter a topic for the quiz: ")

response = client.responses.create(
    model = "gpt-4.1-mini",
    instructions = (
        "You are a educational quiz generator for grade 10 students. "
        "Generate a quiz with 5 multiple choice questions on the given topic."
    ),
    input = f"Generate a quiz on the topic: {topic}",
    text = {
        "format": {
            "type" : "json_schema",
            "name" : "quiz",
            "strict" : True,
            "schema" : {
                "type": "object",
                "properties": {
                    "questions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {"type": "string"},
                                "options": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "correct_answer": {"type": "string"}
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

quiz = json.loads(response.output_text)

for i, question in enumerate(quiz["questions"], start=1):
    print(f"\n{i}. {question['question']}")

    for option in question["options"]:
        print(f"   {option}")

    print(f"Answer: {question['correct_answer']}")