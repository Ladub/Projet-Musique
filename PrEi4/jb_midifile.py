
#sudo pip install python-rtmidi (windows/mac)
import mido
from mido import MidiFile
mido.set_backend('mido.backends.rtmidi')
out_names=mido.get_output_names()
print(out_names)
outport = mido.open_output(out_names[0])


for msg in MidiFile('SweetHomeAlabama.mid').play():
    print(msg)
    outport.send(msg)
