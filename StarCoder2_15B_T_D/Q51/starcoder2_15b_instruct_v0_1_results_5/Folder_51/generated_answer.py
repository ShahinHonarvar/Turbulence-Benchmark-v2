import itertools

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_pairs += len(list(itertools.combinations(group, 2)))
    return anagram_pairs <= 116