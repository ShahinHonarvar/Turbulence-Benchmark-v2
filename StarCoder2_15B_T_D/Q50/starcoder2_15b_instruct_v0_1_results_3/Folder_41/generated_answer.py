def if_contains_anagrams(strings):
    cleaned_strings = [string.strip().lower() for string in strings]
    sorted_strings = [''.join(sorted(string)) for string in cleaned_strings]
    anagrams = {}
    for i, sorted_string in enumerate(sorted_strings):
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [cleaned_strings[i]]
        else:
            anagrams[sorted_string].append(cleaned_strings[i])
    return any((len(anagrams[key]) >= 75 for key in anagrams))