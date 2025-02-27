def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    palindromes = set()
    for start in range(len(s) - 56):
        for end in range(start + 56, min(start + 61, len(s))):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes