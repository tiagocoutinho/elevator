def solve():
    floors = 1, 2, 3, 4, 5
    coopers = 2, 3, 4, 5
    bakers = 1, 2, 3, 4
    fletchers = 2, 3, 4

    def fletcher(fletcher, floors):
        cooper = floors[1]
        return fletcher not in (cooper - 1, cooper + 1)

    def smith(smith, floors):
        fletcher = floors[2]
        return smith not in (fletcher - 1, fletcher + 1)

    for s in floors:
        for c in coopers:
            for b in bakers:
                for f in fletchers:
                    for m in floors[c:]:
                        comb = (b, c, f, m, s)
                        if len(set(comb)) != 5:
                            continue
                        if fletcher(f, comb) and smith(s, comb):
                            return comb


assert solve() == (3, 2, 4, 5, 1)
