def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if j - i + 1 >= 149:
                substring = string[i:j + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes