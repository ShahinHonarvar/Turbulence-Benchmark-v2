from collections import defaultdict

def if_contains_anagrams(words):

    def count_letters(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_counts[count_letters(word)] += 1
    return sum((v - 1 for v in anagram_counts.values())) // 2 <= 85