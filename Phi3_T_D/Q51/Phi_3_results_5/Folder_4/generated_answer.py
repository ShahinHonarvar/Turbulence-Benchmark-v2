from collections import defaultdict

def if_contains_anagrams(lst):

    def count_letters(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagrams[count_letters(word)] += 1
    return sum((x * (x - 1) // 2 for x in anagrams.values())) <= 84