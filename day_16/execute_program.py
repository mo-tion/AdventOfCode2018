import ops

with open("input.txt", "r") as in_file:
    lines = in_file.readlines()
    examples_in = lines[3162:]


def parse_op(example):
    instruction = [int(x) for x in example[:-1].split(" ")]
    return instruction


operations = ops.operations

num_over_two_examples = 0

state = [0, 0, 0, 0]

for instr_in in examples_in:
    instr = parse_op(instr_in)

    state = ops.code_to_op[instr[0]](state, instr[1:])

print state
