"""Say hello, world using the CowSay Python package."""

from cowsay import cow

def hello():
    """Say hello, world."""
    print(cow("Hello, World!"))

if __name__ == "__main__":
    hello()
