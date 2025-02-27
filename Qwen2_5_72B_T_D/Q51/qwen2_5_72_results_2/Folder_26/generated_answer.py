from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs_count <= 35