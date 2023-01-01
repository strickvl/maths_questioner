"""Main Mathser logic."""

DELIMITER = "=========="


def get_questions():
    """Get questions from a source file.

    Returns:
        The content of the source file
    """
    with open("assets/questions.txt", "r") as file:
        content = file.read()
    return content


if __name__ == "__main__":
    # get the content
    content = get_questions()
    # split the content into questions
    questions = content.split(DELIMITER)
    # print the questions
    for question in questions:
        print(question)
