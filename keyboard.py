import musicbox
import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))

pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])

instrument = 0
m = musicbox.MusicBox(instrument)
frequency = 100  # For repetition of note (delay effect)
lowest_note = 36  # Lowest note that can be played (36 is C2, 2 octaves below middle C)

'''Current order of notes on keyboard'''
note = {8: 87, 9: 60, 13: 59, 47: 46, 48: 84, 39: 58, 44: 44, 45: 85, 46: 45, 303: 47, 304: 36, 49: 75, 50: 76, 51: 77, 52: 78, 53: 79, 54: 80, 55: 81, 56: 82, 57: 83, 59: 57, 61: 86, 91: 71, 92: 73, 93: 72, 96: 74, 97: 48, 98: 41, 99: 39, 100: 50, 101: 63, 102: 51, 103: 52, 104: 53, 105: 68, 106: 54, 107: 55, 108: 56, 109: 43, 110: 42, 111: 69, 112: 70, 113: 61, 114: 64, 115: 49, 116: 65, 117: 67, 118: 40, 119: 62, 120: 38, 121: 66, 122: 37}

'''Default order of notes on keyboard'''
default_notes = {8: 87, 9: 60, 13: 59, 47: 46, 48: 84, 39: 58, 44: 44, 45: 85, 46: 45, 303: 47, 304: 36, 49: 75, 50: 76, 51: 77, 52: 78, 53: 79, 54: 80, 55: 81, 56: 82, 57: 83, 59: 57, 61: 86, 91: 71, 92: 73, 93: 72, 96: 74, 97: 48, 98: 41, 99: 39, 100: 50, 101: 63, 102: 51, 103: 52, 104: 53, 105: 68, 106: 54, 107: 55, 108: 56, 109: 43, 110: 42, 111: 69, 112: 70, 113: 61, 114: 64, 115: 49, 116: 65, 117: 67, 118: 40, 119: 62, 120: 38, 121: 66, 122: 37}
'''White and black keys of piano layout'''
piano_layout = {115: 61, 48: 85, 54: 78, 55: 80, 112: 86, 45: 87, 56: 82, 91: 88, 93: 89, 116: 77, 98: 67, 99: 64, 100: 63, 101: 74, 103: 66, 104: 68, 105: 83, 106: 70, 109: 71, 110: 69, 111: 84, 304: 59, 114: 76, 51: 73, 52: 75, 117: 81, 118: 65, 119: 72, 120: 62, 121: 79, 122: 60}
'''Pentatonic scale in E minor'''
pent_scale_layout = {91: 100, 44: 45, 110: 40, 111: 95, 92: 105, 93: 103, 97: 52, 98: 38, 99: 33, 100: 57, 101: 81, 102: 59, 103: 62, 104: 64, 105: 93, 106: 67, 107: 69, 108: 71, 109: 43, 46: 47, 47: 50, 112: 98, 113: 76, 114: 83, 115: 55, 116: 86, 117: 91, 118: 35, 119: 79, 120: 31, 121: 88, 122: 28, 59: 74}

def main():
    global note
    running = True
    sustain = False  # To sustain notes
    sustained_notes = []
    global instrument
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sustain = True
                if event.key in note:
                    m.play_note(note[event.key])
                    if sustain:
                        sustained_notes.append(note[event.key])
                if event.key == pygame.K_INSERT:  # Re-map note order/layout
                    map_notes()
                if event.key == pygame.K_DELETE:
                    note = default_notes
                if event.key == pygame.K_END:
                    note = piano_layout
                if event.key == pygame.K_PAGEDOWN:
                    note = pent_scale_layout
                if event.key == pygame.K_UP:  # Navigate upwards through instruments
                    if instrument < 127:
                        instrument += 1
                        m.set_instrument(instrument)
                if event.key == pygame.K_DOWN:  # Navigate downwards through instruments
                    if instrument > 0:
                        instrument -= 1
                        m.set_instrument(instrument)
                if event.key == pygame.K_F1:
                    set_sound(0)  # Piano
                if event.key == pygame.K_F2:
                    set_sound(4)  # Electric Piano
                if event.key == pygame.K_F3:
                    set_sound(16)  # Electric Organ
                if event.key == pygame.K_F4:
                    set_sound(19)  # Pipe Organ
                if event.key == pygame.K_F5:
                    set_sound(48)  # Strings
                if event.key == pygame.K_F6:
                    set_sound(52)  # Choir
                if event.key == pygame.K_F7:
                    set_sound(14)  # Bells
                if event.key == pygame.K_F8:
                    set_sound(81)  # Synth
                if event.key == pygame.K_F9:
                    set_sound(55)  # Impact/Chord hit
                if event.key == pygame.K_F10:
                    set_sound(86)  # Fifth
                if event.key == pygame.K_F11:
                    set_sound(124)  # Telephone
                if event.key == pygame.K_F12:
                    set_sound(125)  # Helicopter
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if not sustain:
                    if event.key in note:
                        m.stop_note(note[event.key])
                elif event.key == pygame.K_SPACE:
                    sustain = False
                    for i in sustained_notes:
                        m.stop_note(sustained_notes.pop())


def set_sound(num):
    global instrument
    instrument = num
    m.set_instrument(instrument)

def set_frequency(amount):
    global frequency
    frequency += amount


def map_notes():
    global lowest_note
    note.clear()
    key_order = []
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                else:
                    key_order.append(event.key)
    j = 0
    for i in key_order:
        note[i] = lowest_note + j
        j += 1


def map_pent_scale():
    global lowest_note
    note.clear()
    key_order = []
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                else:
                    key_order.append(event.key)
    j = 0
    k = 0
    for i in key_order:
        note[i] = lowest_note + j
        if k % 5 == 0 or (k + 2) % 5 == 0:  # 1st or 4th note in scale
            j += 3
        else:
            j += 2
        k += 1

main()
m.close()
pygame.quit()