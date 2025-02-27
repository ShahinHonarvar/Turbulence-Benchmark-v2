def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(34, 56):
        for i in range(30, 96 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes