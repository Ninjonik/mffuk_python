import sys

slova, hledana = map(lambda val: val.split(" "), sys.stdin)

super_slovnik = {}
for index, slovo in enumerate(slova):
    if slovo in super_slovnik:
        super_slovnik[slovo].append(index)
    else:
        super_slovnik[slovo] = [index]

for slovo in hledana:
    print(f"{slovo.rstrip('\n')} {" ".join(str(index) for index in super_slovnik[slovo]) if slovo in super_slovnik else '-1'}")

