from curses import window
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


# Function to handle a client connection
def handle_client(client_socket: socket, player_count: int, screen: window):
    name = client_socket.recv(1024).decode()
    screen.addstr(f"Player {player_count}: {name} has joined.\n\n")

    if player_count == 2:
        screen.addstr("Both players have joined. Starting the game!\n\n")
        send_game_info(client_socket, ["Player 1", "Player 2"], "Awesome Game")
    else:
        screen.addstr("Waiting for the second player to join.\n\n")

    screen.refresh()


# Function to send game information to clients
def send_game_info(client_socket: socket, player_names: list[str], game_name: str):
    for player_name in player_names:
        info = f"Welcome, {player_name}! You are playing {game_name}."
        client_socket.send(info.encode())

        # Ensure that the client has enough time to receive the message
        client_socket.recv(1024)


# Main server function
def proceedAsServer(screen: window):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("0.0.0.0", 5556))  # Use a different port (e.g., 5556)
    server.listen(2)  # Listen for 2 clients

    screen.addstr("[*] Waiting for players to join on port 5556\n\n")
    screen.refresh()

    player_count = 0

    while player_count < 2:
        client, _ = server.accept()

        player_count += 1

        client_handler = Thread(
            target=handle_client, args=(client, player_count, screen)
        )
        client_handler.start()
