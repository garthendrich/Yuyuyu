from curses import window
from socket import AF_INET, SOCK_STREAM, socket


# Main client function
def proceedAsClient(screen: window):
    screen.addstr("Name: ")
    playerName = screen.getstr().decode()

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 5556))
    client.send(playerName.encode())

    # Wait for the game information from the server
    game_info = client.recv(1024).decode()
    screen.addstr(game_info)
    screen.refresh()

    # Send a confirmation to the server to acknowledge receiving the message
    client.send("Received".encode())

    client.close()
