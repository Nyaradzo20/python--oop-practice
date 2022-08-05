*does parsing and execution of commands from console
*operates on behalf of clientd eg modules
supportd simple syntax:
<client><command [<positonal arg>....
*during startup clients that support commands provide information about them to the cmd module:
-client name .
-for each command
+command name
+command handler callback function
+help string
*when cmd receives a command line from console
-handles some commands directly eg help
-finds clients supporting thr command and invokes function callback
********************************************************
##The idea of the python module cmd which allows to have a shell with dedicated command, auto-completion, help.
1.create a python shell interface
-support a list of commands
-smart auto completion
-allow various moude ie tutorials mde and smart help using python cmd
