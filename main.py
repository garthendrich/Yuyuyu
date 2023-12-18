import curses
from curses import window

from src.utils import displayChoices
from src.client import proceedAsClient
from src.server import proceedAsServer


def main(screen: window):
    curses.echo()

    choiceIndex = displayChoices("Yuyuyu", ["Host the test", "Take the test"], screen)
    screen.clear()
    if choiceIndex == 0:
        proceedAsServer(screen)
    else:
        proceedAsClient(screen)


if __name__ == "__main__":
    curses.wrapper(main)
