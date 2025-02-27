from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagrams = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            sorted_word = ''.join(sorted(w))
            anagrams[sorted_word].append(w)
    for group in anagrams.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
            if anagram_count > 113:
                return False
    return True