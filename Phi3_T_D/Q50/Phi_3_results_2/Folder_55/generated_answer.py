from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(words):
    three_long = [word for word in words if len(word) >= 3]
    anagram_dict = defaultdict(list)
    for word in three_long:
        canonical = ''.join(sorted(word.lower()))
        anagram_dict[canonical].append(word)
    anagram_count = 0
    seen = set()
    for key, anagrams in anagram_dict.items():
        for i, word1 in enumerate(anagrams):
            for word2 in anagrams[i + 1:]:
                if (word1, word2) not in seen and (word2, word1) not in seen:
                    seen.add((word1, word2))
                    anagram_count += 1
    return anagram_count >= 15