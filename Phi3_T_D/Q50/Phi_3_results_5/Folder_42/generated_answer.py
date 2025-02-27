def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    number_of_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return number_of_pairs >= 233