def palindromes_of_specific_lengths(s):
    s = s[200:301]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes