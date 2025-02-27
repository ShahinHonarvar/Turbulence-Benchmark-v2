def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    anagram_pairs = sum((len(v) - 1 for v in anagrams.values()))
    return anagram_pairs <= 14