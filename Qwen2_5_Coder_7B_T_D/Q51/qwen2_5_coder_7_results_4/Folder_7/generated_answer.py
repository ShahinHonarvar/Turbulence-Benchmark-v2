from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            count = [0] * 26
            for char in s.lower():
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 445