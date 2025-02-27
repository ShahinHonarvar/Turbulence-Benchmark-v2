import itertools

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if len(canonical_word) >= 3:
            if canonical_word not in anagram_groups:
                anagram_groups[canonical_word] = []
            anagram_groups[canonical_word].append(word)
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(list(itertools.combinations(group, 2)))
    return anagram_count <= 475