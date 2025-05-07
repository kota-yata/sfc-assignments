from tkinter import *

window = Tk()   
window.geometry("600x600")   
window.attributes("-topmost", True)
window.title("Sample Window")

canvas = Canvas(window, width=600, height=600, background="white")

size = 13
edge, gap = 30, 4
for n in range(1, size+1):
    for m in range(1, size+1):
        if abs(m-n) <= size//2 and abs(m+n-size-1) <= size//2:
            canvas.create_rectangle(m*edge, n*edge, (m+1)*edge-gap, (n+1)*edge-gap)
canvas.pack()
mainloop()
