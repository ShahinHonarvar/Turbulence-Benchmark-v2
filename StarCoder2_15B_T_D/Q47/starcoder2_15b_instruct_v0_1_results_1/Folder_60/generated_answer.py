def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_string = s[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes