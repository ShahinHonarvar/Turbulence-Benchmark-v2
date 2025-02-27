def palindromes_of_specific_lengths(s):
    s = s[17:87].lower()
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes