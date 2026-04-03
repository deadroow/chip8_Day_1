from ..decorators.check_path import check_path
from ..decorators.get_data import get_data
class chip8:
    def __init__(self):
        self.memory=[0]*4096
        self.V=[0]*16
        self.pc=0x200
        self.stack=[]
        self.i=0
        self.sound=0
        self.delay=0
        self.ecran=[]*64*32
    @check_path
    @get_data
    def load_rom(self,path,rom=None):
            start=0x200
            end=start+len(rom)
            self.memory[start:end]= rom
            

    def fetch(self):
         print(f"pc {self.memory[self.pc]<<8:04X}")
         print(f"pc+1 {self.memory[self.pc+1]:04X}")
         opcode = self.memory[self.pc]<<8 | self.memory[self.pc+1]
         print(f"{opcode :0A4}")