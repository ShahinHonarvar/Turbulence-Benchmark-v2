from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_count[sorted_word] += 1
    count = sum((1 for count in anagram_count.values() if count > 1))
    return count <= 78