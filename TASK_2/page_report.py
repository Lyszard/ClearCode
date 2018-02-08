import re
import sys


urlList = []
emptyNumber = 0
error = False
with open(sys.argv[1], 'r') as f:

    for  line in f:
        if  line.strip() == "":
            emptyNumber+=1
            error = True


        else:
        # ----finding url in a line----#
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            # ----removing the query string part----#
            text = urls[0].split("?")
            # ----removing ending slash----#
            if text[0][-1] == "/":
                text[0] = text[0][:-1]
                urlList.append(text[0])
            else:
                urlList.append(text[0])

if error:
    print >> sys.stderr, "Invalid log lines:%d " % emptyNumber
else:
    pass

     #----counting each url and adding it to a dictionary----#
occurences = dict((i, urlList.count(i)) for i in urlList)
for item,value in occurences.items():
    print "\"%s\",%d \n"%(item,value)



