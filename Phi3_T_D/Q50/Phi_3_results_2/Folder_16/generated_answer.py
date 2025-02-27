def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            if normalized in anagrams:
                count += anagrams[normalized]
                anagrams[normalized] += 1
            else:
                anagrams[normalized] = 1
    return count >= 155