def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    anagram_count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(anagrams[key][0]) >= 3:
            anagram_count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_count >= 57