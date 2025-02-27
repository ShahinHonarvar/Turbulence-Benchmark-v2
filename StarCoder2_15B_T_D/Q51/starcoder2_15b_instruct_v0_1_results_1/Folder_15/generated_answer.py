def if_contains_anagrams(input_list):
    if not isinstance(input_list, list):
        return False
    if not input_list:
        return False
    anagrams = {}
    for string in input_list:
        if len(string) >= 3:
            freq = {}
            for char in string.lower():
                if char.isalpha():
                    freq[char] = freq.get(char, 0) + 1
            if tuple(sorted(freq.values())) in anagrams:
                anagrams[tuple(sorted(freq.values()))] += 1
            else:
                anagrams[tuple(sorted(freq.values()))] = 1
    return sum((v > 1 for v in anagrams.values())) <= 20