import sys

slova, hledana = map(lambda val: val.split(" "), sys.stdin)

dict = {}
for index, slovo in enumerate(reversed(slova)):
    dict[slovo] = index

for slovo in hledana:
    print(f"{slovo} {dict[slovo] if slovo in dict else '-1'}")


