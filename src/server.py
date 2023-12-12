import socket
import threading

# Function to handle a client connection
def handle_client(client_socket, player_count):
    name = client_socket.recv(1024).decode()
    print(f"Player {player_count}: {name} has joined.")

    if player_count == 2:
        print("Both players have joined. Starting the game!")
        send_game_info(client_socket, ["Player 1", "Player 2"], "Awesome Game")
    else:
        print("Waiting for the second player to join.")

# Function to send game information to clients
def send_game_info(client_socket, player_names, game_name):
    for i, player_name in enumerate(player_names):
        info = f"Welcome, {player_name}! You are playing {game_name}."
        client_socket.send(info.encode())

        # Ensure that the client has enough time to receive the message
        client_socket.recv(1024)

# Main server function
def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5556))  # Use a different port (e.g., 5556)
    server.listen(2)  # Listen for 2 clients

    print("[*] Waiting for players to join on port 5556")

    player_count = 0

    while player_count < 2:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        player_count += 1

        client_handler = threading.Thread(target=handle_client, args=(client, player_count))
        client_handler.start()
        
# if __name__ == "__server__":
#     server()
