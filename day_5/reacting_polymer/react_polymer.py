with open("polymer.txt", "r") as freq_file:
    polymer = freq_file.readlines()[0]

while True:
    reduced = False
    new_polymer = ""
    last_char = None
    for i, ch in enumerate(polymer):
        if last_char is not None:
            if ch is not last_char and (ch.lower() == last_char.lower() or ch.upper() == last_char.upper()):
                reduced = True
                last_char = None
            else:
                new_polymer += last_char
                last_char = ch
        else:
            last_char = ch
    if last_char is not None:
        new_polymer+=last_char
    polymer = new_polymer
    if not reduced:
        break

print(len(polymer))