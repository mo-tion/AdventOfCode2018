import copy


def addr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] + state[instr[1]]
        return state
    except IndexError:
        return None


def addi(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] + instr[1]
        return state
    except IndexError:
        return None


def mulr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] * state[instr[1]]
        return state
    except IndexError:
        return None


def muli(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] * instr[1]
        return state
    except IndexError:
        return None


def banr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] & state[instr[1]]
        return state
    except IndexError:
        return None


def bani(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] & instr[1]
        return state
    except IndexError:
        return None


def borr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] | state[instr[1]]
        return state
    except IndexError:
        return None


def bori(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]] | instr[1]
        return state
    except IndexError:
        return None


def setr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = state[instr[0]]
        return state
    except IndexError:
        return None


def seti(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = instr[0]
        return state
    except IndexError:
        return None


def gtir(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if instr[0] > state[instr[1]] else 0
        return state
    except IndexError:
        return None


def gtri(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if state[instr[0]] > instr[1] else 0
        return state
    except IndexError:
        return None


def gtrr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if state[instr[0]] > state[instr[1]] else 0
        return state
    except IndexError:
        return None


def eqir(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if instr[0] == state[instr[1]] else 0
        return state
    except IndexError:
        return None


def eqri(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if state[instr[0]] == instr[1] else 0
        return state
    except IndexError:
        return None


def eqrr(state, instr):
    state = copy.deepcopy(state)
    try:
        state[instr[2]] = 1 if state[instr[0]] == state[instr[1]] else 0
        return state
    except IndexError:
        return None


operations = [(addr, "addr"), (addi, "addi"), (mulr, "mulr"), (muli, "muli"), (banr, "banr"), (bani, "bani"),
              (borr, "borr"), (bori, "bori"), (setr, "setr"), (seti, "seti"), (gtir, "gtir"), (gtri, "gtri"),
              (gtrr, "gtrr"), (eqir, "eqir"), (eqri, "eqri"), (eqrr, "eqrr")]

code_to_op = {
    0: eqir,
    1: addi,
    2: gtir,
    3: setr,
    4: mulr,
    5: seti,
    6: muli,
    7: eqri,
    8: bori,
    9: bani,
    10: gtrr,
    11: eqrr,
    12: addr,
    13: gtri,
    14: borr,
    15: banr
}
