from curses import window
from socket import AF_INET, SOCK_STREAM, socket


TAKER_COUNT = 2


clientSockets: list[socket] = []


def proceedAsServer(screen: window):
    with socket(AF_INET, SOCK_STREAM) as serverSocket:
        serverSocket.bind(("0.0.0.0", 5556))  # Use a different port (e.g., 5556)
        serverSocket.listen(TAKER_COUNT)

        screen.addstr("Waiting for users to join on port 5556\n\n")
        screen.refresh()

        while len(clientSockets) < TAKER_COUNT:
            clientSocket, _ = serverSocket.accept()

            clientSockets.append(clientSocket)

            userName = clientSocket.recv(1024).decode()
            screen.addstr(f"User {userName} has joined the lobby.\n\n")

            if len(clientSockets) == TAKER_COUNT:
                screen.addstr("Users have joined. Quiz starts now!\n\n")

                for clientSocket in clientSockets:
                    clientSocket.send(" ".encode())

            else:
                screen.addstr("Waiting for other users to join the lobby\n\n")

            screen.refresh()

        screen.getch()
