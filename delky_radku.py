import sys

zoradene_riadky = sorted(sys.stdin, key=len)

merged = []
for riadok in zoradene_riadky:
    if len(merged) < 1:
        merged.append([riadok])
        continue

    current = len(merged) - 1

    if len(merged[current]) > 0 and len(merged[current][0]) == len(riadok):
        merged[current].append(riadok)
    else:
        merged.append([riadok])

final = (sorted(merged, key=len, reverse=True))
for li in final:
    for riadok in li:
        print(riadok, end="")
    print("\n", end="")
