import re
import sys


urlList = []

with open(sys.argv[1], 'r') as f:


    for line in f:
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
 #----counting each url and adding it to a dictionary----#
occurences = dict((i, urlList.count(i)) for i in urlList)
for item,value in occurences.items():
    print "\"%s\",%d \n"%(item,value)



