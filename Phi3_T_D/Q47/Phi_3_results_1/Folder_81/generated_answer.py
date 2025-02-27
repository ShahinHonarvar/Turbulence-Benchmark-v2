def palindromes_of_specific_lengths(text):
    palindromes = set()
    substr = text[12:122].lower()
    for length in range(12, 221):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes