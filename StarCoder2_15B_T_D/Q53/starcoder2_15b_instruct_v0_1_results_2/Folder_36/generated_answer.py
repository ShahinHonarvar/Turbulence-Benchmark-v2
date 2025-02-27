def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 144
    for i in range(len(string) - n + 1):
        for j in range(i + n - 1, len(string)):
            substring = string[i:j + 1]
            if substring.lower() == substring[::-1].lower() and len(substring) >= n:
                palindromes.add(substring)
    return palindromes