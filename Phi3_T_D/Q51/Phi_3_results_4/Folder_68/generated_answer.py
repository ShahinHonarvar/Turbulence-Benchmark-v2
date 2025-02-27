from collections import Counter

def if_contains_anagrams(words):
    stord_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    count = Counter(stord_words)
    return sum((1 for c in count.values() if c >= 2)) <= 94