def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j]
            if len(substring) >= 140 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes