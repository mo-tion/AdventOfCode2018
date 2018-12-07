num_workers = 5
fixed_time = 60
ascii_offset = 64

active_tasks = {}

with open("assembly.txt", "r") as input_file:
    instructions = input_file.readlines()


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

print (id_to_reqs)
order = ""
t = 0
while len(id_to_reqs) > 0 or len(active_tasks) > 0:
    # decrese work left for all active tasks

    for active_req_id, work in active_tasks.items():
        active_tasks[active_req_id] = work-1

        # check for completed tasks and remove the reqs, if finished
        if work < 2:
            active_tasks.pop(active_req_id)

            for req_id, reqs in id_to_reqs.items():
                id_to_reqs[req_id] = [req for req in id_to_reqs[req_id] if not req == active_req_id]

    # find applicable tasks

    applicable = []
    for req_id, reqs in id_to_reqs.items():
        if reqs == []:
            applicable.append(req_id)

    # distribute applicable tasks to free workers

    if len(applicable) > 1:
        applicable.sort()

    free_workers = num_workers - len(active_tasks)
    for i in range(min(free_workers, len(applicable))):
        active_tasks[applicable[i]] = ord(applicable[i]) - ascii_offset + fixed_time
        id_to_reqs.pop(applicable[i])
    
    print ("t: {:03d}, active: {}".format(t, active_tasks))
    t += 1

print(t-1)
