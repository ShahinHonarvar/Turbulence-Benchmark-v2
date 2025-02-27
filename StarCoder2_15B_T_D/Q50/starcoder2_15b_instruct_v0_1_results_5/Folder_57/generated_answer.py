def if_contains_anagrams(input_list):
    anagrams = {}
    for string in input_list:
        normalized_string = ''.join((c for c in string.lower() if c.isalnum()))
        if len(normalized_string) >= 3:
            sorted_string = ''.join(sorted(normalized_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    return len(anagrams) >= 50