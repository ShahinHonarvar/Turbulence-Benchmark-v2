from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_dict = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 475