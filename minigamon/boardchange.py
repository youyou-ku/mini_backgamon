def boardchange(board, t, n: int, a: int):
    l = len(board)-2
    if t == 1:
        board[n] -= 1
        if n + a <= l:
            board[n+a] += 1
        else:
            board[-2] += 1
    elif t == -1:
        board[-1-n] += 1
        if n + a <= l:
            board[-1-n-a] -= 1
        else:
            board[1] -= 1
    return board
