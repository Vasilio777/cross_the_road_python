from MovingBlock import MovingBlock

class BlockManager():
    def __init__(self, blocks_amount):
        super().__init__()
        self.blocks_amount = blocks_amount
        self.blocks = [MovingBlock() for i in range(blocks_amount)]
        self.active_pointer = 0
        self.freq_counter = 0
        self.freq = 10

    def move_blocks(self, frog):
        if self.freq_counter % self.freq == 0:
            self.freq_counter = 0
            
            self.blocks[self.active_pointer].set_active(True)

            if self.active_pointer < len(self.blocks)-1:
                self.active_pointer += 1

        for i in range(self.active_pointer):
            self.blocks[i].move(frog)

        self.freq_counter += 1

    def on_next_level(self):
        for block in self.blocks:
            block._reset(speed_offset=0.1)
            block.set_active(False)

        self.active_pointer = 0
