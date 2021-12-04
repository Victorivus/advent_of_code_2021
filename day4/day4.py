def processInput():
    pb_input = open("input.txt").read().splitlines()

    draw = pb_input.pop(0).split(',')

    boards = []
    transboards = []
    board = []
    for i in pb_input:
        if i != '':
            board.append(i.split())
        else:
            boards.append(board)
            transboards.append(list(map(list, zip(*board))))
            board = []
    boards.append(board)
    transboards.append(list(map(list, zip(*board))))
    boards.pop(0)  # remove first empty
    transboards.pop(0)  # remove first empty
    return draw, boards, transboards


# Part 1

draw, boards, transboards = processInput()
winner = ''
for i, x in enumerate(draw):
    for board in boards:
        for b in board:
            if set(b) <= set(draw[:i + 1]):
                winner = i
                print(f'The winner is board : {board} thanks to row {b}')
                break
            else:
                continue
        if winner:
            break
        else:
            continue
    if winner:
        break
    else:
        continue
    for board in transboards:
        for b in board:
            if set(b) <= set(draw[:i + 1]):
                winner = i
                print(f'The winner is board : {board} thanks to column {b}')
                break
            else:
                continue
        if winner:
            break
        else:
            continue
    if winner:
        break
    else:
        continue

board = [item for sublist in board for item in sublist]
score = sum(list(map(int, set(board) - set(draw[:i + 1])))) * int(draw[i])

print(f'The solution for part one is : {score}')

# Part 2

draw, boards, transboards = processInput()
winner = ''
last_winner = ''
last_board = ''
last_board_idx = ''
for i, x in enumerate(draw):
    for j, board in enumerate(boards):
        for b in board:
            if set(b) <= set(draw[:i + 1]):
                last_winner = winner = i
                last_board = board
                last_board_idx = j
                boards.pop(j)
                transboards.pop(j)
                break
            else:
                continue
        if winner:
            break
        else:
            continue
    if winner:
        winner = ''
        if len(boards) == 1:  # necessary to not have a fake "last board"
            break
    for j, board in enumerate(transboards):
        for b in board:
            if set(b) <= set(draw[:i + 1]):
                last_winner = winner = i
                last_board = board
                last_board_idx = j
                transboards.pop(j)
                boards.pop(j)
                break
            else:
                continue
        if winner:
            break
        else:
            continue
    if winner:
        winner = ''
    else:
        continue

print(f'\n\nThe last winning is board : {last_board}')
print(f'{last_winner + 1} drawn numbers : {draw[:last_winner + 1]}')

# board=last_board
board = [item for sublist in last_board for item in sublist]
score = sum(list(map(int, set(board) - set(draw[:last_winner + 1])))) * int(draw[last_winner])

print(f'The solution for part two is : {score}')
