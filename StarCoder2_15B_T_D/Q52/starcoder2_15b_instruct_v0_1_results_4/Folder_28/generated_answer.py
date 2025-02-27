def palindrome_of_length_n(string):
    palindromes = set()
    n = 43
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes