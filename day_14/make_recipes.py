start = "37"
index_1 = 0
index_2 = 1

find_after = 306281


def step(scoreboard, id_1, id_2, score_len=None):
    s_1 = int(scoreboard[id_1])
    s_2 = int(scoreboard[id_2])
    new_recipe = s_1 + s_2
    new_recipe = str(new_recipe)

    new_id_1 = (id_1+1+s_1)%(score_len+len(new_recipe))
    new_id_2 = (id_2+1+s_2)%(score_len+len(new_recipe))
    return scoreboard+new_recipe, new_id_1, new_id_2, score_len+len(new_recipe)

scoreboard = start

# PART 1

# start = time.time()
# for i in xrange(find_after+10):
#     if i % 1000 == 1:
#         start = time.time()
#     scoreboard, index_1, index_2 = step(scoreboard, index_1, index_2)
#     if i % 1000 == 0:
#         end = time.time()
#         print ("time for step {:6d}: {}".format(i, end-start))

# res = reduce(lambda x,y: str(x)+str(y), scoreboard[find_after:find_after+10])
# print(res)

# PART 2
tar_len = len(str(find_after))
length = len(scoreboard)
while str(find_after) not in scoreboard[-(tar_len+1):]:
    s_1 = int(scoreboard[index_1])
    s_2 = int(scoreboard[index_2])
    new_recipe = str(s_1+s_2)

    scoreboard += new_recipe

    index_1 = (index_1+1+s_1)%(len(scoreboard))
    index_2 = (index_2+1+s_2)%(len(scoreboard))
print (scoreboard.index(str(find_after)))
