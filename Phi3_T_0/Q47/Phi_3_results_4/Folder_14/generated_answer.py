def palindromes_of_specific_lengths(s):
    s = s[10:75].lower()
    palindromes = set()
    for i in range(10, 75 - 5):
        for length in range(6, 9):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes