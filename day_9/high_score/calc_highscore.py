import numpy as np

num_players = 458
num_marbles = 7201900

current_marble = 0
board = [0]

scoreboard = np.zeros(num_players)

def place_marble(board, current_marble, next_marble):
    # if current_marble == -1:
    #     board.append(next_marble)
    #     current_marble = 0
    #     return board, current_marble, 0

    if next_marble % 23 == 0:
        score = next_marble
        pop_index = (current_marble-7) % len(board)
        score += board.pop(pop_index)
        return board, pop_index % len(board), score


    new_pos = (current_marble+2) % len(board)
    current_marble = new_pos
    board.insert(new_pos, next_marble)
    return board, current_marble, 0

for marble in range(1, num_marbles+1):
    board, current_marble, score = place_marble(board, current_marble, marble)
    scoreboard[(marble-1)%num_players] += score
    # print (marble-1)%num_players+1, board, current_marble

print (np.argmax(scoreboard)+1, np.max(scoreboard))