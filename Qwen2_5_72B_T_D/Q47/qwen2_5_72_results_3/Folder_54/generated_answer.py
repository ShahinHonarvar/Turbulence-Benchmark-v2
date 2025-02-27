def palindromes_of_specific_lengths(s):
    s = s[27:78]
    palindromes = set()
    for i in range(len(s) - 17):
        for length in [18, 19]:
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes