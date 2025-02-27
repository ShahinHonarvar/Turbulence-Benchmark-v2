def palindromes_of_specific_lengths(s):
    start, end = (32, 72)
    palindromes = set()
    for length in range(21, 33):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes