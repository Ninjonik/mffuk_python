import sys

def seskup(it, klic):
    groups = {}
    for item in it:
        k = klic(item)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return list(groups.values())


def normalize(s):
    clean = ''.join(ch for ch in s if ch.isalnum())
    return ''.join(sorted(clean.casefold()))

def normalize_no_sort(s):
    clean = ''.join(ch for ch in s if ch.isalnum())
    return clean.casefold()

radky = []
for radek in sys.stdin:
    radek = radek.rstrip("\r\n")
    radky.append(radek)

unique_map = {}
for radek in radky:
    key = normalize_no_sort(radek)
    if key not in unique_map or radek < unique_map[key]:
        unique_map[key] = radek

unique_radky = list(unique_map.values())

groups = seskup(unique_radky, normalize)

anagram_groups = []
for group in groups:
    if len(group) > 1:
        anagram_groups.append(sorted(group))

anagram_groups.sort(key=lambda g: g[0])

if not anagram_groups:
    sys.exit(1)

for i, group in enumerate(anagram_groups):
    if i > 0:
        print()
    for item in group:
        print(item)
