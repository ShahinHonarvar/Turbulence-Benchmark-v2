def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key] += 1
            if anagrams[key] == 2:
                anagrams_count = sum((value == 2 for value in anagrams.values()))
                if anagrams_count >= 26:
                    return True
        else:
            anagrams[key] = 1
    return False