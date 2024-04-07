import pygame

from cpu import CPU
from pygame import time
from pygame import event

class Emulator:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cpu.load_rom('IBM Logo.ch8')
        self.cpu.dump_cpu()
        pygame.init()
        running = True

        while running:

            pygame.time.wait(1000)
            #print('tick')
            self.cpu.cycle()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
