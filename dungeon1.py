import random


helptext = """
dungeon game move the hero with the keys w a s d
press space to create a new level
"""

maxlines=22
maxchars=60
d=[]

# --- generate dungeon ---
def generate_dungeon():
    d = []
    for y in range(maxlines):
        line=[]
        for x in range(maxchars):
            if x == 0 or y == 0 or x == (maxchars)-1 or y == maxlines-1:
                line.append("#")
            else:
                line.append(random.choice((".")))
        d.append(line)
    # zufalls wände
    for _ in range(2):
        for y in range(maxlines):
            if random.random() < 0.2:
                start=random.randint(1,maxchars-2)
                ende=random.randint(start, maxchars-1)
                for x in range(start, ende):
                    d[y][x]="#"
        for x in range(maxchars):
            if random.random() < 0.2:
                start=random.randint(1,maxlines-2)
                ende=random.randint(start, maxlines-1)
                for y in range(start, ende):
                    d[y][x]="#"
    return d    


# --- generate hero

hero = "@"
herox = 4
heroy = 4
herohp = 20

# --- generate Monster

monster = "M"
mx= 1
my= 1
monsterhp = 10    
    
    
# --- view dungeon ---

#print(d)

d = generate_dungeon()
#d0 = d[:]

msg = ""
while True:
    
    #d[my][mx]="."
    dx=random.choice((-1,0,0,0,1))
    dy=random.choice((-1,0,0,0,1))
    if d[my+dy][mx+dx] == "#":
        dx=0
        dy=0
        msg += "Monster autsch"
    mx += dx
    my += dy
    #d[my][mx]="M"

    for y, line in enumerate(d):
        for x, char in enumerate(line):
            if x==herox and y==heroy:
                print(hero, end="")
            elif x==mx and y==my:
                print(monster, end="")
            else:
                print(char, end="")
        print()
        
    #y=int(input("y  >>>"))
    #x=int(input("x  >>>"))
    #print(d[y][x])
    print(msg)
    msg = ""
    c = input("type command and ENTER, ? for help >>>")
    dx = 0
    dy = 0
    if c == "q":
        break
    if c == "?":
        msg = helptext
    if c == " ":
        d = generate_dungeon()
        continue
    if c == "a":
        dx = -1
        #herox-=1
    if c == "d":
        dx = 1
        #herox+=1
    if c == "w":
        dy = -1
        # heroy-=1
    if c == "s":
        dy = 1
        # heroy+=1
    # # ----- walltest -----
    if d[heroy+dy][herox+dx] == "#":
        dx = 0
        dy = 0
        msg="Autsch eine Wand"
    herox += dx
    heroy += dy
