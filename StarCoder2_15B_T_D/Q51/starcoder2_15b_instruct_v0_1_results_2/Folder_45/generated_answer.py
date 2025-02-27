import collections

def if_contains_anagrams(words):
    anagrams = collections.defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3 and all((word.count(ch) == word.count(ch) for ch in set(word))):
            anagrams[tuple(sorted(word))].append(word)
    return len(anagrams) <= 464