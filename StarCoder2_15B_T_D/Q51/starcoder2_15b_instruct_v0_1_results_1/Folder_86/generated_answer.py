def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    count_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return count_anagrams <= 48