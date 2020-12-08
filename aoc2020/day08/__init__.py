import re

instruction_regex = re.compile(r'(\w+) ([+-]\d+)')


class Instruction(object):
    opcode: str
    operand: int
    visits: int

    def __init__(self, instruction_string: str):
        opcode, operand = instruction_regex.match(instruction_string).groups()
        self.opcode = opcode
        self.operand = int(operand)
        self.visits = 0


def execute(instructions: [Instruction], throw_on_loop: bool = False) -> int:
    accumulator = 0
    program_counter = 0
    while program_counter < len(instructions):
        instruction = instructions[program_counter]

        if instruction.visits > 0:
            if throw_on_loop:
                raise RuntimeError()
            else:
                return accumulator

        if instruction.opcode == "nop":
            program_counter += 1
        elif instruction.opcode == "acc":
            accumulator += instruction.operand
            program_counter += 1
        elif instruction.opcode == "jmp":
            program_counter += instruction.operand

        instruction.visits += 1
    return accumulator


def part1(instruction_strings: [str]) -> int:
    instructions = [Instruction(i) for i in instruction_strings]
    return execute(instructions)


def part2(instruction_strings: [str]) -> int:
    for pc in range(len(instruction_strings)):
        instructions = [Instruction(i) for i in instruction_strings]

        if instructions[pc].opcode == "acc":
            pass
        elif instructions[pc].opcode == "jmp":
            instructions[pc].opcode = "nop"
        elif instructions[pc].opcode == "nop":
            instructions[pc].opcode = "jmp"

        try:
            return execute(instructions, throw_on_loop=True)
        except RuntimeError:
            pass
