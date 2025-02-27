from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = Counter((normalize(word) for word in lst if len(word) >= 3))
    return sum((count * (count - 1) // 2 for count in anagrams.values())) >= 219