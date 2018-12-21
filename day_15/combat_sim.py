import copy
import time

pf_free = -1
pf_wall = -2
pf_unit = -3
pf_goblin = -3
pf_elf = -4

class Unit:
    def __init__(self, pos, faction):
        self.pos = pos
        self.faction = faction
        self.hp = 200
        self.ap = 3

class Timer:
    def __init__(self):
        self.start = time.clock()

    def start_timer(self):
        self.start = time.clock()

    def stop_timer(self, text, proc_name):
        print (text.format(proc_name, time.clock() - self.start) )

def get_neighbours(x_pos, y_pos):
    return [(x_pos + 1, y_pos), (x_pos - 1, y_pos), (x_pos, y_pos + 1), (x_pos, y_pos - 1)]

class Node:
    def __init__(self, pos, start):
        self.path = []
        self.est = abs(pos[0] - start[0]) + abs(pos[1] - start[1])
        self.pos = pos

    def dist(self):
        if len(self.path) == 0:
            return float("inf")
        else:
            return len(self.path[0])

def is_reachable(start, goal, round=None):
    next_nodes = []
    all_nodes = {}

    global stored_round
    global mem

    if start == (2,1):
        pass

    if stored_round != round:
        stored_round = round
        mem = {}
        print "reset mem"

    if start in mem.keys():
        timer.start_timer()

        all_nodes = mem[start]
        if all_nodes[goal].dist() < float("inf"):
            # print goal
            # timer.stop_timer("Mem access for {} finished in {}", str(start))
            return (True, [path[2:] + [goal] for path in all_nodes[goal].path])
        else:
            # print ("no path")
            # timer.stop_timer("Mem access for {} finished in {}", str(start))
            return (False, None)



    for x_pos in range(width):
        for y_pos in range(height):
            if playfield[y_pos][x_pos] != pf_wall and (x_pos, y_pos) != start:
                node = Node((x_pos, y_pos), start)
                all_nodes[(x_pos, y_pos)] = node
                next_nodes.append(node)

    start_node = Node(start, start)
    start_node.path = [[start]]
    all_nodes[start] = start_node
    next_nodes.append(start_node)

    next_nodes = sorted(next_nodes, key=lambda x: x.dist())

    # print ("start {}".format(start))

    curr_min = float("inf")

    # timer.start_timer()
    
    while not len(next_nodes)==0:
        current_node = next_nodes[0]
        next_nodes = next_nodes[1:]


        # print ("neighbours of {}".format(current_node.pos))
        # print ("current has dist {}".format(current_node.dist()))
        neighbours = filter(lambda pos: playfield[pos[1]][pos[0]] == pf_free, get_neighbours(current_node.pos[0], current_node.pos[1]))
        # print (neighbours)
        for neighbour in neighbours:
            neighbour_node = all_nodes[neighbour]
            # print ("neighbour {} has current dist of {}".format(neighbour,neighbour_node.dist()))
            # print ("neighbour: {}".format(neighbour))
            if neighbour_node.dist() == current_node.dist() + 1:
                if current_node.dist() < 15:
                    neighbour_node.path.extend([path + [current_node.pos] for path in current_node.path])

            if neighbour_node.dist() > current_node.dist()+1:
                neighbour_node.path = [path+[current_node.pos] for path in current_node.path]

            # print ("neighbour {} has new dist of {}".format(neighbour,neighbour_node.dist()))
        next_nodes = sorted(next_nodes, key=lambda a: a.dist())

    # if start == (2, 1):
    #     print "hallo"
    #     for k, v in all_nodes.items():
    #         print (k, v.path)
    # timer.stop_timer("Node {} finished in {}", str(start))

    mem[start] = all_nodes

    if all_nodes[goal].dist() < float("inf"):
        # print goal
        return (True, [x_pos[2:] + [goal] for x_pos in all_nodes[goal].path])
    else:
        # print ("no path")
        return (False, None)



def unit_sort(unit):
    global width
    return unit.pos[1]*width+unit.pos[0]

def pos_sort(pos):
    global width
    return pos[1]*width+pos[0]

def find_open_spaces_at_target(unit):
    global playfield
    found = []
    for y, l in enumerate(playfield):
        for x, occ in enumerate(l):
            if x in [unit.pos[0]-1, unit.pos[0]+1] and y in [unit.pos[1]-1, unit.pos[1]+1] and occ == pf_free:
                found.append((x,y))
    return found

def vis():
    global playfield
    print (" " + "".join([str(i) for i in range(len(playfield[0]))]))
    i = 0
    unit_count = 0
    for line in playfield:
        print_line = str(i)
        unit_line = ""
        for ch in line:
            if ch == pf_free:
                print_line += '.'
            elif ch == pf_wall:
                print_line += '#'
            elif ch == pf_goblin:
                print_line += 'g'
                unit_line += 'G({})'.format(units[unit_count].hp)
                unit_count += 1
            elif ch == pf_elf:
                print_line += 'e'
                unit_line += 'E({})'.format(units[unit_count].hp)
                unit_count += 1
        print(print_line + ' ' + unit_line)
        i += 1

def is_reachable_old(start, goal, steps=[], visited=None):
    if visited is None:
        visited = set()
    global playfield

    if len(steps) == 0:
        visited = set(start)

    if start == goal:
        return (True, [steps])

    if playfield[start[1]][start[0]] == pf_wall:
        return (False, steps)

    if playfield[start[1]][start[0]] <= pf_unit and len(steps) > 0:
        return (False, steps)


    try_next = {(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] + 1), (start[0], start[1] - 1)}
    try_next = try_next - visited

    min_steps = float("inf")
    reach_paths = []

    for next in try_next:
        reachable, paths_to_goal = is_reachable_old(next, goal, steps + [next], visited | set(try_next))
        if reachable and len(paths_to_goal) > 0 and len(paths_to_goal[0])<=min_steps:
            if len(paths_to_goal[0])<min_steps:
                reach_paths = paths_to_goal
                min_steps = len(paths_to_goal[0])
            else:
                reach_paths.extend(paths_to_goal)
    if len(reach_paths) > 0:
        return True, reach_paths
    return False, steps

with open("start_conf.txt", "r") as file_content:
    lines = file_content.readlines()

width = len(lines[0])-1
height = len(lines)

playfield = [[0 for x in range(width)] for y in range(height)]
units = []

timer = Timer()
timer_str = "step {} took {}s"

for y, line in enumerate(lines):
    line = line.strip()
    for x, ch in enumerate(line):
        if ch == '#':
            playfield[y][x] = pf_wall
        elif ch == '.':
            playfield[y][x] = pf_free
        elif ch == 'G':
            units.append(Unit((x,y), pf_goblin))
            playfield[y][x] = pf_goblin
        elif ch == 'E':
            units.append(Unit((x,y), pf_elf))
            playfield[y][x] = pf_elf
        else:
            raise

end = False
remove_list = []
stored_round = 0
mem = {}
for round_number in range (100):
    # raw_input("Press Enter to continue...")

    for remove_this in remove_list:
        units.remove(remove_this)
    units = sorted(units, key=unit_sort)

    vis()
    if end:
        print ("end at round {}".format(round_number-1))
        print ("{} units alive".format(len(units)))
        hp_sum = 0
        for unit in units:
            hp_sum += unit.hp
        print ("end at round {}, result is {}".format(round_number-1, (round_number-1)*hp_sum))
        break
    remove_list = []
    reachable_cache = {}
    for unit in copy.copy(units):
        if unit.pos == (2,1):
            pass
        # timer.start_timer()
        if unit.hp < 1:
            print ("ERROR DEAD MAN WALKING")
            continue

        targets = list(filter(lambda x: x.faction != unit.faction, units))
        if len(targets) == 0:
            end = True
            break

        open_target_spaces = []
        in_range = False
        for target in targets:
            spaces = [
                (target.pos[0]+1, target.pos[1]  ),
                (target.pos[0]-1, target.pos[1]  ), 
                (target.pos[0]  , target.pos[1]+1), 
                (target.pos[0]  , target.pos[1]-1)
            ]
            spaces = list(filter(lambda x: playfield[x[1]][x[0]] == pf_free or unit.pos == x, spaces))
            open_target_spaces.extend(spaces)

        # timer.stop_timer(timer_str, "open_spaces")

        if not unit.pos in open_target_spaces:
            reachable_target_spaces = []
            for space in open_target_spaces:
                # timer.start_timer()

                reachable, steps_to_goal = None, None
                if (unit.pos, space) in reachable_cache.keys():
                    reachable, steps_to_goal = reachable_cache[(unit.pos, space)]
                else:
                    reachable, steps_to_goal = is_reachable(unit.pos, space, round=round_number)
                    reachable_cache[(unit.pos, space)] = (reachable, steps_to_goal)


                # eachable_old, steps_to_goal_old = is_reachable_old(unit.pos, space)
                # a = True
                # for path in steps_to_goal_old:
                #     a = a and path in steps_to_goal
                # for path in steps_to_goal:
                #     a = a and path in steps_to_goal_old
                # if not a and unit.pos == (4,2):
                #     print ("from {} to {}".format(unit.pos, space))
                #     print (steps_to_goal_old)
                #     print steps_to_goal
                #     raise
                # timer.stop_timer(timer_str, "reachable")
                # print steps_to_goal
                if reachable:
                    reachable_target_spaces.append((space, steps_to_goal))

            if len(reachable_target_spaces) == 0:
                continue

            reachable_target_spaces = sorted(reachable_target_spaces, key=lambda x: len(x[1][0]))

            min_steps = len(reachable_target_spaces[0][1][0])
            nearest_spaces = []

            for i in range(len(reachable_target_spaces)):
                if len(reachable_target_spaces[i][1][0]) == min_steps:
                    nearest_spaces.append(reachable_target_spaces[i][0])

            nearest_spaces = sorted(nearest_spaces, key=pos_sort)

            unit_goal = nearest_spaces[0]

            if unit_goal != unit.pos:
                _, paths = None, None
                if (unit.pos, unit_goal) in reachable_cache.keys():
                    _, paths = reachable_cache[(unit.pos, unit_goal)]
                else:
                    _, paths = is_reachable(unit.pos, unit_goal, round=round_number)
                    reachable_cache[(unit.pos, unit_goal)] = (_, paths)

                step = None
                first_steps = [path[0] for path in paths]
                first_steps = sorted(first_steps, key=pos_sort)

                step_target = first_steps[0]

                playfield[unit.pos[1]][unit.pos[0]] = pf_free
                unit.pos = step_target
                playfield[unit.pos[1]][unit.pos[0]] = unit.faction

        attackable_targets = []
        for enemy in targets:
            if abs(enemy.pos[0] - unit.pos[0]) + abs(enemy.pos[1] - unit.pos[1]) < 2:
                attackable_targets.append(enemy)
                # print ("{} can attack {}".format(unit.pos, enemy.pos))
        if len(attackable_targets) == 0:
            continue

        sorted_targets = sorted(attackable_targets, key=lambda x: x.hp)
        min_hp = sorted_targets[0].hp
        min_hp_targets = []
        for enemy in sorted_targets:
            if enemy.hp == min_hp:
                min_hp_targets.append(enemy)

        sorted_min_hp_targets = sorted(min_hp_targets, key=unit_sort)
        # print ("{} attacks target at: {} with {} hp".format(unit.pos, sorted_min_hp_targets[0].pos, sorted_min_hp_targets[0].hp))
        target = sorted_min_hp_targets[0]
        target.hp -= unit.ap
        if target.hp < 1:
            playfield[target.pos[1]][target.pos[0]] = pf_free
            # remove_list.append(target)
            units.remove(target)
vis()
