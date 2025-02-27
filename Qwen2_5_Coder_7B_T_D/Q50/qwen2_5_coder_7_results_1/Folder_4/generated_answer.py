from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(word):
        return Counter(sorted(word))
    anagram_pairs = 0
    seen = {}
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        anagram_count = count_anagrams(string)
        if anagram_count in seen:
            anagram_pairs += seen[anagram_count]
            seen[anagram_count] += 1
        else:
            seen[anagram_count] = 1
    return anagram_pairs >= 42