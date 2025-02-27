from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagrams = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    for group in anagrams.values():
        anagram_count += len(group) * (len(group) - 1) // 2
        if anagram_count > 188:
            return False
    return True