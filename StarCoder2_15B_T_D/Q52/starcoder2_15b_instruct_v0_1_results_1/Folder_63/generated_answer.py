def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 17):
        for j in range(i + 18, length + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes