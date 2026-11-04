from quiz_validation import validate_quiz


def test_valid_quiz():
    quiz = {
        "questions": [
            {
                "question": "What is AI?",
                "options": ["A", "B", "C", "D"],
                "correct_answer": "A"
            }
        ] * 5
    }

    assert validate_quiz(quiz) is True


def test_invalid_number_of_questions():
    quiz = {"questions": []}

    assert validate_quiz(quiz) is False


def test_invalid_number_of_options():
    quiz = {
        "questions": [
            {
                "question": "What is AI?",
                "options": ["A", "B"],
                "correct_answer": "A"
            }
        ] * 5
    }

    assert validate_quiz(quiz) is False