with open("frequencies.txt", "r") as freq_file:
    content = freq_file.readlines()

start_freq = 0

freq = start_freq

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

print freq
