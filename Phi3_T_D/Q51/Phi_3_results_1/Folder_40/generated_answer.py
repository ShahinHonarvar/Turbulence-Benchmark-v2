from collections import defaultdict

def if_contains_anagrams(strings):

    def get_sorted_tuple(s):
        return tuple(sorted((c.lower() for c in s if c.isalpha())))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_tuple = get_sorted_tuple(s)
            anagram_count[sorted_tuple] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 29