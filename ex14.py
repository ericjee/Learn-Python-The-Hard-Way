from sys import argv

script, user_name = argv
prompt = ">> "

print "Hi %s, I\'m the %s script. " % (user_name, script)
print "I\'d like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What\'s your wife\'s name?"
my_wife_name = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
Your wife\'s name is %s.
And you have a %r computer. Nice.
""" % (likes, lives, my_wife_name, computer)
