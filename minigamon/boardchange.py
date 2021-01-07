def boardchange(board, t, n: int, a: int):
    """
    >>> boardchange([0, 2, 2, 2, 2, -2, -2, -2, -2, 0], 1, 3, 1)
    [0, 2, 2, 1, 3, -2, -2, -2, -2, 0]
    >>> boardchange([0, -3, 0, 0, 3, 2, -1, 0], -1, 1, 100)
    [0, -4, 0, 0, 3, 2, 0, 0]
    >>> boardchange([0, 2, 2, 2, 2, -2, -2, -1, -2, -1], 1, 4, 3)
    [0, 2, 2, 2, 1, -2, -2, 1, -2, -2]
    >>> boardchange([0, -3, 0, 0, 3, 1, -1, 0], -1, 1, 1)
    [1, -3, 0, 0, 3, -1, 0, 0]
    >>> boardchange([0, 2, 2, 2, 2, -2, -2, -1, -2, -1], 1, 4, 2)
    You can't
    [0, 2, 2, 2, 2, -2, -2, -1, -2, -1]
    """
    l = len(board)-2
    if t == 1:
        if n + a <= l:
            p = n + a
        else:
            p = -2
        if board[p] == -1:
            board[n] -= 1
            board[-1] -= 1
            board[p] = 1
        elif board[p] >= 0:
            board[n] -= 1
            board[p] += 1
        else:
            print("You can't")
    elif t == -1:
        if n + a <= l:
            p = -1-n-a
        else:
            p = 1
        if board[p] == 1:
            board[-1-n] += 1
            board[0] += 1
            board[p] = -1
        elif board[p] <= 0:
            board[-1-n] += 1
            board[p] -= 1
        else:
            print("You can't")
    return board
