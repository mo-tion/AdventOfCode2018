import numpy as np

def react_polymer(polymer):
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

    return len(polymer)

with open("polymer.txt", "r") as freq_file:
    input_poly = freq_file.readlines()[0]

alphabet = map(chr, range(97, 123))
len_reacted = []

for ch in alphabet:
    reduced_poly = input_poly.replace(ch, '')
    reduced_poly = reduced_poly.replace(ch.upper(), '')
    len_reacted.append(react_polymer(reduced_poly))

print(np.min(np.array(len_reacted)))


