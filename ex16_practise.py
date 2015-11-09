from sys import argv

script, filename = argv

print "I'm going to open the file %s." % filename
txt = open(filename)

print txt.read()
print txt.readline(2)
