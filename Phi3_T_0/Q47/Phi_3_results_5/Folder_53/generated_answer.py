def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes