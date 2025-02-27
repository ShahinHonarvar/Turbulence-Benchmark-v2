def palindromes_of_specific_lengths(s):
    start, end = (41, 89)
    palindromes = set()
    for length in range(23, 39):
        for i in range(start, end - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes