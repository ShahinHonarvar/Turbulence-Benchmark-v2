def palindromes_of_specific_lengths(s):
    substr = s[14:91]
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(substr) - length + 1):
            substr_part = substr[i:i + length]
            if all((c.isalpha() for c in substr_part)) and substr_part.lower() == substr_part[::-1].lower():
                palindromes.add(substr_part)
    return palindromes