import urllib, json


def read_text():
    url = "http://www.wdylike.appspot.com/?q="
    file = open('text.txt', 'r')
    profanity_found = False
    for line in file:
        response = urllib.urlopen(url+line)
        data = json.loads(response.read())
        if data:
            print "Profanity found"
            profanity_found = True
    if not profanity_found:
        print "All good here"
    file.close()
read_text()