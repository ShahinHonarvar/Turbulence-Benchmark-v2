from collections import Counter

def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    word_counts = Counter(sorted_words)
    return sum((count * (count - 1) // 2 for count in word_counts.values())) >= 11