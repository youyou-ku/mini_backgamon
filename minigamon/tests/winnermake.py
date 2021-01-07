def winnercheck(board, n, t):
    """
    >>> winnercheck([0, -3, -4, -1, 0, 0, 2, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0], 8, -1)
    True
    >>> winnercheck([0, -3, -4, -1, 0, 0, 2, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0], 10, -1)
    False
    >>> winnercheck([0, -3, -4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 0], 8, 1)
    True
    """
    if t == 1:
        p = [board[-2-i] for i in range(3) if board[-2-i] > 0]
        for i in p:
            n -= p[i]
    elif t == -1:
        p = [board[1+i] for i in range(3) if board[1+i] < 0]
        for i in p:
            n += p[i]
    if n == 0:
        return True
    else:
        return False
