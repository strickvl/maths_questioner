"""Main Mathser logic."""

DELIMITER = "=========="


def get_questions() -> list[str]:
    """Get questions from a source file.

    Returns:
        The content of the source file as a list.
    """
    with open("assets/questions.txt", "r") as file:
        content = file.read()
    return list(
        filter(
            lambda question: question not in ["", "\n"],
            content.split(DELIMITER),
        )
    )


def parse_questions(questions: list[str]) -> dict[str, str]:
    """Parse questions from a string.

    Args:
        questions: The string containing the questions

    Returns:
        A list of questions
    """
    parsed_questions = {}
    return parsed_questions


if __name__ == "__main__":
    # get the content
    content = get_questions()
    # split the content into questions
    parsed_questions = parse_questions(content)
    # print the questions
    for question in parsed_questions:
        print(question)
