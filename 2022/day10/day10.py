def print_crt(crt):
    for row in crt:
        print("".join(row), end="\n")

def render_crt(crt, x, cycle):
    row = cycle // 40
    drawing_position = cycle % 40
    if row <= 5:
        if -1 <= x <= 40:
            if (x-1) <= drawing_position <= (x+1):
                crt[row][drawing_position] = " ■ "
            else:
                crt[row][drawing_position] = " . "
    return crt

def run_instructions(cycles):
    with open("2022/day10/input.txt", "r") as f:
        instructions = f.read().splitlines()
        for count in range(0, len(instructions)):
            instructions[count] = instructions[count].split(" ")

        crt = [["."] * 40 for i in range(6)]
        for count in range(0, len(instructions)):
            if (instructions[count-1][0]) == "noop":
                cycles.append(cycles[-1])
                crt = render_crt(crt, cycles[-1], len(cycles)-2)
            if instructions[count][0] == "addx":
                cycles.append(cycles[-1])
                crt = render_crt(crt, cycles[-1], len(cycles)-2)
                cycles.append((cycles[-1])+(int(instructions[count][1])))
                crt = render_crt(crt, cycles[-1], len(cycles)-2)

    return cycles, crt

def calculate_signal_strengths(registers):
    signal_strengths = []
    for count in range(0, len(registers)):
        signal_strengths.append(registers[count]*(count))
    return signal_strengths

if __name__ == "__main__":
    registers = [1]
    registers, crt = run_instructions(registers)
    signal_strengths = calculate_signal_strengths(registers)
    strength = 0
    for i in [20, 60, 100, 140, 180, 220]:
        strength += signal_strengths[i]
    print(f"Strength: {strength}")
    print_crt(crt)