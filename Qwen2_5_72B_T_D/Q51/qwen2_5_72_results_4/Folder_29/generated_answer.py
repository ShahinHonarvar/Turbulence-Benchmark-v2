from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    pairs = 0
    for count in anagram_dict.values():
        pairs += count * (count - 1) // 2
    return pairs <= 318