import tkinter
import re
from polyglot import Polyglot

root = tkinter.Tk()
root.title("Polyglot")
root.geometry("430x180")
root.configure(bg = "black")
xlist = []

def step():
    btn1["text"] = "next"
    if ent.get() == "":
        p = Polyglot()
        po = p.load()
        lbl1.configure(text = po[0][1])
        lbl2.configure(text = " ".join(po[1]))
        lbl3.configure(text = "")
        lbl4.configure(text = "")
        xlist.append(po)
    else:
        count = 0
        tr = ent.get()
        wl = re.split("[\s]", tr)
        fp = xlist[-1]
        sp = fp[0][0]
        pol = re.split("[\s]", sp)
        for i, j in zip(wl, pol):
            if i == j:
                count += 1
        if len(pol) == count:
            lbl3.configure(text = " ".join(pol))
            lbl4.configure(text = "Good!")
        else:
            txt = "right answer: " + " ".join(pol)
            lbl3.configure(text = tr)
            lbl4.configure(text = txt)
        ent.delete(0, "end")

lbl1 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl2 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl3 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl4 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "enter", bg = "gray", command = step)
btn1["text"] = "start"

lbl1.place(x = 45, y = 20)
lbl2.place(x = 45, y = 40)
lbl3.place(x = 45, y = 60)
lbl4.place(x = 45, y = 80)
ent.place(x = 15, y = 100 )
btn1.place(x = 350, y = 96)

if __name__ == "__main__":
    root.mainloop()
