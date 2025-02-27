def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 42):
        for j in range(i + 42, len(string)):
            substring = string[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes