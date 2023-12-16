import tkinter as tk

pencere = tk.Tk()
pencere.config(bg="#888")
pencere.title("Number")
pencere.geometry("280x500")
pencere.maxsize(width=280,height=500)
pencere.minsize(width=280,height=500)

tus_takimi_frame= tk.Frame()
tus_takimi_frame.config(bg="#222")
goster_frame = tk.Frame()
goster_frame.config(bg="#888")
islem_etiket = tk.Label(master=goster_frame,bg="#777",fg="#fff",width=7,height=2,font=("Arial",16))
etiket = tk.Label(master=goster_frame,bg="#888",fg="#fff",width=9,font=("Arial",26))
islem_etiket.pack(side=tk.LEFT)
etiket.pack(side=tk.LEFT)
sonuc_frame = tk.Frame()
sonuc_frame.config(bg="#000")
sonuc = tk.Label(master=sonuc_frame,bg="#000",fg="#fff",width=23,font=("new times roman",16))
sonuc.pack()

# 10 :  backspace
# 11 : heximal
# 12 :  decimal
# 13 : octal
# 14 : binary

def hesap(index,frm,to):
    snc = []
    if to == "16":
        try:
            snc.append(hex(int(index,frm))[2:])
        except ValueError:
            etiket["text"] = "ERROR"
    elif to == "10":
        try:
            snc.append(int(index,frm))
        except ValueError:
            etiket["text"] = "ERROR"
    if to == "8":
        try:
            snc.append(oct(int(index,frm))[2:])
        except ValueError:
            etiket["text"] = "ERROR"
    if to == "2":
        try:
            snc.append(bin(int(index,frm))[2:])
        except ValueError:
            etiket["text"] = "ERROR"
    sonuc["text"] = snc

def islem(sayi):
    if sayi == 11:
        if islem_etiket["text"] == "":
            islem_etiket["text"] += "16"
        elif islem_etiket["text"].count(">") == 1 and len(islem_etiket["text"])<=5:
            islem_etiket["text"] += "16"
    elif sayi == 12:
        if islem_etiket["text"] == "":
            islem_etiket["text"] += "10"
        elif islem_etiket["text"].count(">") == 1 and len(islem_etiket["text"])<=5:
            islem_etiket["text"] += "10"    
    elif sayi == 13:
        if islem_etiket["text"] == "":
            islem_etiket["text"] += "8"
        elif islem_etiket["text"].count(">") == 1 and len(islem_etiket["text"])<=5:
            islem_etiket["text"] += "8"    
    elif sayi == 14:
        if islem_etiket["text"] == "":
            islem_etiket["text"] += "2"
        elif islem_etiket["text"].count(">") == 1 and len(islem_etiket["text"])<=5:
            islem_etiket["text"] += "2"
    elif sayi == 16:
        if islem_etiket["text"] != "" and islem_etiket["text"].count(">") == 0:
            islem_etiket["text"] += " -> "
    elif sayi == 17:
        if etiket["text"]:
            index = etiket["text"]
            frm = islem_etiket["text"].split(" -> ")[0]
            to = islem_etiket["text"].split(" -> ")[1]
            hesap(index,int(frm),to)
        else:
            pass

def yaz(sayi):
    etiket_text = etiket["text"]
    if sayi == 10:
        if etiket_text:
            etiket["text"] = etiket_text[:-1]
    elif sayi == 15:
        etiket["text"] = ""
        islem_etiket["text"] = ""
        sonuc["text"] = ""
    else:
        if sayi in ["a","b","c","d","e","f"]:
            islem(11)
        etiket["text"] += str(sayi)
    

tus1 = tk.Button(text=1 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(1)).grid(column=0,row=1)
tus2 = tk.Button(text=2 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(2)).grid(column=1,row=1)
tus3 = tk.Button(text=3 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(3)).grid(column=2,row=1)

tus4 = tk.Button(text=4 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(4)).grid(column=0,row=2)
tus5 = tk.Button(text=5 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(5)).grid(column=1,row=2)
tus6 = tk.Button(text=6 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(6)).grid(column=2,row=2)

tus7 = tk.Button(text=7 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(7)).grid(column=0,row=3)
tus8 = tk.Button(text=8 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(8)).grid(column=1,row=3)
tus9 = tk.Button(text=9 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(9)).grid(column=2,row=3)
tus0 = tk.Button(text=0 ,master=tus_takimi_frame, width=3,bg="#222",fg="#ddd", font=("Arial",26), command= lambda: yaz(0)).grid(row=4,column=0)

a = tk.Button(text="a" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("a")).grid(row=4,column=1)
b = tk.Button(text="b" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("b")).grid(row=4,column=2)
c = tk.Button(text="c" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("c")).grid(row=4,column=3)
d = tk.Button(text="d" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("d")).grid(row=5,column=0)
e = tk.Button(text="e" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("e")).grid(row=5,column=1)
f = tk.Button(text="f" ,master=tus_takimi_frame, width=3,bg="#1a1a1a",fg="#ddd", font=("Arial",26), command= lambda: yaz("f")).grid(row=5,column=2)


tus_sil = tk.Button(text="←" ,master=tus_takimi_frame, width=3,bg="#a22",fg="#ddd", font=("Arial",26), command= lambda: yaz(10)).grid(row=1,column=3)
tus_cls = tk.Button(text="cls" ,master=tus_takimi_frame, width=3,bg="#a22",fg="#ddd", font=("Arial",26), command= lambda: yaz(15)).grid(row=2,column=3)

he = tk.Button(text="(16)" ,master=tus_takimi_frame, width=3,bg="#d72",fg="#222", font=("Arial",26), command= lambda: islem(11)).grid(row=0,column=0)
de = tk.Button(text="(10)" ,master=tus_takimi_frame, width=3,bg="#d72",fg="#222", font=("Arial",26), command= lambda: islem(12)).grid(row=0,column=1)
ok = tk.Button(text="(8)" ,master=tus_takimi_frame, width=3,  bg="#d72",fg="#222", font=("Arial",26), command= lambda: islem(13)).grid( row=0,column=2)
bi = tk.Button(text="(2)" ,master=tus_takimi_frame, width=3, bg="#d72",fg="#222", font=("Arial",26), command= lambda: islem(14)).grid( row=0,column=3)

to = tk.Button(text="->" ,master=tus_takimi_frame, width=3, bg="#444",fg="#fff", font=("Arial",26), command= lambda: islem(16)).grid( row=3,column=3)
go = tk.Button(text="=" ,master=tus_takimi_frame, width=3,  bg="#444",fg="#fff", font=("Arial",26), command= lambda: islem(17)).grid( row=5,column=3)

goster_frame.pack()
tus_takimi_frame.pack()
sonuc_frame.pack()

pencere.mainloop()
