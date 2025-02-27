def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_groups:
                anagram_groups[canonical_form].append(word)
            else:
                anagram_groups[canonical_form] = [word]
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(group) // 2
    return anagram_count <= 92