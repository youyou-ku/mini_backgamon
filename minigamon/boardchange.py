def boardchange(board, t, n: int, a: int):
    """
    >>> boardchange([0, 2, 2, 2, 2, -2, -2, -2, -2, 0], 1, 3, 1)
    [0, 2, 2, 1, 3, -2, -2, -2, -2, 0]
    >>> boardchange([0, -8, 0, 0, 3, 2, 1, 0], 1, 4, 4)
    [0, -8, 0, 0, 2, 2, 2, 0]
    """
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
