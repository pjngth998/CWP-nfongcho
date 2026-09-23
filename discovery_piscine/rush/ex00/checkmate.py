def scan(occupied, me, directions, size, max_steps=None):
    for (r, c), name in occupied.items():
        if name == me:
            row = r
            col = c

    if max_steps is None:
        max_steps = size

    for step in range(1, max_steps + 1):
        found_other = False
        for dr, dc in directions:
            r = row + dr * step
            c = col + dc * step
            if 0 <= r < size and 0 <= c < size and (r, c) in occupied:
                if occupied[(r, c)] == "K":
                    return 1
                found_other = True
        if found_other:
            return 0
    return 0


STRAIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def checkmate(board):
    rows = board.split()
    table = [list(row) for row in rows]
    size = len(table)

    for row in table:
        if len(row) != size:
            return "failed"

    occupied = {}
    for r in range(size):
        for c in range(size):
            if table[r][c] in ("P", "B", "R", "Q", "K"):
                occupied[(r, c)] = table[r][c]

    if "K" not in occupied.values():
        return "failed"

    p_can = 0
    b_can = 0
    r_can = 0
    q_can = 0

    if "P" in occupied.values():
        p_can = scan(occupied, "P", [(-1, -1), (-1, 1)], size, max_steps=1)
    if "B" in occupied.values():
        b_can = scan(occupied, "B", DIAGONAL, size)
    if "R" in occupied.values():
        r_can = scan(occupied, "R", STRAIGHT, size)
    if "Q" in occupied.values():
        q_can = scan(occupied, "Q", STRAIGHT + DIAGONAL, size)

    if p_can + b_can + r_can + q_can > 0:
        return "success"
    return "failed"

