import musicbox
import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))

m = musicbox.MusicBox()
frequency = 100  # For repetition of note (delay effect)
lowest_note = 30  # Lowest note that can be played

'''Default order of notes on keyboard (Don't worry, I did not manually type this out.)'''
note = {8: 81, 9: 54, 13: 53, 47: 40, 48: 78, 39: 52, 44: 38, 45: 79, 46: 39, 303: 41, 304: 30, 49: 69, 50: 70, 51: 71, 52: 72, 53: 73, 54: 74, 55: 75, 56: 76, 57: 77, 59: 51, 61: 80, 91: 65, 92: 67, 93: 66, 96: 68, 97: 42, 98: 35, 99: 33, 100: 44, 101: 57, 102: 45, 103: 46, 104: 47, 105: 62, 106: 48, 107: 49, 108: 50, 109: 37, 110: 36, 111: 63, 112: 64, 113: 55, 114: 58, 115: 43, 116: 59, 117: 61, 118: 34, 119: 56, 120: 32, 121: 60, 122: 31}

def main():

    #map_notes()
    #print(note)
    running = True
    sustain = False  # To sustain notes
    selective_sustain = False  # To sustain a select group of notes
    sustained_notes = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_SPACE:
                    sustain = True
                if event.key == pygame.K_LCTRL:
                    selective_sustain = True
                if event.key in note:
                    m.play_note(note[event.key])     
                    if sustain:
                        sustained_notes.append(note[event.key])
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if not selective_sustain and not sustain:
                    if event.key in note:
                        m.stop_note(note[event.key])
                elif event.key == pygame.K_LCTRL:
                    selective_sustain = False
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


main()
m.close()
pygame.quit()