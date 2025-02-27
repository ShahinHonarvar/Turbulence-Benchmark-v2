from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """
    Returns True if there are at most 91 pairs of anagrams in the given list of words;
    otherwise, returns False. Anagrams are considered only for the English letters, and
    only words of length at least three are considered. The comparison is case-insensitive.
    """
    anagram_groups = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3 and all((c.isalpha() for c in word)):
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
    num_anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return num_anagram_pairs <= 91