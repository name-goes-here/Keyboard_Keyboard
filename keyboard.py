import musicbox
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((100, 100))

m = musicbox.MusicBox()
frequency = 200

note = {
    pygame.K_x:50,
    pygame.K_c:55,
    pygame.K_v:60
}

def main():

    key_down = False
    running = True

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                #key_down = True
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

                else:
                    if event.key in note:
                        while keystate[event.key]:
                            play(note[event.key], frequency)
                            keystate = pygame.key.get_pressed()
                    '''if event.key in note:
                        pygame.key.set_repeat(10, 10)
                        m.play_note(note[event.key], 50)
                        print(event.scancode, event.key, event.unicode)'''

def play(note, duration):
    m.play_note(note, duration)
    time.sleep(duration/1000)

def set_frequency(amount):
    global frequency
    frequency += amount

main()
pygame.quit()