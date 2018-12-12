num_generations = 20000
print_every = 2000

with open("pots_and_rules.txt", "r") as file_input:
    pots_and_rules = file_input.readlines()

pots_text = pots_and_rules[0].split(' ')[2]
rules_text = pots_and_rules[2:]

def viz(cur):
    print ''.join('#' if i in cur else '.' for i in xrange(-3, 40))

pots = [i for i, c in enumerate(pots_text[:-1]) if c=='#']

rules = []
for rule_text in rules_text:
    if rule_text[-2] == "#":
        rules.append(rule_text[:5])

print (sum(pots))
prev = sum(pots)
for gen in xrange(0,num_generations):

    next_gen = set()

    start = min(pots)
    end = max(pots)

    for out_val in xrange(start-3, end+4):

        matched_res = '.'
        

        pat = "".join('#' if i in pots else '.' for i in xrange(out_val-2, out_val+3) )
        if pat in rules:
            next_gen.add(out_val)

    pots = next_gen
    if (gen+1) % print_every == 0:
        print (gen+1, sum(pots), sum(pots)-prev)
        prev = sum(pots)


# part 2:
# observations:
# after 10000: 320328
# every 2000: + 64000
# thus 320328 + (50000000000 - 10000)/2000 * 64000 = 1600000000328
