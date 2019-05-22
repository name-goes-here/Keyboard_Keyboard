import musicbox
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((100, 100))

m = musicbox.MusicBox()
frequency = 100
lowest_note = 30
key_order = []

note = {8: 81, 9: 55, 13: 54, 45: 79, 47: 40, 48: 78, 39: 53, 44: 38, 301: 42, 46: 39, 303: 41, 304: 30, 49: 70, 50: 71, 51: 72, 52: 73, 53: 74, 54: 75, 56: 76, 57: 77, 59: 52, 61: 80, 91: 66, 92: 68, 93: 67, 96: 69, 97: 43, 98: 35, 99: 33, 100: 45, 101: 58, 102: 46, 103: 47, 104: 48, 105: 63, 106: 49, 107: 50, 108: 51, 109: 37, 110: 36, 111: 64, 112: 65, 113: 56, 114: 59, 115: 44, 116: 60, 117: 62, 118: 34, 119: 57, 120: 32, 121: 61, 122: 31}

'''def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in note:
                    m.play_note(note[event.key])
                #key = note[event.key]
                #m.play_note(60)
                #print(event.scancode, event.key, event.unicode)
                #print(note[event.key])
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                #if event.key in note:
                m.stop_note(event.key)
            if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    while key_down:
                        set_frequency(1)
                        if event.type == pygame.KEYUP:
                            key_down = False
                elif event.key == pygame.K_DOWN:
                    while keystate[pygame.K_DOWN]:
                        set_frequency(-1)
                        keystate = pygame.key.get_pressed()

'''

def set_frequency(amount):
    global frequency
    frequency += amount


def map_notes():
    global key_order
    global lowest_note
    note.clear()
    key_order.clear()
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


#main()
m.close()
pygame.quit()