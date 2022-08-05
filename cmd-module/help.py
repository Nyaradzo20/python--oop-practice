from cmd import Cmd

from cmd import Cmd

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("exit")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

    def help_add(self):
        print('adding new entry to the system')

MyPrompt().cmdloop()
print('after')
'''
Entering ? not all the commands are listed under the "Documented commands":

(Cmd) ?

Documented commands (type help <topic>):
========================================
add  exit  help
We can get help by typing in help and the name of the command:

(Cmd) help add
Add a new entry to the system.
(Cmd) help exit
exit the application.
We can still exit the application:

(Cmd) exit
Bye
'''
