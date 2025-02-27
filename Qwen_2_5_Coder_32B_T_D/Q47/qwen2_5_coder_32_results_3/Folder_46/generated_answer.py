def palindromes_of_specific_lengths(s):
    s = s[11:98].lower()
    palindromes = set()
    for start in range(len(s) - 28):
        for end in range(start + 29, min(start + 63, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes