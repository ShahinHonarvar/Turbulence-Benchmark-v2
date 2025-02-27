from collections import defaultdict

def if_contains_anagrams(words):

    def count_chars(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = count_chars(word)
            anagrams[key].append(word)
    pairs = sum([len(group) * (len(group) - 1) // 2 for group in anagrams.values()])
    return pairs <= 48