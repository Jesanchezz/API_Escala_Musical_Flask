__author__ = 'Frodo'

class MusicalScale:

    def accommodate_scale(self, musical_scale, index):
        if index == 0:
          return musical_scale
        else:
            slice = musical_scale[0:index]

            for note in slice:
                if note in musical_scale:
                    musical_scale.remove(note)
                for note in slice:
                    if note not in musical_scale:
                        musical_scale.append(note)

        return musical_scale


    def create_major_scale(self, accommodated_scale):
        new_major_scale = []

        for i in range(len(accommodated_scale)):
            if (i%2==0 and i<=4):
                new_major_scale.append(accommodated_scale[i])
            elif (i%2!=0 and i>4):
                new_major_scale.append(accommodated_scale[i])

        return new_major_scale


    def create_minor_scale(self, accommodated_scale):
        new_minor_scale =[]

        for i in range(len(accommodated_scale)):
            if i==0 or i==2:
                new_minor_scale.append(accommodated_scale[i])
            elif i%2!=0 and i>=3 and i<8:
                new_minor_scale.append(accommodated_scale[i])
            elif i%2==0 and i>=8:
                new_minor_scale.append(accommodated_scale[i])

        return new_minor_scale


    def create_major_pentatonic_scale(self, musical_major_scale):
        major_pentatonic_scale = musical_major_scale
        major_pentatonic_scale.pop(6)
        major_pentatonic_scale.pop(3)
     
        return major_pentatonic_scale


    def create_minor_pentatonic_scale(self, musical_minor_scale):
        minor_pentatonic_scale = musical_minor_scale
        minor_pentatonic_scale.pop(5)
        minor_pentatonic_scale.pop(1)
        
        return minor_pentatonic_scale


    def create_major_blues_scale(self, musical_scale, major_pentatonic_scale):
        #Nota bemolizada, entre el segundo y tercer grado
        previous_note = major_pentatonic_scale[1]
        index = musical_scale.index(previous_note)
        blues_note = musical_scale[index+1]
        major_blues_scale = major_pentatonic_scale
        major_blues_scale.insert(2, blues_note)
        
        return major_blues_scale


    def create_minor_blues_scale(self, musical_scale, minor_pentatonic_scale):
        #Nota bemolizada, entre el tercer y cuarto grado
        previous_note = minor_pentatonic_scale[2]
        index = musical_scale.index(previous_note)
        blues_note = musical_scale[index+1]
        minor_blues_scale = minor_pentatonic_scale
        minor_blues_scale.insert(3, blues_note)
       
        return minor_blues_scale