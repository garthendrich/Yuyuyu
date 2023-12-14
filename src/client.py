from curses import window
from socket import AF_INET, SOCK_STREAM, socket

from data.quiz_items import quizItems
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
        clientSocket.recv(1024)

        startQuiz(quizItems, screen)
