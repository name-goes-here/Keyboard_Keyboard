import musicbox
import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))

pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])

instrument = 0
m = musicbox.MusicBox(instrument)
frequency = 100  # For repetition of note (delay effect)
lowest_note = 36  # Lowest note that can be played

'''Default order of notes on keyboard (Don't worry, I did not manually type this out.)'''
note = {8: 87, 9: 60, 13: 59, 47: 46, 48: 84, 39: 58, 44: 44, 45: 85, 46: 45, 303: 47, 304: 36, 49: 75, 50: 76, 51: 77, 52: 78, 53: 79, 54: 80, 55: 81, 56: 82, 57: 83, 59: 57, 61: 86, 91: 71, 92: 73, 93: 72, 96: 74, 97: 48, 98: 41, 99: 39, 100: 50, 101: 63, 102: 51, 103: 52, 104: 53, 105: 68, 106: 54, 107: 55, 108: 56, 109: 43, 110: 42, 111: 69, 112: 70, 113: 61, 114: 64, 115: 49, 116: 65, 117: 67, 118: 40, 119: 62, 120: 38, 121: 66, 122: 37}

def main():

    #map_notes()
    #print(note)
    running = True
    sustain = False  # To sustain notes
    sustained_notes = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_SPACE:
                    sustain = True
                if event.key in note:
                    m.play_note(note[event.key])     
                    if sustain:
                        sustained_notes.append(note[event.key])
                if event.key == pygame.K_UP:
                    m.set_instrument(++instrument)
                if event.key == pygame.K_DOWN:
                    m.set_instrument(--instrument)
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


def change_instrument():
    #  Possible implementation: When an assigned key is pressed (insert, del, etc...), user can type in a specific number to change sound


main()
m.close()
pygame.quit()