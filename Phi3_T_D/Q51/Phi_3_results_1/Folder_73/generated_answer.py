from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        freqs = defaultdict(int)
        for char in s.lower():
            if 'a' <= char <= 'z':
                freqs[char] += 1
        return freqs
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            frequency_count = frozenset(count_letters(string).items())
            anagram_counts[frequency_count] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 279