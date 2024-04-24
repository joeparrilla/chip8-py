import pygame

from cpu import CPU
from display import Display
from pygame import time
from pygame import event

WIDTH=600
HEIGHT=480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

class Emulator:
    def __init__(self):
        self.cpu = CPU()
        self.display = Display()

    def run(self):
        self.cpu.load_rom('IBM Logo.ch8')
        self.cpu.load_font()
        self.display.dump_screen_bits();
        # self.cpu.dump_cpu()
        pygame.init()
        running = True

        while running:

            #pygame.time.wait(1000)
            #print('tick')
            #self.cpu.cycle()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("Key 1 has been pressed")
                    if event.key == pygame.K_2:
                        print("Key 2 has been pressed")
                    if event.key == pygame.K_3:
                        print("Key 3 has been pressed")         
                    if event.key == pygame.K_4:
                        print("Key C has been pressed")
                    if event.key == pygame.K_q:
                        print("Key 4 has been pressed")
                    if event.key == pygame.K_w:
                        print("Key 5 has been pressed")
                    if event.key == pygame.K_e:
                        print("Key 6 has been pressed")         
                    if event.key == pygame.K_r:
                        print("Key D has been pressed")
                    if event.key == pygame.K_a:
                        print("Key 7 has been pressed")
                    if event.key == pygame.K_s:
                        print("Key 8 has been pressed")
                    if event.key == pygame.K_d:
                        print("Key 9 has been pressed")         
                    if event.key == pygame.K_f:
                        print("Key E has been pressed")
                    if event.key == pygame.K_z:
                        print("Key A has been pressed")
                    if event.key == pygame.K_x:
                        print("Key 0 has been pressed")
                    if event.key == pygame.K_c:
                        print("Key B has been pressed")         
                    if event.key == pygame.K_v:
                        print("Key F has been pressed")
                    if event.key == pygame.K_SPACE:
                        print("CPU CYCLE")
                        self.cpu.cycle()
