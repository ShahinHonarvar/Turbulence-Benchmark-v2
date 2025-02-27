from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs <= 257