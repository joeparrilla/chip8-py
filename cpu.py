from collections import deque

MEM_SIZE = 4096
STACK_SIZE = 16
FONT = [0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
        0x20, 0x60, 0x20, 0x20, 0x70, # 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
        0x90, 0x90, 0xF0, 0x10, 0x10, # 4
        0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
        0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
        0xF0, 0x10, 0x20, 0x40, 0x40, # 7
        0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
        0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
        0xF0, 0x90, 0xF0, 0x90, 0x90, # A
        0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
        0xF0, 0x80, 0x80, 0x80, 0xF0, # C
        0xE0, 0x90, 0x90, 0x90, 0xE0, # D
        0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
        0xF0, 0x80, 0xF0, 0x80, 0x80] # F

class CPU:
    def __init__(self):
        self.mem = bytearray(MEM_SIZE)
        self.stack = deque(maxlen=STACK_SIZE)
        self.operand = 0
        self.timers = {
            'delay': 0,
            'sound': 0
        }
        self.registers = {
            'v': [],
            'pc': 0,
            'sp': 0,
            'index': 0
        }

    def cycle(self):
        #Fetch
        self.operand = self.mem[self.registers['pc']]
        self.operand << 8
        self.operand += self.mem[self.registers['pc'] + 1]
        self.registers['pc'] += 2
        
        #Decode

        #Execute

    def load_rom(self, rom):
        data = open(rom, 'rb').read()
        for index, val in enumerate(data):
            self.mem[0x200 + index] = val
    
    def load_font(self):
        for index, val in enumerate(FONT):
            self.mem[0x050 + index] = val

    def dump_cpu(self):
        data = f"""
        CPU Contents:
        Registers: {self.registers}
        Timers: {self.timers}
        Stack: {self.stack}
        Memory: {self.mem.hex()}
        """
        print(data)