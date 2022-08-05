from getpass import getpass
import fire

def login(name = None):
    if name == None:
        name = input("whats your name?\n")
    pw = getpass("whats your password?\n")

    return ("good job")
if __name__ == '__main__':
    fire.Fire(login)
