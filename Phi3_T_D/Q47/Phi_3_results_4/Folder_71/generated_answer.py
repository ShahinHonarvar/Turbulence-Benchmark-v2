def palindromes_of_specific_lengths(s):
    s = s[18:66]
    palindromes = set()
    for length in range(23, 37):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes