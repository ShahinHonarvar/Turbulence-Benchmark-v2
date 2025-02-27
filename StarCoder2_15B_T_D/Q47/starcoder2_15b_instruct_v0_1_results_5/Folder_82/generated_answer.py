def palindromes_of_specific_lengths(string):
    palindromes = set()
    n = len(string)
    for length in range(30, 301):
        for i in range(3, 301):
            if i + length - 1 < n:
                substring = string[i:i + length]
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes