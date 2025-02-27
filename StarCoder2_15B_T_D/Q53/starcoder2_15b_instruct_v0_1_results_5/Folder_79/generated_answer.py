def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 16):
        for j in range(i + 17, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes