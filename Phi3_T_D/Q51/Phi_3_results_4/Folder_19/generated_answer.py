def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    anagrams = {}
    for s in lst:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 69