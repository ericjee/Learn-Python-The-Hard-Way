from sys import argv

# script, file_name = argv
prompt = "> "

# txt = open(file_name)
file_name = raw_input(prompt)
txt = open(file_name)

print "Here\'s your file %r:" % txt
print txt.read()

txt.close()
