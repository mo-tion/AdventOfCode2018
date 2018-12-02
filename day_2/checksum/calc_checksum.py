with open("box_ids.txt", "r") as freq_file:
    content = freq_file.readlines()

num_twos = 0
num_threes = 0

for id in content:
    char_dict = {}
    found_two = False
    found_three = False

    for ch in id:
        if not ch in char_dict.keys():
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1

    for ch, num in char_dict.iteritems():
        if num == 2 and not found_two:
            num_twos += 1
            found_two = True
        if num == 3 and not found_three:
            num_threes += 1
            found_three = True

print(num_twos * num_threes)
