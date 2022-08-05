from cmd import Cmd

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("exit")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

MyPrompt().cmdloop()
print('after')
'''
We implemented to commands: exit and add.

When we run the script it will show use the standard prompt:

(Cmd)
If at this point we press TAB twice we get the list of all the available command. In our case that is

add   exit  help
If we type in help we get the following output:

(Cmd) help1
Documented commands (type help <topic>):
========================================
help

Undocumented commands:
======================
add  exit
If we type in help add as the help window suggests for the documented commands we get:

(Cmd) help add
*** No help on add
If we type in add followed by some text and press ENTER the system will run the do_add method and pass the text to the method. In our case we get:

(Cmd) add Hello World
Adding 'Hello World'
If we type in exit it will call the do_exit method, print "Bye" and exit the cmdloop. In our case it means it will go on and print the string "after".

(Cmd) exit
Bye
after
'''
