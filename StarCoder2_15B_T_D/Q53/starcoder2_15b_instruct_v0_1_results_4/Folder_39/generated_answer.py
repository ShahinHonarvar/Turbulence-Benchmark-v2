def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j]
            if len(substring) >= 69 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes