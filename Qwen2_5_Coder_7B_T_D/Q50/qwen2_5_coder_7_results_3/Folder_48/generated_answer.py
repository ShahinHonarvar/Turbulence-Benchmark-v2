from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagrams[sorted_chars(word)].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count >= 219