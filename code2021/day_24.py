
class ALU:
    def __init__(self, prog):
        self.prog = prog
        self.d = {'x':0, 'y':0, 'z':0, 'w':0,}
        self.inp_ind = -1
        self.input_v = []

    def reboot(self, input_v):
        self.d = {'x':0, 'y':0, 'z':0, 'w':0,}
        self.inp_ind = -1
        self.input_v = input_v

    def run(self, input_v):
        self.reboot(input_v)
        for op,v in self.prog: getattr(self, op)(*v)
        return self.d

    def inp(self, a):
        self.inp_ind += 1
        self.d[a] = self.input_v[self.inp_ind]

    def add(self, a, b):
        if type(b)==type(0): self.d[a] += b
        else: self.d[a] += self.d[b]

    def mul(self, a, b):
        if type(b)==type(0): self.d[a] *= b
        else: self.d[a] *= self.d[b]

    def div(self, a, b):
        if type(b)==type(0): self.d[a] //= b
        else: self.d[a] += self.d[b]

    def mod(self, a, b):
        if type(b)==type(0): self.d[a] %= b
        else: self.d[a] %= self.d[b]

    def eql(self, a, b):
        if type(b)==type(0): self.d[a] = int(self.d[a]==b)
        else: self.d[a] = int(self.d[a]==self.d[b])





def solve_a():
    from itertools import product
    prog = []
    t = input()
    while len(t)>0:
        op = t.split()[0]
        v = t.split()[1:]
        for i in range(len(v)):
            try: v[i] = int(v[i])
            except: pass
        prog.append((op, v))
        t = input()

    alu = ALU(prog)

    c = 0
    for v in product((9, 8, 7, 6, 5, 4, 3, 2, 1)[::-1], repeat=14):
        c += 1
        if c % 100000 == 0: print(''.join(map(str, v[::-1])))
        t = alu.run(v[::-1])
        if t['z'] == 0: print('______', ''.join(map(str, v[::-1])))

def solve_b():...

if __name__ == "__main__":
    solve_a()
