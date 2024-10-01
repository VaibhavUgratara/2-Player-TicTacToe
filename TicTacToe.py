from tkinter import *
p1=""
p2=""
c=0
table=["-","-","-","-","-","-","-","-","-"]
k=True
def recover():
    global p1,p2,c,table,k
    p1=""
    p2=""
    c=0
    table=["-","-","-","-","-","-","-","-","-"]
    k=True
    p_c1.config(text="Player One: ")
    p_c2.config(text="")
    box0.config(text="")
    box1.config(text="")
    box2.config(text="")
    box3.config(text="")
    box4.config(text="")
    box5.config(text="")
    box6.config(text="")
    box7.config(text="")
    box8.config(text="")
    f4.forget()
    b1.grid(row=0,column=1)
    fl1.grid(row=0,column=3)
    b2.grid(row=0,column=5)
    f5.config(text="")
    f5.forget()
    f6.forget()
def qu():
    root.destroy()
def rcheck():
    global table,k
    for i in [0,3,6]:
        if table[i]==table[i+1]==table[i+2]!="-":
            if(c%2!=0):
                f5.config(text="Player One Won!!")
            else:
                f5.config(text="Player Two Won!!")
            k=False
            break;
def ccheck():
    global table,k
    for i in [0,1,2]:
        if table[i]==table[i+3]==table[i+6]!="-":
            if(c%2!=0):
                f5.config(text="Player One Won!!")
            else:
                f5.config(text="Player Two Won!!")
            k=False
            break;
def dcheck():
    global k,table
    if (table[0]==table[4]==table[8]!="-") or (table[2]==table[4]==table[6]!="-"):
        if(c%2!=0):
            f5.config(text="Player One Won!!")
        else:
            f5.config(text="Player Two Won!!")
        k=False
def play():
    rcheck()
    ccheck()
    dcheck()
    if("-" not in table):
        f5.config(text="Match Draw!!")
def choice(n):
    global p1,p2
    if(n=="X"):
        p1="X"
        p2="O"
    else:
        p1="O"
        p2="X"
    b1.grid_forget()
    b2.grid_forget()
    fl1.grid_forget()
    p_c1.config(text=f"Player One: {p1}")
    p_c2.config(text=f"Player Two: {p2}")
    f4.pack()
    f5.pack()
    f6.pack()
def w(n):
    global p1,p2,c,table,k
    if c%2==0 and n["text"]=="" and k==True:
        n.config(text=p1)
        c+=1
        j=n["text"]
        i=b_l.index(n)
        table[i]=j
        play()
    elif n["text"]=="" and k==True:
        n.config(text=p2)
        c+=1
        j=n["text"]
        i=b_l.index(n)
        table[i]=j
        play()
root=Tk()
root.title("2-Player Tic tac toe")
root.geometry("500x500")
root.configure(bg="skyblue")
f1=Frame(root)
f1.pack()
l1=Label(f1,text="2-Player Tic Tac Toe",font="Verdana 20 bold",fg="Gold",bg="skyblue")
l1.pack()
f3=Frame(root)
f3.pack()
l2=Label(f3,text=" ",bg="skyblue")
l2.pack()
f2=Frame(root,bg="skyblue")
f2.pack()
p_c1=Label(f2,text="Player One: ",bg="skyblue")
p_c1.grid(row=0,column=0)
b1=Button(f2,text="X",width=12,height=3,borderwidth=4,relief=RIDGE,command= lambda:choice("X"))
b1.grid(row=0,column=1)
b2=Button(f2,text="O",width=12,height=3,borderwidth=4,relief=RIDGE,command= lambda:choice("O"))
b2.grid(row=0,column=5)
fl1=Label(f2,text="or",bg="skyblue")
fl1.grid(row=0,column=3)
fl2=Label(f2,text=" ",bg="skyblue")
fl2.grid(row=0,column=2)
fl3=Label(f2,text=" ",bg="skyblue")
fl3.grid(row=0,column=4)
p_c2=Label(f2,text=" ",bg="skyblue")
p_c2.grid(row=1,column=0)
f4=Frame(root)
box0=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box0.bind("<Button-1>",lambda e: w(box0))
box0.grid(row=0,column=0)
box1=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box1.bind("<Button-1>",lambda e: w(box1))
box1.grid(row=0,column=1)
box2=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box2.bind("<Button-1>",lambda e: w(box2))
box2.grid(row=0,column=2)
box3=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box3.bind("<Button-1>",lambda e: w(box3))
box3.grid(row=1,column=0)
box4=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box4.bind("<Button-1>",lambda e: w(box4))
box4.grid(row=1,column=1)
box5=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box5.bind("<Button-1>",lambda e: w(box5))
box5.grid(row=1,column=2)
box6=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box6.bind("<Button-1>",lambda e: w(box6))
box6.grid(row=2,column=0)
box7=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box7.bind("<Button-1>",lambda e: w(box7))
box7.grid(row=2,column=1)
box8=Label(f4,text="",highlightbackground="black",highlightthickness=2,height=5,width=10)
box8.bind("<Button-1>",lambda e: w(box8))
box8.grid(row=2,column=2)
f5=Label(root,text="",bg="skyblue")
f6=Frame(root,bg="skyblue")
re_start=Button(f6,text="Restart",command=recover)
d=Button(f6,text="Quit",command=qu)
re_start.pack()
d.pack()
re_start=Button(f6,text="Restart",command=recover)
b_l=[box0,box1,box2,box3,box4,box5,box6,box7,box8]
root.mainloop()
