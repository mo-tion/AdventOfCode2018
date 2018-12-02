import sys

with open("frequencies.txt", "r") as freq_file:
    content = freq_file.readlines()

start_freq = 0
freq_list = set({})

freq = start_freq
num_runs = 0

while(True):
    for line in content:
        line = line.replace('\n', '')
    
        operator = line[0]
        value = int(line[1:])
    
        if operator == '+':
            freq = freq + value
        elif operator == '-':
            freq = freq - value
        else:
            raise

        if freq in freq_list:
            print(freq)
            sys.exit(100)
        else:
            freq_list.add(freq)
    num_runs += 1
    print("num runs: {}".format(num_runs))
