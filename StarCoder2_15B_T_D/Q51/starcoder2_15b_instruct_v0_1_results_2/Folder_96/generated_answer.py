import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 2:
                    return False
    return anagram_pairs <= 2

def is_anagram(s1, s2):
    s1 = ''.join((c for c in s1.lower() if c.isalpha()))
    s2 = ''.join((c for c in s2.lower() if c.isalpha()))
    if len(s1) != len(s2):
        return False
    counts = collections.Counter(s1)
    for c in s2:
        if c not in counts or counts[c] == 0:
            return False
        counts[c] -= 1
    return all((count == 0 for count in counts.values()))