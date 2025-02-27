def palindromes_of_specific_lengths(s):
    substr = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if all((c.isalpha() for c in candidate)) and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes