from collections import Counter

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            count = Counter(word)
            key = tuple((count[ch] for ch in 'abcdefghijklmnopqrstuvwxyz'))
            anagrams[key] = anagrams.get(key, []) + [word]
    return len(anagrams) <= 91