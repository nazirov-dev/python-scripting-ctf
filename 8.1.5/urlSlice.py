#!/usr/bin/python3

hrefLine = '<a herf="htts://www.offensive-security.cam/offsec/game-hacking-intro/">Introduction to Game Hacking</a>'

start="htts"
end="\">"

url=hrefLine[hrefLine.index(start):hrefLine.index(end)]
print(url)
