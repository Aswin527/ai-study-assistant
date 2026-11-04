def validate_quiz(quiz):
    questions = quiz["questions"]

    if len(questions) != 5:
        return False

    for question in questions:
        if len(question["options"]) != 4:
            return False

        if question["correct_answer"] not in question["options"]:
            return False

    return True

