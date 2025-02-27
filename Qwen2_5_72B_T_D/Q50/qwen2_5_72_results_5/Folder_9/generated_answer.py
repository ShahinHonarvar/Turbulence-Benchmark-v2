from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in words]
    count = Counter(sorted_words)
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs >= 66