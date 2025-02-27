def palindromes_of_specific_lengths(s):
    s = s[26:88]
    palindromes = set()
    for length in range(52, 57):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes