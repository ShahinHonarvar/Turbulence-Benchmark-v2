def palindromes_of_specific_lengths(s):
    substring = s[10:101]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part.isalpha() and part.lower() == part[::-1].lower():
                palindromes.add(part)
    return palindromes