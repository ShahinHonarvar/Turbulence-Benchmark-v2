from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = [v for v in anagram_dict.values() if len(v) > 1]
    return sum((len(v) * (len(v) - 1) // 2 for v in anagram_pairs)) >= 108