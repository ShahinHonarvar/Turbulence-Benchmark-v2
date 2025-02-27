def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    n = 100
    while n <= len(string):
        for i in range(len(string) - n + 1):
            substr = string[i:i + n]
            if all((c.isalpha() for c in substr)) and substr == substr[::-1]:
                palindromes.add(substr)
        n += 1
    return palindromes