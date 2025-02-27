from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    count = 0
    words = [w.lower() for w in words if len(w) >= 3]
    sorted_words = [''.join(sorted(w)) for w in words]
    word_counts = Counter(sorted_words)
    for pair in combinations(word_counts.values(), 2):
        count += pair[0] * pair[1]
    return count >= 43