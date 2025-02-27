def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(3, 6):
            if i + length <= 6:
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes