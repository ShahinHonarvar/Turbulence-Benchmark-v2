from collections import defaultdict

def if_contains_anagrams(lst):

    def hash_anagram(word):
        return ''.join(sorted(word.lower()))
    anagrams_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_key = hash_anagram(word)
            anagrams_count[anagram_key] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return total_pairs <= 277