from curses import KEY_ENTER, window
import json
import socket as socketModule
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from typing_extensions import cast as typecast, TypedDict

from data.quiz_items import items, quizItemsWithoutAnswers
from src.globals import Identification, MultipleChoice


class Client(TypedDict):
    userName: str
    socket: socket
    thread: Thread
    answers: list[str | int]

def getScoreByCategory(category):
    if category == "easy":
        return 2
    elif category == "medium":
        return 3
    elif category == "difficult":
        return 5

def proceedAsServer(screen: window):
    with socket(AF_INET, SOCK_STREAM) as serverSocket:
        serverSocket.bind(("", 0))
        serverSocket.listen()

        clients = findConnections(serverSocket, screen)

        screen.erase()
        screen.addstr("Quiz is ongoing\n\n")
        screen.refresh()

        for client in clients:
            client["socket"].send(json.dumps(quizItemsWithoutAnswers).encode())
            client["thread"].start()

        for client in clients:
            client["thread"].join()

         # Create/open a file to write the score summary
        with open('Overall_Scores.txt', 'w') as file:
            file.write("Score Summary\n\n")

            screen.erase()
            screen.addstr(f"Score Summary\n\n")
            for client in clients:
                score = 0

                for itemIndex in range(len(items)):
                    item = items[itemIndex]
                    clientAnswer = client["answers"][itemIndex]

                    itemType = item["itemType"]
                    if itemType == "identification":
                        item = typecast(Identification, item)

                        if clientAnswer in item["possibleAnswers"]:
                            score += getScoreByCategory(item["category"])

                    elif itemType == "multiple choice":
                        item = typecast(MultipleChoice, item)

                        if clientAnswer == item["answerIndex"]:
                            score += getScoreByCategory(item["category"])

                screen.addstr(f"{client['userName']}: {score}\n")

                # Write the score to the file
                file.write(f"{client['userName']}: {score}\n")
                
                client["socket"].send(str(score).encode())

        screen.addstr("\nPress any key to exit")
        screen.refresh()
        screen.getch()


def findConnections(serverSocket: socket, screen: window):
    hostname = socketModule.gethostname()
    ip = socketModule.gethostbyname(hostname)
    portNumber = serverSocket.getsockname()[1]

    screen.addstr("Waiting for users to join...\n")
    screen.addstr("Press enter to start quiz.\n\n")
    screen.addstr(f"IP Address: {ip}\n")
    screen.addstr(f"Port number: {portNumber}\n\n")
    screen.refresh()

    clients: list[Client] = []

    serverSocket.settimeout(0.1)
    screen.nodelay(True)
    keyPress = None
    while True:
        keyPress = screen.getch()

        if keyPress in [KEY_ENTER, 10, 13]:
            if len(clients) > 0:
                break
            screen.addstr("There are no users yet\n\n")

        clientSocket = None
        try:
            clientSocket, _ = serverSocket.accept()
        except socketModule.timeout:
            if clientSocket is None:
                continue

        userName = clientSocket.recv(1024).decode()
        answersReceiver: list[str | int] = []
        clientThread = Thread(
            target=receiveAnswers, args=(clientSocket, answersReceiver)
        )
        clients.append(
            {
                "userName": userName,
                "socket": clientSocket,
                "thread": clientThread,
                "answers": answersReceiver,
            }
        )

        screen.addstr(f"User {userName} has joined the lobby.\n")
        screen.refresh()
    screen.nodelay(False)

    return clients


def receiveAnswers(clientSocket: socket, answersReceiver: list[str | int]):
    answers: list[str | int] = json.loads(clientSocket.recv(1024).decode())
    for answer in answers:
        answersReceiver.append(answer)
