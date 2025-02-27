def palindromes_of_specific_lengths(s):
    index_range = range(12, 93)
    length_range = range(17, 67)
    palindromes = set()
    for start_index in index_range:
        for length in length_range:
            end_index = start_index + length
            if end_index > 92:
                end_index = 92
            substring = s[start_index:end_index].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes