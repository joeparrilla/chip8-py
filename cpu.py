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
            'pc': 0x200,
            'sp': 0,
            'index': 0
        }

    def cycle(self):
        #Fetch
        print('pc: ' + hex(self.registers['pc']))
        self.operand = self.mem[self.registers['pc']]
        self.operand <<= 8
        self.operand += self.mem[self.registers['pc'] + 1]
        self.registers['pc'] += 2
        print('opcode: ' + hex(self.operand))

        #split the opcode into important parts
        op = (self.operand & 0xF000) >> 12
        x = (self.operand & 0x0F00) >> 8
        y = (self.operand & 0x00F0) >> 4
        n = (self.operand & 0x000F)
        nn = (self.operand & 0x00FF)
        nnn = (self.operand & 0x0FFF)
        print('op:' + hex(op) + ' x:' + hex(x) + ' y:' + hex(y) + ' n:' + hex(n) + ' nn:' + hex(nn) + ' nnn:' + hex(nnn))
        
        #Decode

        #Execute

    def load_rom(self, rom):
        data = open(rom, 'rb').read()
        for index, val in enumerate(data):
            self.mem[0x200 + index] = val
    
    def load_font(self):
        for index, val in enumerate(FONT):
            self.mem[0x50 + index] = val

    def dump_cpu(self):
        data = f"""
        CPU Contents:
        Registers: {self.registers}
        Timers: {self.timers}
        Stack: {self.stack}
        Memory: {self.mem.hex()}
        """
        print(data)

    
    #INSTRUCTIONS
    
    #00E0 - CLS
    def op_00e0(self):
        return

    #1nnn - JP addr
    def op_1nnn(self, nnn):
        self.pc = nnn

    #6xkk - LD Vx, byte
    def op_6xkk(self, x, kk):
        self.registers['v'][x] = kk

    #7xkk - ADD Vx, byte
    def op_7xkk(self, x, kk):
        self.registers['v'][x] += kk

    #Annn - LD I, addr
    def op_annn(self, nnn):
        self.registers['index'] = nnn

    #Dxyn - DRW Vx, Vy, nibble
    def op_dxyn(self, x, y, nib):
        return