import cmd
import readline
from cmd import Cmd

class myinterface(Cmd):

    def do_helloworld(Self, line):
        print("Hello world" + line)
        #command in interface starts with do
        #defines a command hellowrld

    def help_helloworld(self):
        print("print hello world")
        #default is to use the documentantion string

    def complete_helloworld(self, text, line, begidx, endidx):
        possibilities = ['user', 'Nyari', 'Petros']
        return [f for f in possibilities if f.startswith(text)]
           #define auto-completion

if __name__ == '__main__':
    readline.parse_and_bind("tab: complete")
    interface = myinterface()
    interface.cmdloop()

    #configure readline for auto-completion
    #different versions  of readline
    #scriptable either via pipe(not advised)
    #or via command file
     
