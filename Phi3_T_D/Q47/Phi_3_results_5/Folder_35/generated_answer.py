def palindromes_of_specific_lengths(s):
    length_range = range(14, 40)
    substring = s[34:91].lower()
    palindromes = set()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes