import ops

with open("input.txt", "r") as in_file:
    lines = in_file.readlines()
    examples_in = lines[:3160]


def parse_example(example):
    pre = [int(x) for x in example[0][9:-2].split(", ")]
    instruction = [ int(x) for x in example[1][:-1].split(" ")]
    result = [ int(x) for x in example[2][9:-2].split(", ")]
    return pre, instruction, result


operations = ops.operations

num_over_two_examples = 0
op_code_to_ops = {}
for i in range(len(examples_in)/4):
    state, instr, res = parse_example(examples_in[i*4:i*4+3])

    num_valid = 0

    possible_ops = set()
    impossible_ops = set()

    for f, f_name in operations:
        if instr[0] not in op_code_to_ops.keys():
            op_code_to_ops[instr[0]] = (set(), set())
            print ("create sets for {}".format(instr[0]))

        if f(state, instr[1:]) == res:
            num_valid += 1
            op_code_to_ops[instr[0]][0].add(f_name)
        else:
            op_code_to_ops[instr[0]][1].add(f_name)

    if num_valid > 2:
        num_over_two_examples += 1

print num_over_two_examples

assignments = []
for op_code, (poss, imposs) in op_code_to_ops.items():
    print ("op code {} {}".format(op_code, poss.difference(imposs)))
