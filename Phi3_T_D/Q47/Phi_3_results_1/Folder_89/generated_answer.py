def palindromes_of_specific_lengths(s):
    sub_string = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes