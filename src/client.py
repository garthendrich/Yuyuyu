import socket

# Function to get player name from the user
def get_player_name():
    name = input("Enter your name: ")
    return name

# Main client function
def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5556))

    player_name = get_player_name()
    client.send(player_name.encode())

    # Wait for the game information from the server
    game_info = client.recv(1024).decode()
    print(game_info)

    # Send a confirmation to the server to acknowledge receiving the message
    client.send("Received".encode())

    client.close()

# if __name__ == "__client__":
#     client()
