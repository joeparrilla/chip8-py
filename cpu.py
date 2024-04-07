from collections import deque

MEM_SIZE = 4096
STACK_SIZE = 16

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

    def dump_cpu(self):
        data = f"""
        CPU Contents:
        Registers: {self.registers}
        Timers: {self.timers}
        Stack: {self.stack}
        Memory: {self.mem.hex()}
        """
        print(data)