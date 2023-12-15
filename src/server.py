from curses import window
import json
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from typing_extensions import TypedDict

from data.quiz_items import quizItems


TAKER_COUNT = 2


class Client(TypedDict):
    userName: str
    socket: socket
    thread: Thread
    answers: list[str | int]


def proceedAsServer(screen: window):
    with socket(AF_INET, SOCK_STREAM) as serverSocket:
        serverSocket.bind(("0.0.0.0", 5556))  # Use a different port (e.g., 5556)
        serverSocket.listen(TAKER_COUNT)

        clients = findConnections(serverSocket, screen)

        screen.erase()
        screen.addstr("Quiz is ongoing\n\n")
        screen.refresh()

        for client in clients:
            client["socket"].send(json.dumps(quizItems).encode())
            client["thread"].start()

        for client in clients:
            client["thread"].join()

        screen.erase()

        for client in clients:
            screen.addstr(json.dumps(client["answers"]) + "\n")
            screen.refresh()

        screen.getch()


def findConnections(serverSocket: socket, screen: window):
    screen.addstr("Waiting for users to join on port 5556\n\n")
    screen.refresh()

    clients: list[Client] = []

    while len(clients) < TAKER_COUNT:
        clientSocket, _ = serverSocket.accept()
        userName = clientSocket.recv(1024).decode()
        answersReceiver: list[str | int] = []
        thread = Thread(target=receiveAnswers, args=(clientSocket, answersReceiver))
        clients.append(
            {
                "userName": userName,
                "socket": clientSocket,
                "thread": thread,
                "answers": answersReceiver,
            }
        )

        screen.addstr(f"User {userName} has joined the lobby.\n\n")
        screen.refresh()

    return clients


def receiveAnswers(clientSocket: socket, answersReceiver: list[str | int]):
    answers: list[str | int] = json.loads(clientSocket.recv(1024).decode())
    for answer in answers:
        answersReceiver.append(answer)
