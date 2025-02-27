from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(int)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            sorted_word = ''.join(sorted(w))
            anagrams[sorted_word] += 1
            count += anagrams[sorted_word] - 1
    return count >= 21