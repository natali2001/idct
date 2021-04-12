import qrcode
from tkinter import*

me = Tk()
me.geometry("345x200")
me.title("QR Code")
melabel = Label(me, text="Input your text in field below", bg='White', font=("Times", 16, 'bold'))
melabel.pack(side = TOP)
me.config(background='black')

textin=StringVar()

def generate():
    First_qrcode=qrcode.make(textin.get())
    First_qrcode.show()


metext=Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='white')
metext.place(x=50, y=80)

btngenerate=Button(me, text='Generate', font=('arial', 12, 'bold'), width=24, bd=4, command=generate)
btngenerate.place(x=50, y=120)

me.mainloop()
