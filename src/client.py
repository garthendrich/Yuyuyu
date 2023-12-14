from curses import window
import json
from socket import AF_INET, SOCK_STREAM, socket

from src.globals import QuizItem
from src.quiz_proper import startQuiz


def proceedAsClient(screen: window):
    screen.addstr("Name: ")
    playerName = screen.getstr().decode()

    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        clientSocket.connect(("127.0.0.1", 5556))
        clientSocket.send(playerName.encode())

        screen.addstr("\nWaiting for other users to join the lobby\n\n")
        screen.refresh()

        # wait for test to start
        quizItems: list[QuizItem] = json.loads(clientSocket.recv(1024).decode())
        startQuiz(quizItems, screen)
