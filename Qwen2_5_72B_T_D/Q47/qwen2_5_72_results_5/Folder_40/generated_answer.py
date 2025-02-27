def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    palindromes = set()
    for i in range(3, 6):
        for j in range(0, 6 - i):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes