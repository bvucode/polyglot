import random
import re
import json

listforhelp = ["i you he she we they",
               "me him her us them",
               "am are is",
               "be was were",
               "have has had",
               "will, not, shall",
               "do doesn't did't did does",
               "this that their",
               "what who where when why how"]

with open("data.json", "r") as file:
    data = json.load(file)

class Polyglot:
    def _init__(self):
        pass
    def load(self):
        xlist = []
        tlist = []
        engvar = ""
        ruvar = ""
        engvar, ruvar = random.choice(list(data.items()))
        xlist.append(engvar)
        xlist.append(ruvar)
        ispl = re.split("\s", engvar)
        for i in ispl:
            for j in listforhelp:
                x = j.split(" ")
                if i in x:
                    c = 2
                    tlist.append(i)
                    while c > 0:
                        y = random.choice(x)
                        if y not in tlist:
                            tlist.append(y)
                            c -= 1
        return xlist, tlist

if __name__ == "__main__":
    while True:
        p = Polyglot()
        po = p.load()
        print(po[0][1])
        print(" ".join(po[1]))
        count = 0
        inp = input("text: ")
        wl = re.split("[\s]", inp)
        pol = re.split("[\s]", po[0][0])
        for i, j in zip(wl, pol):
            if i == j:
                count += 1
        if len(pol) == count:
            print(" ".join(pol))
            print("Good!\n")
        else:
            print("right answer: " + " ".join(pol) +"\n")
