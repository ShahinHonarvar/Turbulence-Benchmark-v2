def palindromes_of_specific_lengths(s):
    s = s[41:90].lower()
    palindromes = set()
    for i in range(len(s) - 22):
        for j in range(i + 23, min(i + 39, len(s)) + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if len(substring) >= 23 and len(substring) <= 38 and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes