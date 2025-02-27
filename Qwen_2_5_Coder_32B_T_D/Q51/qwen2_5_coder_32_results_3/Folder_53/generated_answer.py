from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            anagram_counts[''.join(sorted(word))] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 8