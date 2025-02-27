from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    count = sum((1 for v in anagrams.values() if len(v) > 1 for i in range(len(v)) for j in range(i + 1, len(v))))
    return count >= 46