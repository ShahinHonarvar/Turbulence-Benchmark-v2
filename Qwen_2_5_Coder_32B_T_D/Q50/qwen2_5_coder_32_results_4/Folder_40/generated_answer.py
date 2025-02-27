from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_counts[sorted_word] += 1
    return sum((count >= 2 for count in anagram_counts.values())) >= 3