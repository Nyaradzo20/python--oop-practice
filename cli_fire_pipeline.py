import fire
from getpass import getpass

def login(username = None):
    if username == None:
        username == input('username: ')
    if username == None:
        print('A username is required')
        return
    pw = getpass('Password: ')
    return(username, pw)
