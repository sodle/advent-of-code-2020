import re

mask_command_rex = re.compile(r"^mask = ([01X]+)$")
mem_command_rex = re.compile(r"^mem\[(\d+)] = (\d+)$")


def apply_address_mask(value_bits: str, mask_bits: str) -> [str]:
    if len(value_bits) != len(mask_bits):
        raise ValueError("Mask and value must be same size!")

    value_bits_masked = "".join(["1" if mask_bits[i] == "1" else v for i, v in enumerate(value_bits)])
    value_bits = value_bits_masked

    if "X" not in mask_bits:
        return [value_bits]
    else:
        first_mask_addr = mask_bits.index("X")
        value_bits_before = value_bits[:first_mask_addr]
        value_bits_after = value_bits[first_mask_addr + 1:]
        mask_bits_after = mask_bits[first_mask_addr + 1:]
        partials = apply_address_mask(value_bits_after, mask_bits_after)
        return [f"{value_bits_before}0{p}" for p in partials] + [f"{value_bits_before}1{p}" for p in partials]


def part1(commands: [str]) -> int:
    memory = {}
    mask = "X" * 36

    for command in commands:
        if 'mask' in command:
            mask, = mask_command_rex.match(command).groups()
        elif 'mem[' in command:
            addr, value_str = mem_command_rex.match(command).groups()
            value_int = int(value_str)
            value_bits = f"{value_int:036b}"
            masked_value = ""
            for place, bit in enumerate(value_bits):
                if mask[place] == "X":
                    masked_value += bit
                else:
                    masked_value += mask[place]
            memory[addr] = masked_value

    return sum([int(memory[i], 2) for i in memory])


def part2(commands: [str]) -> int:
    memory = {}
    mask = "X" * 36

    for command in commands:
        if 'mask' in command:
            mask, = mask_command_rex.match(command).groups()
        elif 'mem[' in command:
            addr_str, value_str = mem_command_rex.match(command).groups()
            addr_int = int(addr_str)
            value = int(value_str)
            addr_bits = f"{addr_int:036b}"
            write_addrs = apply_address_mask(addr_bits, mask)
            for addr in write_addrs:
                memory[addr] = value

    return sum([memory[i] for i in memory])
