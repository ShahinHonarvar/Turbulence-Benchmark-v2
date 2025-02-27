from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(string_list):

    def char_combo_generator(s):
        for k in range(3, len(s) + 1):
            for perm in permutations(s.lower(), k):
                yield ''.join(perm)
    anagram_counts = defaultdict(int)
    for string in string_list:
        for combo in char_combo_generator(string):
            anagram_counts[combo] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 188