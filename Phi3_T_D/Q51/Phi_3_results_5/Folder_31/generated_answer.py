from collections import defaultdict

def if_contains_anagrams(lst):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagrams[count_chars(word)] += 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) <= 65