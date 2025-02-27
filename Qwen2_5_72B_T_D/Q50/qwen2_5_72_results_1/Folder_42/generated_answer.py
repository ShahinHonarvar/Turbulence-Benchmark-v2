from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst]
    sorted_words = [''.join(sorted(word)) for word in lst if len(word) >= 3]
    counts = Counter(sorted_words)
    pairs = 0
    for count in counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 233