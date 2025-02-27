def palindromes_of_specific_lengths(s):
    s = s[16:61].lower()
    palindromes = set()
    for start in range(len(s) - 15):
        for end in range(start + 15, min(start + 40, len(s))):
            substring = ''.join(filter(str.isalpha, s[start:end + 1]))
            if substring == substring[::-1] and 16 <= len(substring) <= 39:
                palindromes.add(substring)
    return palindromes