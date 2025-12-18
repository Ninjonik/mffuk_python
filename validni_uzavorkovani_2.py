vstup = input()
length = len(vstup)

braces = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
}

braces_keys = braces.keys()
braces_values = braces.values()

is_valid = True
if length % 2 != 0:
    is_valid = False
else:
    arr = []
    for i in range(length):
        char = vstup[i]

        if char in braces_keys:
            arr.append(char)
        elif char in braces_values:
            if len(arr) < 1:
                is_valid = False
                break

            for j in range(len(arr)):
                if len(arr) < 1:
                    is_valid = False
                    break
                start_char = arr[-1]
                if start_char in braces_keys and braces[start_char] == char:
                    arr.pop()
                    break
                else:
                    arr.pop()

    if len(arr) > 0:
        is_valid = False

print(is_valid)