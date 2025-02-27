def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for length in [18, 19]:
            if i + length <= len(s):
                substring = ''.join(filter(str.isalpha, s[i:i + length]))
                if len(substring) == length and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes