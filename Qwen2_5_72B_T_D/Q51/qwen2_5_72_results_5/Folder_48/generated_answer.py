from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_count[normalized_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 277