def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
    count = sum((len(value) - 1 for value in anagrams.values() if len(value) > 1))
    return count >= 209