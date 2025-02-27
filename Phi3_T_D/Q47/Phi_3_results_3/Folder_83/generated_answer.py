def palindromes_of_specific_lengths(input_string):
    substring = input_string[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((c.isalpha() and candidate.lower() == candidate[::-1].lower() for c in candidate)):
                palindromes.add(candidate.lower())
    return palindromes