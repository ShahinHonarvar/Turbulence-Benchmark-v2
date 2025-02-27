def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    palindromes = set()
    for i in range(len(s) - 50 + 1):
        for length in range(50, 52):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes