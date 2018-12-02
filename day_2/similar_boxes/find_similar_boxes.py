import sys
with open("box_ids.txt", "r") as freq_file:
    content = freq_file.readlines()

check_against = []
last_diff = -1
for number, id in enumerate(content):
    check_against.append(id)

    for number_2, id_2 in enumerate(check_against):
        num_diffs = 0
        last_diff = -1
        for i, ch in enumerate(id):
            if not ch == id_2[i]:
                num_diffs += 1
                lastdiff = i
        #if num_diffs > 1:
        #    continue;
        if num_diffs == 1:
            #print (id, id_2, number, number_2)
            print(id[0:last_diff-1]+id[last_diff:-1])
            sys.exit(100)
