def palindromes_of_specific_lengths(s):
    s = s[11:98]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 28):
        for length in range(29, 63):
            if s[i:i + length] == s[i + length - 1:i - 1:-1]:
                palindromes.add(s[i:i + length])
    return palindromes