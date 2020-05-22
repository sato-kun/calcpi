import tkinter as tk
PI = 3.14

def enntyuu(hankei,takasa):
    taiseki = hankei * hankei * PI * takasa
    return taiseki

def displbl(hankei, takasa, lbl):
    lbl.configure(text=enntyuu(hankei, takasa))

def createEntry(txtprop, lblprop):
    txt = tk.Entry(width = txtprop['width'])
    txt.place(x = txtprop['x'], y = txtprop['y'])
    lbl = tk.Label(text = lblprop['text'])
    lbl.place(x = lblprop['x'], y = lblprop['y'])
    return txt, lbl

def getTextVal(target):
    try:
    	float(target.get())
    except:
    	return 0
    return float(target.get()) 

root = tk.Tk()
root.geometry("300x200")

hankeitextprop = {'width': 20, 'x': 90, 'y': 70}
hankeilabelprop = {'text': '半径', 'x': 30, 'y': 70}
hankeitext,hankeilabel = createEntry(hankeitextprop, hankeilabelprop)

takasatextprop = {'width': 20, 'x': 90, 'y': 90}
takasalabelprop = {'text': '高さ', 'x': 30, 'y': 90}
takasatext,takasalabel = createEntry(takasatextprop, takasalabelprop)

lbl = tk.Label(text = "Enter")
btn = tk.Button(text = "PUSH", command = lambda: displbl(getTextVal(hankeitext), getTextVal(takasatext), lbl))

lbl.pack()
btn.pack()
tk.mainloop()
