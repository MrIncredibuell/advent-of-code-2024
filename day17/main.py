from dataclasses import dataclass
from copy import deepcopy

@dataclass
class CPU:
    a: int
    b: int
    c: int
    program: list[int]
    ip: int = 0
    quine: bool = False

    _output = []

    def combo(self, operand):
        if operand == 4:
            operand = self.a
        elif operand == 5:
            operand = self.b
        elif operand == 6:
            operand = self.c
        return operand

    def step(self):
        if self.ip >= len(self.program):
            return False
        operator = self.program[self.ip]
        operand = self.program[self.ip + 1]

        # print(operator, operand)

        if operator == 0:
            self.a = self.a // 2**self.combo(operand)
        elif operator == 1:
            self.b = self.b ^ operand
        elif operator == 2:
            self.b = self.combo(operand) % 8
        elif operator == 3:
            if self.a != 0:
                self.ip = operand
                return True
        elif operator == 4:
            self.b = self.b ^ self.c
        elif operator == 5:
            self._output.append(self.combo(operand) % 8)
            if self.quine and (len(self._output) > len(self.program) or self._output[-1] != self.program[len(self._output) - 1]):
                raise ValueError("TOO BAD")
        elif operator == 6:
            self.b = self.a // 2**self.combo(operand)
        elif operator == 7:
            self.c = self.a // 2**self.combo(operand)
        self.ip += 2
        return True


lines = open("input.txt").read().split("\n")

data = CPU(
    int(lines[0].split(" ")[-1]),
    int(lines[1].split(" ")[-1]),
    int(lines[2].split(" ")[-1]),
    [int(i) for i in lines[4].split(" ")[-1].split(",")]
)



def part1(data):
    while data.step():
        pass
    return ",".join([str(i) for i in data._output])


def part2(data):
    i = 1
    best = []
    # for i in range(10):
    while True:
        cpu = deepcopy(data)
        cpu.a = i
        cpu.quine = True
        cpu._output = []
        try:
            # print(cpu)
            while cpu.step():
                # print(cpu)
                pass
            # print(cpu, cpu._output)
            # if cpu._output == cpu.program:
            #     return i
        except ValueError:
            pass
            # return
        if len(cpu._output) - 1 >= len(best):
            best = cpu._output[:-1]
            if len(best) == 3:
                print(i, len(best))
                return
        # print(i, cpu._output)
        i += 1
    

# print(part1(deepcopy(data)))
print(part2(deepcopy(data)))

# def foo(A):
#     C = A // (2 ** ((A % 8) ^ 1))
#     B = 

'''
A % 8 -> B
B ^ 1 -> B
A // 2 ** B -> C
A // 8 -> A
B ^ 4 -> B
B ^ C -> B
print B % 8
JUMP




A = A // 8
B = (2 ** ((A % 8) ^ 1)) ^ 4 ^ (A // (2 ** ((A % 8) ^ 1)))
C = A // (2 ** ((A % 8) ^ 1))

((((A % 8) ^ 1)) ^ 4 ^ (A // (2 ** ((A % 8) ^ 1)))) % 8
'''