from cmd import Cmd

class MyPrompt(Cmd):
    prompt = '>>'
    intro = "type help or ? to list commands"

    def do_exit(self, inp):
        print('bye')
        return True

MyPrompt().cmdloop()
     
