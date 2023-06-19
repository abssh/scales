
# notes
notes =["A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#"]


class Scale:
    def __init__(self, method) -> None:
        self.method = method
        pass

    def genarate_scale(self, starting_note):
        s = [starting_note]

        zero = notes.index(starting_note)
        # self.method = (2,2,1,2,2,2,1)
        for step in self.method:
            zero = self.next(zero, step) 
            s.append(notes[zero])
        
        return s



        
    @staticmethod
    def next(num, step) -> int:
        return (num+step)%12




