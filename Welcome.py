#import
from Georgian_B import Georgian_B, write_in_file
import time

#Welcome text
welcome = ["gamarjoba,", "ginda", "SeZlo", "aseTi", "ramis", "gakeTeba", "piTonSi?", "maSin", "ganagrZe", "videos", "yureba." ]
#text to write in a file
sentence = []

#Which shapers and separators do we want to use
shapers =    ["0", "(", ")", "#", "%", "$", "1", "@", "=", "-", "*"]
separators = [" ", "0", "o", "^", "-", ",", " ", "!", "-", " ", " "]

#Do actual job
for index,line in enumerate(welcome):
    
    #print 4th and 7th letters slower
    wait_time = 0.001 #default speed

    if index == 0:
        wait_time = 0.1
        
    elif index == 3 or index == 6:
        wait_time = 0.05
    #make text centered on the screen
    centered_text = line.center(10)
    #print result
    word = Georgian_B(centered_text, separators[index], shapers[index], True, wait_time)
    sentence += word
    #wait before next word
    time.sleep(0.4)

#wait few seconds, write data in text file and open it
write_in_file(sentence, open_after = True)
