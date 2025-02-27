def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            canonical = ''.join(sorted(string.lower()))
            if canonical in anagrams:
                anagrams[canonical].append(string)
            else:
                anagrams[canonical] = [string]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 276