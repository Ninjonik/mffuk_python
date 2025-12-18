"""
Napište program, který jako vstup dostane posloupnost závorek (()[]{}<>) a rozhodne, jestli je uzávorkování platné.
Vypište True, pokud je uzávorkování v pořádku, tedy pokud ke každé otevírací závorce existuje uzavírací závorka
 a různé typy závorek se nekříží. Pokud řetězec závorek platný není, vypište False.

Můžete použít implementaci zásobníku z přednášky nebo ze cvičení.

Příklad:

    Pro vstup <>[{}()]() máte vypsat True.
    Pro vstup {}([])) máte vypsat False.

"""

vstup = input()
vstup_len = len(vstup)

braces = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
}

braces_keys = braces.keys()
braces_values = braces.values()

is_valid = True

table = []

if vstup_len %2 != 0:
    is_valid = False
else:
    # check if pairs of braces exist
    taken = []

    for i in range(vstup_len):
        start = vstup[i]
        if start in braces_keys:
            for j in range(i, vstup_len):
                if j in taken:
                    continue
                potential_end = vstup[j]
                if braces[start] == potential_end:
                    taken.append(j)
                    break

    for i in range(vstup_len):
        start = vstup[i]

        if start in braces_keys:
            end = None

            same_starts_in_between = []
            for j in range(i, vstup_len):
                char = vstup[j]

                # char is the same class as start
                if char == start:
                    same_starts_in_between.append(char)
                # char is of the same class as start as an end
                elif char == braces[start]:
                    if len(same_starts_in_between) > 0:
                        same_starts_in_between.pop()
                    else:
                        end = char
                        break
                # char is a start
                elif char in braces_keys:
                    pass
                # char is an end
                elif char in braces_values:
                    pass


             # either something in between misses a closing parenthesis or the start itself does
            if len(same_starts_in_between) > 1 or not end:
                is_valid = False
                break



            starts_before = []
            for j in range(0, i + 1):
                if vstup[j] in braces_keys:
                    starts_before.append(vstup[j])

            for j in range(len(starts_before)):
                pass


print(is_valid)
