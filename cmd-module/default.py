from cmd import Cmd

class MyPrompt(Cmd):
    def do_exit(self, inp):
        '''exit the application.shothsnd x or q'''
        print('bye')
        return True

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print('Default: {}'.format(inp))

MyPrompt().cmdloop()
            
