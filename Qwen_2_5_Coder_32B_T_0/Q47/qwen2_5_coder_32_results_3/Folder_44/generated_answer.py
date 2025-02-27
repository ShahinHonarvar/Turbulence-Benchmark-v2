def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    palindromes = set()
    for i in range(len(s) - 30):
        for j in range(i + 30, min(i + 51, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes