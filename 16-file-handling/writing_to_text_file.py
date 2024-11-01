# execute from the command line, ensure cursor is in this directory

file = open("data2.txt", mode='a')
# w writes but overwrites existing
# x creates, raises an FileExistsError error if exists already
# a append to existing

# 1. write()
text = "\n\nadditional content\nadditional content\nadditional content"
file.write(text)
file.close()


