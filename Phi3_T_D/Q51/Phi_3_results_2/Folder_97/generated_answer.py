from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            letters_tuple = count_letters(s)
            anagram_map[letters_tuple] += 1
    return sum((count * (count - 1) // 2 for count in anagram_map.values())) <= 18