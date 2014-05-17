
from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
    #    print "Encountered a start tag:", tag
    #def handle_endtag(self, tag):
    #    print "Encountered an end tag :", tag
    def handle_data(self, data):
        if data == "\n" or data == "" or data == " " or data == "\t" or data == "\x0b" or data == "\r" or data == "\x0c":
            pass
        else:
            print data

# instantiate the parser and fed it some HTML

#f = open("Bulbasaur.html")

parser = MyHTMLParser()
#parser.feed('<html><head><title>Test</title></head>'
#            '<body><h1>Parse me!</h1></body></html>')

for i in range(1, 5):
    html_str = "http://www.psypokes.com/dex/psydex/"
    if i < 10:
        html_str += ("00" + str(i))
    elif 10 < i < 100:
        html_str += ("0" + str(i))
    else:
        html_str += (str(i))

    html_str += "/general"

    f = urllib2.urlopen(html_str)

    flag = 0
    for line in f:
        #print line[9:22]
        if line[9:22] == "Begin Content":
            flag = 1
        if flag == 1:
            parser.feed(line)

    html_str = ""