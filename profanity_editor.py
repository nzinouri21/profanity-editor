
import urllib

def read_text():
    quotes = open(r"C:\Users\nazanin\Desktop\HHIV\Intro to Programming Nanodegree\4-Create a Movie Website\send-a-text\movie_quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file

    check_profanity(contents_of_file)

    quotes.close()

def check_profanity(text_to_ckeck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_ckeck)
    output = connection.read()
    if output == "true":
        print "Profanity Alert!"
    elif output == "false":
        print "This document has no curse words!"
    else:
        print "Could not scan the document properly."
    #print output

    connection.close()


read_text()
