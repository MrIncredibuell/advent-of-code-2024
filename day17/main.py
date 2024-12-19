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


def run(A):
    return ((((A % 8) ^ 1)) ^ 4 ^ (A // (2 ** ((A % 8) ^ 1)))) % 8

def part2(data):
    program = data.program
    index = 0
    product = 0

    while index < len(program):
        index += 1
        goal = program[-index]
        i = 0
        while run(product+i) != goal:
            i += 1
        product += i
        product *= 8
    A = product

    output = []
    while A:
        output.append(run(A))
        A = A // 8
    # print(output)
    return product // 8

print(part1(deepcopy(data)))
print(part2(deepcopy(data)))

