from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagrams_count[normalize(word)] += 1
    return sum((count * (count - 1) // 2 for count in anagrams_count.values())) >= 136