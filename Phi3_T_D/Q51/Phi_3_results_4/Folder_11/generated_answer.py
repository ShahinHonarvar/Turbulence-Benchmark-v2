from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for word in lst:
        word_key = ''.join(sorted(word.lower()))
        anagrams[word_key] += 1
    count = 0
    for key in anagrams:
        if anagrams[key] >= 2:
            count += anagrams[key] // 2
    return count <= 41