def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = {}
    for word in strings:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_pairs:
            anagram_pairs[normalized].append(word)
        else:
            anagram_pairs[normalized] = [word]
    count = 0
    for value in anagram_pairs.values():
        if len(value) >= 2:
            count += len(value) // 2
    return count <= 8