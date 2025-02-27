from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagrams[w] += 1
            count += anagrams[w] - 1
    return count <= 401