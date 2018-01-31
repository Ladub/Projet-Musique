#JB Fasquel
import tkinter as tk


############
# MIDI part
import mido,time
print(mido.get_output_names())
out_names=mido.get_output_names()
outport = mido.open_output(out_names[0])

############alex
# PLAY
def play():
    chaine=saisie.get(1.0, tk.END)
    #TODO: use a thread
    for i in chaine:
        outport.send(mido.Message('note_on', channel=0, note=ord(i), velocity=100, time=0))
        time.sleep(0.1)

    #saisie.delete(1.0, tk.END)

############
# GUI part
mainwindow=tk.Tk()
saisie=tk.Text(mainwindow)
saisie.grid(row=0,column=0)
button=tk.Button(mainwindow,text="PLAY TEXT", command=play)
button.grid(row=1,column=0)
#saisie.insert(tk.END, "hello, ")
mainwindow.mainloop()
