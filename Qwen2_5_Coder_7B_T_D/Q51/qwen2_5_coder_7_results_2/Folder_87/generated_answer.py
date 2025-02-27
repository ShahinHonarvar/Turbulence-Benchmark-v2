from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word.isalpha():
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key in anagram_dict:
        count = len(anagram_dict[key])
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 392