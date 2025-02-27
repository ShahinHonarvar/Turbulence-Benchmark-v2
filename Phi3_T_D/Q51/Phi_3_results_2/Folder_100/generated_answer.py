from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    count = 0
    seen = set()
    for lst in anagrams.values():
        if len(lst) > 1:
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if (lst[i].lower(), lst[j].lower()) not in seen:
                        sorted_pair = tuple(sorted([lst[i].lower(), lst[j].lower()]))
                        seen.add(sorted_pair)
                        count += 1
    return count <= 98