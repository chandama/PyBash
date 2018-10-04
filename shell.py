# Chandler Taylor
# IT344 Lab 3
# September 26 2017

import sys, os, subprocess, shlex, socket, pwd

result = 0
# loop until result != 1
while result == 0: 
    # This is my attempt to copy the actual bash where it shows your username, hostname
    #   and your current directory. Its close enough to the acutal bash but only shows
    #   the basename of the cwd and not everything from Desktop forward like the real bash
    shell_name = pwd.getpwuid(os.getuid()).pw_name + "@" + socket.gethostname() + ":~/" + os.path.basename(os.getcwd()) + "$ "
    line = raw_input(shell_name) 

    if line != "":
    	# use shlex to split user input into an array of strings
    	parse_string = shlex.split(line)

    	if parse_string[0] == "exit":
    		# exit loop
    		result = 1
    		# print exit result
    		print "Exited with result: ", result
    	elif parse_string[0] == "cd":
    		# if user enters only cd and no argument, reprompt for input
    		if len(parse_string) == 1:
    			continue
    		# call os.chdir command to cd to the directory specified by the arg
    		# if the user enters an invalid directory, catch the exception and reprompt
    		else:
    			try:
	    			os.chdir(parse_string[1])
	    		except:
	    			print "bash: cd: ", parse_string[1], " No such file or directory"
                # if no exception, print current working directory after cd executes
                # print os.getcwd()
    	else:
    		# use subprocess.call(parse_string) to call external commands
            # if the user enters an invalid command, the error is caught and handled
            #   instead of exiting the program
            try:
    		    subprocess.call(parse_string)
            except: 
                print parse_string[0], ": command not found"