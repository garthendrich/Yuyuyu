from curses import window
import json
from socket import AF_INET, SOCK_STREAM, socket

from src.globals import QuizItem
from src.quiz_proper import startQuiz


def proceedAsClient(screen: window):
    screen.addstr("Name: ")
    playerName = screen.getstr().decode()

    screen.addstr("Server IP address: ")
    serverIp = screen.getstr().decode()
    screen.addstr("Server port number: ")
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

        score = int(clientSocket.recv(1023).decode())
        screen.erase()
        screen.addstr(f"You got a score of {score} out of {len(quizItems)}\n\n")
        screen.addstr("Press any key to exit")
        screen.getch()
