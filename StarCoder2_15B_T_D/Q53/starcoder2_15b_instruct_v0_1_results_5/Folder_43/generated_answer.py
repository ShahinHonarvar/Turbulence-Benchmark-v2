def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string_lowercase = string.lower()
    for i in range(len(string_lowercase) - 49):
        for j in range(i + 49, len(string_lowercase)):
            substring = string_lowercase[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes