from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying file %s to %s" % (from_file, to_file)

# # We could do these two on one line too, how?
# in_data = open(from_file).read()

# print "The input file is %d byte long." % len(in_data)

# print "Does the output file exists? %s" % exists(to_file)

# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()
# output_file = open(to_file, 'w')
# output_file.write(in_data)

# print "All Done."

# output_file.close()
# open(from_file).close()

open(to_file, 'w').write(open(from_file).read())
