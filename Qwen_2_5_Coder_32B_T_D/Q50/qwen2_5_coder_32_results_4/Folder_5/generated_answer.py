from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count >= 21:
            return True
    return False