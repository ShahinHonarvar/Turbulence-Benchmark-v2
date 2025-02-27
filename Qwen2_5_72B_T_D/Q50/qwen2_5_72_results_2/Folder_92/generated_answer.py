from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    groups = Counter((''.join(sorted(word)) for word in words))
    return sum((count >= 2 for count in groups.values())) >= 2