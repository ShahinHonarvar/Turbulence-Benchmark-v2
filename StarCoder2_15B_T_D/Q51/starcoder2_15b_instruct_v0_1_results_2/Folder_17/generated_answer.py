def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if canonical_word in anagram_groups:
            anagram_groups[canonical_word].append(word)
        else:
            anagram_groups[canonical_word] = [word]
    num_anagram_groups = sum((len(group) >= 2 for group in anagram_groups.values()))
    return num_anagram_groups <= 2