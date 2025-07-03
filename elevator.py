def solve():
    floors = 1, 2, 3, 4, 5
    bakers = 1, 2, 3, 4
    coopers = 2, 3, 4, 5
    fletchers = 2, 3, 4
    smiths = floors

    for s in smiths:
        for c in coopers:
            if c == s:
                continue
            for b in bakers:
                if b == c or b == s:
                    continue
                for f in fletchers:
                    if f == b or f == c or f == s:
                        continue
                    if f == c - 1 or f == c + 1 or s == f - 1 or s == f + 1:
                        continue
                    for m in floors[c:]:
                        if m == b or m == s or m == f:
                            continue
                        return b, c, f, m, s


assert solve() == (3, 2, 4, 5, 1)
