from collections import defaultdict, Counter

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            word_lowercase = word.lower()
            sorted_word = ''.join(sorted(word_lowercase))
            anagram_dict[sorted_word].append(word)
    anagram_count = sum((1 for anagrams in anagram_dict.values() if len(anagrams) >= 2))
    return anagram_count >= 55