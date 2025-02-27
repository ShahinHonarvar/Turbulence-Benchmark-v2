def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if canonical_word not in anagram_groups:
            anagram_groups[canonical_word] = [word]
        else:
            anagram_groups[canonical_word].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values()]
    return sum((1 for count in anagram_counts if count >= 2)) <= 4