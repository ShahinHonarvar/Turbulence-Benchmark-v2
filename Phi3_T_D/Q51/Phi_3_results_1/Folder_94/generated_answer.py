from itertools import combinations
    import collections

def if_contains_anagrams(strings):

    def count_letters(s):
        return sorted(((char.lower(), count) for char, count in collections.Counter(s).items() if char.isalpha()))

    def is_anagram(a, b):
        return count_letters(a) == count_letters(b)
    anagram_count = sum((1 for pair in combinations(strings, 2) if is_anagram(pair[0], pair[1]) and len(pair[0]) >= 3 and (len(pair[1]) >= 3)))
    return anagram_count <= 181