def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 62):
        substring = string[i:i + 63]
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes