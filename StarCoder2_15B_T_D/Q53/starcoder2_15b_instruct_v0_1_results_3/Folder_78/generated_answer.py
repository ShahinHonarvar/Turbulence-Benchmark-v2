def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 96
    string = string.lower()
    for i in range(len(string) - n + 1):
        for j in range(i + n - 1, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes