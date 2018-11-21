import random


helptext = """
dungeon game move the hero with the keys w a s d
press space to create a new level
"""

maxlines=18
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
    # zufallsMonster
    for m in range(20):
        while True:
            x = random.randint(1,maxchars-2)
            y = random.randint(2,maxlines-2)
            if d[y][x]==".":
                for mo in Game.zoo:
                    if mo.x == x and mo.y == y:
                        break
                else:
                    print("erschaffe Monster Nummer", m)
                    Monster(x,y,0)
                    break
                    
    return d    

class Game():
    zoo=[]
    storage=[]

class Monster():
    number=0
    
    def __init__(self,x,y,z, char="M"):
        self.number=Monster.number
        Monster.number+=1
        Game.zoo.append(self)
        self.x=x
        self.y=y
        self.z=z
        self.char = char
        self.sniffrange=random.randint(5,10)
        self.hp=random.randint(10, 25)
        self.waffe=random.choice(("schwert", "axt", "keule"))
        self.gold=random.randint(5, 30)
        self.armor=random.choice(("hemd", "helm", "brustpanzer"))
        self.mood=random.choice(("agressive", "peacfull", "curious", "sleepy"))
        self.report()
        
    def ai(self, hero):
        distx=hero.x-self.x
        disty=hero.y-self.y
        dist = (distx**2+disty**2)**0.5
        if dist < self.sniffrange:
            if hero.x > self.x:
                dx = 1
            elif hero.x < self.x:
                dx = -1
            else:
                dx = 0
            if hero.y > self.y:
                dy = 1
            elif hero.y < self.y:
                dy = -1
            else:
                dy = 0
        else:
             dx = random.choice((-1,0,0,1))
             dy = random.choice((-1,0,0,1))
        return dx, dy
        
    def report(self):
        print("ich bin ein {} nummer {}".format(self.__class__.__name__,self.number))
        print("ich habe {} hp".format(self.hp))
        print("ich habe {}".format(self.waffe))
        print("ich habe {} gold".format(self.gold))
        print("ich habe {}".format(self.armor))
        print("ich bin {}".format(self.mood))



# --- generate hero

hero = Monster(1,1,0,"@")
#herox = 4
#heroy = 4
hero.hp = 200

# --- generate Monster
#print("rudi")
#rudi=Monster(0,0,0)
#rudi.report()

#print("detlef")
#detlef=Monster(2,2,2)
#detlef.report()

#monster = "M"
#mx= 1
#my= 1
#monsterhp = 10    
    
    
# --- view dungeon ---

#print(d)


d = generate_dungeon()
#d0 = d[:]

msg = ""
while True:
    
    #d[my][mx]="."
    #dx=random.choice((-1,0,0,0,1))
    #dy=random.choice((-1,0,0,0,1))
    #if d[my+dy][mx+dx] == "#":
    #    dx=0
    #    dy=0
    #    msg += "Monster autsch"
    #mx += dx
    #my += dy
    #d[my][mx]="M"

    for y, line in enumerate(d):
        for x, char in enumerate(line):
            #if x==herox and y==heroy:
            #    print(hero, end="")
            #elif x==mx and y==my:
            #    print(monster, end="")
            #else:
            #    print(char, end="")
            for mo in Game.zoo:
                if mo.x == x and mo.y == y:
                    print(mo.char, end="")
                    break
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
        msg += helptext
    #if c == " ":
    #    d = generate_dungeon()
    #    continue
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
    if d[hero.y+dy][hero.x+dx] == "#":
        dx = 0
        dy = 0
        msg+="\nAutsch eine Wand"
    hero.x += dx
    hero.y += dy
    #-------bewegung für Monster ------
    for mo in Game.zoo:
        if mo.number == 0:
            continue # hero hat sich schon bewegt
        dx, dy = mo.ai(hero)
        # test ob monster in wall läuft
        if d[mo.y + dy][mo.x + dx] == "#":
            #msg+="\nMonster nr {} wollte in Wand laufen".format(mo.number)
            dx, dy = 0,0
        # test ob monster in player läuft (Angriff)
        if mo.y + dy == hero.y and mo.x + dx == hero.x:
            dx, dy = 0, 0
            msg+="\nMonster nr {} wollte player angreifen".format(mo.number)
        # test ob monster in anderes monster läuft
        for mo2 in Game.zoo:
            if mo2.number == mo.number:
                continue
            if mo2.number == hero.number:
                continue
            if mo.y + dy == mo2.y and mo.x + dx == mo2.x:
                #msg+="\nMonster nr {} wollte in Monster nr {} laufen".format(mo.number, mo2.number)
                dx, dy = 0, 0
        mo.x += dx
        mo.y += dy
