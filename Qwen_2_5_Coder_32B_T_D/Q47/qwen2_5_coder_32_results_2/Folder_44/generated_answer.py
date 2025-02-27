def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    palindromes = set()
    for start in range(len(s) - 30):
        for length in range(31, 52):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes