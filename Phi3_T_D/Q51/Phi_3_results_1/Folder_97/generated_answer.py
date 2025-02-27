from collections import defaultdict

def if_contains_anagrams(lst):

    def count_chars(word):
        return ''.join(sorted(word.lower().replace(' ', '')))
    anagram_counts = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_key = count_chars(word)
            anagram_counts[anagram_key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 18