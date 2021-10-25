fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
     for word in line.split():
          if word in line.split():
               line.split().append(word)
          if word not in line.split():
               continue
          print (word)
