import copy

with open("tracks.txt", "r") as file_content:
    lines = file_content.readlines()
    track_map = []
    for line in lines:
        track_map.append(line.splitlines()[0])

# track_map = ["->---<--"]
# print(track_map)
# track_map = [
# "/->-\        ",
# "|   |  /----\\",
# "| /-+--+-\  |",
# "| | |  | v  |",
# "\-+-/  \-+--/",
# "  \------/   "
# ]
# print(state[0])
line_len = len(track_map[0])

class Cart:
    def __init__(self, start_pos, facing, ID):
        self.pos = start_pos
        self.facing = facing
        self.turns = [-1, 0, 1]
        self.num_turns = 0
        self.ID = ID

    def move(self, track_map, carts):
        x, y = self.pos
        if self.facing == 0:
            new_pos = (x, y-1)
        elif self.facing == 1:
            new_pos = (x+1, y)
        elif self.facing == 2:
            new_pos = (x, y+1)
        elif self.facing == 3:
            new_pos = (x-1, y)

        if track_map[new_pos[1]][new_pos[0]] in ['-', '|']:
            self.pos = new_pos
        elif track_map[new_pos[1]][new_pos[0]] == '\\':
            self.pos = new_pos
            dir_modder = 1 if self.facing in [1,3] else -1
            self.facing = (self.facing+dir_modder) % 4
        elif track_map[new_pos[1]][new_pos[0]] == '/':
            self.pos = new_pos
            dir_modder = -1 if self.facing in [1,3] else 1
            self.facing = (self.facing+dir_modder) % 4
        elif track_map[new_pos[1]][new_pos[0]] == '+':
            self.pos = new_pos
            turn = self.turns
            self.facing = (self.facing + self.turns[self.num_turns % len(self.turns)]) % 4
            self.num_turns += 1
        else:
            raise
        # if cart_id == 1:
        # print("id {}: new_pos {}, new_facing: {}".format(self.ID, new_pos, self.facing))

        for cart in carts:
            if cart.pos == new_pos and cart.ID != self.ID:
                return (True, new_pos, cart)

        return (False, new_pos, None)

carts = []
cart_id = 0
for l_nr, line in enumerate(track_map):
    for c_nr, char in enumerate(line):
        if char == '^':
            carts.append(Cart((c_nr, l_nr), 0, cart_id))
            cart_id += 1
            print("add cart at {}, facing {}".format((c_nr, l_nr), 0))
        elif char == '>':
            carts.append(Cart((c_nr, l_nr), 1, cart_id))
            cart_id += 1
            print("add cart at {}, facing {}".format((c_nr, l_nr), 1))
        elif char == 'v':
            carts.append(Cart((c_nr, l_nr), 2, cart_id))
            cart_id += 1
            print("add cart at {}, facing {}".format((c_nr, l_nr), 2))
        elif char == '<':
            carts.append(Cart((c_nr, l_nr), 3, cart_id))
            cart_id += 1
            print("add cart at {}, facing {}".format((c_nr, l_nr), 3))

    track_map[l_nr] = track_map[l_nr].replace('^', '|')
    track_map[l_nr] = track_map[l_nr].replace('>', '-')
    track_map[l_nr] = track_map[l_nr].replace('v', '|')
    track_map[l_nr] = track_map[l_nr].replace('<', '-')

# PART 1

# crash = None
# crashed = False
# i = 0
# while (not crashed):
#     for cart_id, cart in enumerate(carts):
#         cart_crashed, crash_pos, second_cart = cart.move(track_map, carts, cart_id=cart_id)
#         if cart_crashed:
#             print(i, crash_pos)
#             crashed = True
#             break
#     i += 1
#     carts.sort(key=lambda x: x.pos[0]+x.pos[1]*line_len)

# PART 2
i = 0
while (True):
    # print ("\n\nstart frame {}".format(i))
    crashed_carts = set()
    for cart_id, cart in enumerate(carts):
        cart_crashed, crash_pos, second_cart = cart.move(track_map, carts)
        if cart_crashed:
            crashed_carts.add(cart)
            crashed_carts.add(second_cart)
    for crashed_cart in crashed_carts:
        carts.remove(crashed_cart)
    i += 1
    carts.sort(key=lambda x: x.pos[0]+x.pos[1]*line_len)
    if len(carts) < 2:
        break

print carts[0].pos