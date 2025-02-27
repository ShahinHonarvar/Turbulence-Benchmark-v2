import itertools

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        if len(canonical_form) >= 3:
            anagram_groups.setdefault(canonical_form, set()).add(word)
    return len(list(itertools.filterfalse(lambda g: len(g) <= 1, anagram_groups.values()))) <= 10