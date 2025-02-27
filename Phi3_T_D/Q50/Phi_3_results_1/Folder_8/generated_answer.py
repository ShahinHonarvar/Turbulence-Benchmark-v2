from collections import defaultdict

def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words]
    anagram_counts = defaultdict(int)
    for word in sorted_words:
        anagram_counts[word] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 85