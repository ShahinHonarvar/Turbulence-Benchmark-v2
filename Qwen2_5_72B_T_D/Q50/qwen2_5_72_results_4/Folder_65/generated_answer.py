from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagrams = Counter([''.join(sorted(word)) for word in words if len(word) >= 3])
    return sum((count * (count - 1) // 2 for count in anagrams.values())) >= 94