def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_groups:
                anagram_groups[canonical_form].append(word)
            else:
                anagram_groups[canonical_form] = [word]
    num_anagrams = sum((len(group) for group in anagram_groups.values()))
    return num_anagrams <= 66