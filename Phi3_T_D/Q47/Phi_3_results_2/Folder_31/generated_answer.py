def palindromes_of_specific_lengths(input_string):
    substr = input_string[11:84]
    palindromes = set()
    for length in range(37, 61):
        for start in range(len(substr) - length + 1):
            substring = substr[start:start + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes