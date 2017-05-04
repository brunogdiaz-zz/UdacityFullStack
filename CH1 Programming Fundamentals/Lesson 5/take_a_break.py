from time import sleep
import webbrowser

#Should take 3 breaks
number_of_breaks = 3
break_time = 5

while number_of_breaks > 0:
    sleep(break_time)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    number_of_breaks -= 1