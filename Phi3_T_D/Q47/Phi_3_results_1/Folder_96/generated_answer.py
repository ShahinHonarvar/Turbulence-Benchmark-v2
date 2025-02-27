def palindromes_of_specific_lengths(s):
    start, end = (100, 300)
    s = s.lower()
    char_set = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(50, 101):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if all((c in char_set for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes