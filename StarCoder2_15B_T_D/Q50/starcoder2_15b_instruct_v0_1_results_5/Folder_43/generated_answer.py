def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    anagram_pairs = []
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            for i in range(len(anagram_group) - 1):
                for j in range(i + 1, len(anagram_group)):
                    anagram_pairs.append((anagram_group[i], anagram_group[j]))
    return len(anagram_pairs) >= 61