import cmd

class MyPrompt(cmd.Cmd):
    pass

MyPrompt().cmdloop()
'''
We create an instance object of the MyPrompt class and immediately call the cmdloop method. We could have used a temporary variable there if we wanted to be a bit more verbose like this:
p = MyPrompt()
p.cmdloop()
but the result is the same.

When we run this script it will display a default prompt:

(Cmd)
You can't do much with it. You can type in ? and press ENTER to get the following help:

Documented commands (type help <topic>):
========================================
help
help # (Cmd) Ctrl-C

You can ask for help on help by typing in:

help help
And it will print:

List available commands with "help" or detailed help with "help cmd".
If you would like to exit the application you need to press Ctlr-C and get a KeyboardInterrupt.
'''
