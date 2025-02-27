from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word] += 1
    anagram_count = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_count >= 47