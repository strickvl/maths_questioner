# open the txt file inside the assets/ folder
# and read the content
# then return the content
DELIMITER = "=========="


def get_questions():
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
