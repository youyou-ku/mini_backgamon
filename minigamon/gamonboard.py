from minigamon.boardchange import boardchange
from minigamon.dice import dice
from minigamon.winnermake import winnercheck


board = [0 for _ in range(10)]
board[1:4] = [2, 2, 2]
board[-4:-1] = [-2, -2, -2]
t = 1
while True:
    print(board[1:-1])
    print(board[0], board[-1])
    p = dice()
    for i in p:
        n = int(input())
        q = 0
        if t == 1:
            q = n
        elif t == -1:
            q = -1-n
        if board[q] * t > 0:
            board = boardchange(board, t, n, i)
            print(board[1:-1])
            print(board[0], board[-1])
        else:
            print("You can't choose it")
    if winnercheck(board, 6, t):
        print("You Win!!")
        break
    else:
        t *= -1
        print("Take turns.")

