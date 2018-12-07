with open("assembly.txt", "r") as input_file:
    instructions = input_file.readlines()

# instructions = [
# "Step C must be finished before step A can begin.",
# "Step C must be finished before step F can begin.",
# "Step A must be finished before step B can begin.",
# "Step A must be finished before step D can begin.",
# "Step B must be finished before step E can begin.",
# "Step D must be finished before step E can begin.",
# "Step F must be finished before step E can begin."
# ]

id_to_reqs = {}
for instruction in instructions:
    inst_id = instruction.split(' ')[7]
    requirement = instruction.split(' ')[1]
    if not inst_id in id_to_reqs:
        id_to_reqs[inst_id] = [requirement]
    else:
        id_to_reqs[inst_id].append(requirement)

    if not requirement in id_to_reqs:
        id_to_reqs[requirement] = []

order = ""

while len(id_to_reqs) > 0:

    applicable = []
    for req_id, reqs in id_to_reqs.items():
        if reqs == []:
            applicable.append(req_id)

    if len(applicable) > 1:
        applicable.sort()

    order += applicable[0]
    id_to_reqs.pop(applicable[0])

    for req_id, reqs in id_to_reqs.items():
        id_to_reqs[req_id] = [req for req in id_to_reqs[req_id] if not req == applicable[0]]

print(order)