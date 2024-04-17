import music21
from music21 import stream, midi
from music21 import converter
import numpy as np

class S1987:
    def __init__(self, lilypondPath, yourfilepath):
        self.lilypondPath = lilypondPath
        self.yourfilepath = yourfilepath
    def __str__(self):
        return """Music Variation Maker V.1: Work on progress (0 ^ 0)
        This package is building for piano user only.
        Function in this package
        1.
        
        """
    def note_converter(self, midi_note):
        """
        This function convert single midi note value to readable musical note.
        Important parameter:
        midi_note: midi note value;
                   60 ----> C4
                   
        """
        if midi_note == '<REST>':
            return '<REST>'
        else:
            if 0 <= midi_note <= 127:
                pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

                octave = (midi_note // 12) - 1
                pitch_index = midi_note % 12

                pitch = pitches[pitch_index]
                return f"{pitch}{octave}"
            else:
                return "Invalid MIDI note value. Must be between 0 and 127."
    def le(self, t, xyz, *args, **kwargs):
        """
        ********************************************************************************
        "I didn't have any knowledge about Chaotic System" you say,
        Nah Just use this one and change to any chaotic system you want later.
        Chaotic Trajectory parameter:
        d: 10 
        r: 28 
        b: 8/3 
        ********************************************************************************
        !!! This function relate with rk4 !!!
        """
        d, r, b = kwargs['d'], kwargs['r'], kwargs['b']
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        xdot = d*(y - x)
        ydot = x*(r - z) - y
        zdot = x*y - b*z
        return np.array([xdot, ydot, zdot])
    def rk4(self, time=None, ini=None, f=le, h=0.01, *args, **kwargs):
        """
        ********************************************************************************
        This function can approximate solution of Chaotic system, but this version
        isn't support import new chaotic solution from outsource.
        Important parameter:
        time: The list of time you want from start to finish;
              [0, 40] ---> (start, end)
        ini: The seed for trajectory;
             np.array([1,1,1]) ----> [x, y, z]
        h:   step size;
             0.01, 0.001, 0.0001
        ********************************************************************************
        !!! This function relate with music_variation_generator !!!
        """
        t = np.arange(time[0], time[1]+h, h)
        row = len(t)
        try:
            var = len(ini)
        except TypeError:
            var = 1
        x = np.zeros((row, var))
        x[0, :] = ini
        for j in range(0, len(t)-1):
            k1 = f(self, t[j], x[j], *args, **kwargs)
            k2 = f(self, t[j] + 0.5*h, x[j] +0.5*h*k1, *args, **kwargs)
            k3 = f(self, t[j] + 0.5*h, x[j] + 0.5*h*k2, *args, **kwargs)
            k4 = f(self, t[j] + h, x[j] + h*k3, *args, **kwargs)
            x[j+1, :] = x[j] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        return t, x
    def midi2pdfmidi(self, seed1=None, seed2=None, T=None, 
                     d=None, r=None, b=None,
                     approxsol=rk4, convert_single_note=note_converter, trajstyle=None,
                     third_hand=False, th_trajstyle=None, 
                     midiname=None, origin_name=None, new_name=None, 
                     *args, **kwargs):
        time, xyz = approxsol(self, time=T, ini=seed1, d=d, r=r, b=b, *args, **kwargs)
        x = xyz[:, 0]
        y = xyz[:, 1]
        z = xyz[:, 2]
        new_time, new_xyz = approxsol(self, time=T, ini=seed2, d=d, r=r, b=b, *args, **kwargs)
        new_x = new_xyz[:, 0]
        new_y = new_xyz[:, 1]
        new_z = new_xyz[:, 2]
        
        mf = midi.MidiFile()
        mf.open(midiname)
        mf.read()
        mf.close()
        s = midi.translate.midiFileToStream(mf)
        ss = midi.translate.midiFileToStream(mf)
        s1 = s[0]
        s2 = s[1]
        
        Melody_Chord_list1 = []
        Duration_list1 = []
        for part in s1:
            for n in part.flat.notesAndRests:
                if n.isRest:
                    dur = n.duration.quarterLength
                    note_num = "<REST>"
                    Melody_Chord_list1.append(note_num)
                    Duration_list1.append(dur)
                else:
                    dur = n.duration.quarterLength
                    if len(n.pitches) == 1:
                        note_num = n.pitches[0].midi
                        Melody_Chord_list1.append(note_num)
                        Duration_list1.append(dur)
                    else: 
                        note_num = sorted(set([p.midi for p in n.pitches]))
                        Melody_Chord_list1.append(list(note_num))
                        Duration_list1.append(dur)
                        
        Melody_Chord_list2 = []
        Duration_list2 = []
        for part in s2:
            for n in part.flat.notesAndRests:
                if n.isRest:
                    dur = n.duration.quarterLength
                    note_num = "<REST>"
                    Melody_Chord_list2.append(note_num)
                    Duration_list2.append(dur)
                else:
                    dur = n.duration.quarterLength
                    if len(n.pitches) == 1:
                        note_num = n.pitches[0].midi
                        Melody_Chord_list2.append(note_num)
                        Duration_list2.append(dur)
                    else: 
                        note_num = sorted(set([p.midi for p in n.pitches]))
                        Melody_Chord_list2.append(list(note_num))
                        Duration_list2.append(dur)
        
        STR_Melody_Chord_list1 = Melody_Chord_list1
        for i in range(len(Melody_Chord_list1)):
            try:
                STR_Melody_Chord_list1[i] = convert_single_note(self, Melody_Chord_list1[i])
            except TypeError:
                for j in range(len(Melody_Chord_list1[i])):
                    STR_Melody_Chord_list1[i][j] = convert_single_note(self, Melody_Chord_list1[i][j])
                    
        STR_Melody_Chord_list2 = Melody_Chord_list2
        for i in range(len(Melody_Chord_list2)):
            try:
                STR_Melody_Chord_list2[i] = convert_single_note(self, Melody_Chord_list2[i])
            except TypeError:
                for j in range(len(Melody_Chord_list2[i])):
                    STR_Melody_Chord_list2[i][j] = convert_single_note(self, Melody_Chord_list2[i][j])
        
        if trajstyle == 'x':
            Criteria_Melody_Chord_list1 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))] 
        elif trajstyle == 'xy':        
            Criteria_Melody_Chord_list1 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_y[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'xz':        
            Criteria_Melody_Chord_list1 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
            
        elif trajstyle == 'y':
            Criteria_Melody_Chord_list1 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_y[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_y[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'yx':
            Criteria_Melody_Chord_list1 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_y[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'yz':
            Criteria_Melody_Chord_list1 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'z':
            Criteria_Melody_Chord_list1 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'zx':
            Criteria_Melody_Chord_list1 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           x[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_x[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        elif trajstyle == 'zy':
            Criteria_Melody_Chord_list1 = [[index, 
                                           z[::5][index], 
                                           STR_Melody_Chord_list1[index]] 
                                          for index in range(len(STR_Melody_Chord_list1))]
            New_Melody_Chord_list1 = [[index, 
                                      new_z[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list1))]

            Criteria_Melody_Chord_list2 = [[index, 
                                           y[::5][index], 
                                           STR_Melody_Chord_list2[index]] 
                                          for index in range(len(STR_Melody_Chord_list2))]
            New_Melody_Chord_list2 = [[index, 
                                      new_y[::5][index]]
                                     for index in range(len(STR_Melody_Chord_list2))]
        
        Sorted_Criteria_Melody_Chord_list1 = sorted(Criteria_Melody_Chord_list1, key=lambda x: x[1])
        Sorted_Criteria_Melody_Chord_list2 = sorted(Criteria_Melody_Chord_list2, key=lambda x: x[1])
        
        biindex1 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list1)/2), 
                                     int(len(Sorted_Criteria_Melody_Chord_list1)/2))]
        biindex2 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list2)/2), 
                                     int(len(Sorted_Criteria_Melody_Chord_list2)/2))]
        if len(Criteria_Melody_Chord_list1) != len(biindex1):
            biindex1 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list1)/2), 
                                         int(len(Sorted_Criteria_Melody_Chord_list1)/2) + 1)]
        if len(Criteria_Melody_Chord_list2) != len(biindex2):
            biindex2 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list2)/2), 
                                         int(len(Sorted_Criteria_Melody_Chord_list2)/2) + 1)]
        
        Criteria_Melody_Chord_list1 = [[biindex1[index], 
                                        Sorted_Criteria_Melody_Chord_list1[index][1], 
                                        Sorted_Criteria_Melody_Chord_list1[index][2]] 
                                       for index in range(len(Sorted_Criteria_Melody_Chord_list1))]
        Criteria_Melody_Chord_list2 = [[biindex2[index], 
                                        Sorted_Criteria_Melody_Chord_list2[index][1], 
                                        Sorted_Criteria_Melody_Chord_list2[index][2]] 
                                       for index in range(len(Sorted_Criteria_Melody_Chord_list2))]
        
        Result1 = [None]*len(Criteria_Melody_Chord_list1)
        for mc in range(len(New_Melody_Chord_list1)):
            for smml in range(len(Criteria_Melody_Chord_list1)):
                if (New_Melody_Chord_list1[mc][1] < (Criteria_Melody_Chord_list1[smml][1] + Criteria_Melody_Chord_list1[smml - 1][1])/2) and (smml > 0):
                    target_value = Criteria_Melody_Chord_list1[smml][0] - 1
                    Result1[mc] = target_value
                    break
                elif (New_Melody_Chord_list1[mc][1] < Criteria_Melody_Chord_list1[smml][1]) and (smml == 0):
                    target_value = Criteria_Melody_Chord_list1[smml][0] - 1
                    Result1[mc] = target_value
        Result2 = [None]*len(Criteria_Melody_Chord_list2)
        for mc in range(len(New_Melody_Chord_list2)):
            for smml in range(len(Criteria_Melody_Chord_list2)):
                if (New_Melody_Chord_list2[mc][1] < (Criteria_Melody_Chord_list2[smml][1] + Criteria_Melody_Chord_list2[smml - 1][1])/2) and (smml > 0):
                    target_value = Criteria_Melody_Chord_list2[smml][0] - 1
                    Result2[mc] = target_value
                    break
                elif New_Melody_Chord_list2[mc][1] < Criteria_Melody_Chord_list2[smml][1] and (smml == 0):
                    target_value = Criteria_Melody_Chord_list2[smml][0] - 1
                    Result2[mc] = target_value
                    break
        
        for check in range(len(Result1)):
            if (Result1[check] == None) and (New_Melody_Chord_list1[check][1] >= Criteria_Melody_Chord_list1[check][1]):
                Result1[check] = max(Criteria_Melody_Chord_list1)[0]
            elif (Result1[check] == None) and (New_Melody_Chord_list1[check][1] <= Criteria_Melody_Chord_list1[check][1]):
                Result1[check] = min(Criteria_Melody_Chord_list1)[0]
        for check in range(len(Result2)):
            if (Result2[check] == None) and (New_Melody_Chord_list2[check][1] >= Criteria_Melody_Chord_list2[check][1]):
                Result2[check] = max(Criteria_Melody_Chord_list2)[0]
            elif (Result2[check] == None) and (New_Melody_Chord_list2[check][1] <= Criteria_Melody_Chord_list2[check][1]):
                Result2[check] = min(Criteria_Melody_Chord_list2)[0]
                
        Result1 = [element + int(len(Sorted_Criteria_Melody_Chord_list1)/2) for element in Result1]
        Result2 = [element + int(len(Sorted_Criteria_Melody_Chord_list2)/2) for element in Result2]
        
        NV_Melody_Chord_list1 = [Criteria_Melody_Chord_list1[rindex][2] for rindex in Result1]
        NV_Melody_Chord_list2 = [Criteria_Melody_Chord_list2[rindex][2] for rindex in Result2]
        
        replacement_list1 = NV_Melody_Chord_list1
        replacement_list2 = NV_Melody_Chord_list2
        
        index1 = 0
        for element in ss[0].recurse():
            if isinstance(element, (music21.note.Note, music21.chord.Chord, music21.note.Rest)):
                replacement1 = replacement_list1[index1]
                duration_value1 = Duration_list1[index1]
                if replacement1 == '<REST>':
                    # If the replacement is '<REST>', replace with a rest
                    new_element = music21.note.Rest()
                elif isinstance(replacement1, list):
                    # If the replacement is a chord, create a chord object
                    new_element = music21.chord.Chord(replacement1)
                else:
                    # If the replacement is a note, create a note object
                    new_element = music21.note.Note(replacement1)

                # Set the duration for the new element
                new_element.duration = music21.duration.Duration(duration_value1)
                # Replace the old element with the new element
                element.activeSite.replace(element, new_element)

                index1 += 1
        index2 = 0
        for element in ss[1].recurse():
            if isinstance(element, (music21.note.Note, music21.chord.Chord, music21.note.Rest)):
                replacement2 = replacement_list2[index2]
                duration_value2 = Duration_list2[index2]
                if replacement2 == '<REST>':
                    # If the replacement is '<REST>', replace with a rest
                    new_element = music21.note.Rest()
                elif isinstance(replacement2, list):
                    # If the replacement is a chord, create a chord object
                    new_element = music21.chord.Chord(replacement2)
                else:
                    # If the replacement is a note, create a note object
                    new_element = music21.note.Note(replacement2)

                # Set the duration for the new element
                new_element.duration = music21.duration.Duration(duration_value2)
                # Replace the old element with the new element
                element.activeSite.replace(element, new_element)

                index2 += 1
        ##############################################################################################
        # Third_hand option section ... 
        #############################################################################################
        if third_hand == True:
            s3 = s[2]
            Melody_Chord_list3 = []
            Duration_list3 = []
            for part in s3:
                for n in part.flat.notesAndRests:
                    if n.isRest:
                        dur = n.duration.quarterLength
                        note_num = "<REST>"
                        Melody_Chord_list3.append(note_num)
                        Duration_list3.append(dur)
                    else:
                        dur = n.duration.quarterLength
                        if len(n.pitches) == 1:
                            note_num = n.pitches[0].midi
                            Melody_Chord_list3.append(note_num)
                            Duration_list3.append(dur)
                        else: 
                            note_num = sorted(set([p.midi for p in n.pitches]))
                            Melody_Chord_list3.append(list(note_num))
                            Duration_list3.append(dur)
            
            STR_Melody_Chord_list3 = Melody_Chord_list3
            for i in range(len(Melody_Chord_list3)):
                try:
                    STR_Melody_Chord_list3[i] = convert_single_note(self, Melody_Chord_list3[i])
                except TypeError:
                    for j in range(len(Melody_Chord_list3[i])):
                        STR_Melody_Chord_list3[i][j] = convert_single_note(self, Melody_Chord_list3[i][j])
            if th_trajstyle == 'x':
                Criteria_Melody_Chord_list3 = [[index, 
                                                x[::5][index], 
                                                STR_Melody_Chord_list3[index]] 
                                               for index in range(len(STR_Melody_Chord_list3))]
                New_Melody_Chord_list3 = [[index, 
                                           new_x[::5][index]]
                                          for index in range(len(STR_Melody_Chord_list3))]
            elif th_trajstyle == 'y':
                Criteria_Melody_Chord_list3 = [[index, 
                                                y[::5][index], 
                                                STR_Melody_Chord_list3[index]] 
                                               for index in range(len(STR_Melody_Chord_list3))]
                New_Melody_Chord_list3 = [[index, 
                                           new_y[::5][index]]
                                          for index in range(len(STR_Melody_Chord_list3))]
            elif th_trajstyle == 'z':
                Criteria_Melody_Chord_list3 = [[index, 
                                                z[::5][index], 
                                                STR_Melody_Chord_list3[index]] 
                                               for index in range(len(STR_Melody_Chord_list3))]
                New_Melody_Chord_list3 = [[index, 
                                           new_z[::5][index]]
                                          for index in range(len(STR_Melody_Chord_list3))]
            
            Sorted_Criteria_Melody_Chord_list3 = sorted(Criteria_Melody_Chord_list3, key=lambda x: x[1])
            biindex3 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list3)/2), 
                                         int(len(Sorted_Criteria_Melody_Chord_list3)/2))]
            if len(Criteria_Melody_Chord_list3) != len(biindex3):
                biindex3 = [i for i in range(int(-len(Sorted_Criteria_Melody_Chord_list3)/2), 
                                             int(len(Sorted_Criteria_Melody_Chord_list3)/2) + 1)]
            
            Criteria_Melody_Chord_list3 = [[biindex3[index], 
                                            Sorted_Criteria_Melody_Chord_list3[index][1], 
                                            Sorted_Criteria_Melody_Chord_list3[index][2]] 
                                           for index in range(len(Sorted_Criteria_Melody_Chord_list3))]
            
            Result3 = [None]*len(Criteria_Melody_Chord_list3)
            for mc in range(len(New_Melody_Chord_list3)):
                for smml in range(len(Criteria_Melody_Chord_list3)):
                    if (New_Melody_Chord_list3[mc][1] < (Criteria_Melody_Chord_list3[smml][1] + Criteria_Melody_Chord_list3[smml - 1][1])/2) and (smml > 0):
                        target_value = Criteria_Melody_Chord_list3[smml][0] - 1
                        Result3[mc] = target_value
                        break
                    elif New_Melody_Chord_list3[mc][1] < Criteria_Melody_Chord_list3[smml][1] and (smml == 0):
                        target_value = Criteria_Melody_Chord_list3[smml][0] - 1
                        Result3[mc] = target_value
                        break
            
            for check in range(len(Result3)):
                if (Result3[check] == None) and (New_Melody_Chord_list3[check][1] >= Criteria_Melody_Chord_list3[check][1]):
                    Result3[check] = max(Criteria_Melody_Chord_list3)[0]
                elif (Result3[check] == None) and (New_Melody_Chord_list3[check][1] <= Criteria_Melody_Chord_list3[check][1]):
                    Result3[check] = min(Criteria_Melody_Chord_list3)[0]
            
            Result3 = [element + int(len(Sorted_Criteria_Melody_Chord_list3)/2) for element in Result3]
            NV_Melody_Chord_list3 = [Criteria_Melody_Chord_list3[rindex][2] for rindex in Result3]
            replacement_list3 = NV_Melody_Chord_list3
            
            index3 = 0
            for element in ss[2].recurse():
                if isinstance(element, (music21.note.Note, music21.chord.Chord, music21.note.Rest)):
                    # Check if the replacement_list still has elements
                    if replacement_list3:
                        replacement3 = replacement_list3[index3]
                        duration_value3 = Duration_list3[index3]

                        if replacement3 == '<REST>':
                            # If the replacement is '<REST>', replace with a rest
                            new_element = music21.note.Rest()
                        elif isinstance(replacement3, list):
                            # If the replacement is a chord, create a chord object
                            new_element = music21.chord.Chord(replacement3)
                        else:
                            # If the replacement is a note, create a note object
                            new_element = music21.note.Note(replacement3)

                        # Set the duration for the new element
                        new_element.duration = music21.duration.Duration(duration_value3)

                        # Replace the old element with the new element
                        element.activeSite.replace(element, new_element)

                        index3 += 1
        
        us = music21.environment.UserSettings()
        us['lilypondPath'] = self.lilypondPath
        
        s.metadata = music21.metadata.Metadata()
        s.metadata.title = origin_name
        conv1 = music21.converter.subConverters.ConverterLilypond()
        scorename = origin_name
        filepath = self.yourfilepath + scorename 
        conv1.write(s, fmt='lilypond', fp=filepath, subformats = ['pdf'])
        sname = origin_name + '.mid'
        s.write('midi', sname)
        
        ss.metadata = music21.metadata.Metadata()
        ss.metadata.title = new_name
        conv2 =  music21.converter.subConverters.ConverterLilypond()
        scorename = new_name
        filepath = self.yourfilepath + scorename 
        conv2.write(ss, fmt = 'lilypond', fp=filepath, subformats = ['pdf'])
        ssname = new_name + '.mid'
        ss.write('midi', ssname)
        
        return "If This function didn't return any error, your file should be in the same .ipynb file directory"