from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_words = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    anagram_counts = defaultdict(int)
    for word in sorted_words:
        anagram_counts[word] += 1
    return sum((1 for count in anagram_counts.values() if count >= 2)) >= 10