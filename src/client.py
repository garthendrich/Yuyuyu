from curses import window
import json
from socket import AF_INET, SOCK_STREAM, socket

from src.globals import QuizItem
from src.quiz_proper import startQuiz


def proceedAsClient(screen: window):
    screen.addstr("👉👉 Name: ")
    playerName = screen.getstr().decode()

    screen.addstr("👉👉 Server IP address: ")
    serverIp = screen.getstr().decode()
    screen.addstr("👉👉 Server port number: ")
    serverPortNumber = int(screen.getstr().decode())

    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        clientSocket.connect((serverIp, serverPortNumber))
        clientSocket.send(playerName.encode())

        screen.addstr("\nWaiting for other users to join the lobby\n")
        screen.refresh()

        # wait for test to start
        quizItems: list[QuizItem] = json.loads(clientSocket.recv(8192).decode())
        answers = startQuiz(quizItems, screen)
        clientSocket.send(json.dumps(answers).encode())

        screen.addstr("Waiting for other users to finish taking the quiz\n")
        screen.refresh()

        # receive score and correctness information from the server
        received_data = clientSocket.recv(8192).decode()
        data = json.loads(received_data)
        score = data["score"]
        correctness = data["correctness"]
        question_categories = data["question_categories"]

        screen.erase()
        screen.addstr(f"You got a score of {score} out of {len(quizItems)}\n\n")

        # Display correctness information for each question
        screen.addstr("Summary of Answers:\n")
        for index, is_correct in enumerate(correctness, start=1):
            screen.addstr(f"Question {index} ({question_categories[index-1].capitalize()}): {'Correct' if is_correct else 'Incorrect'}\n")

        screen.addstr("Press any key to exit")
        screen.getch()
