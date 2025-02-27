def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 18):
        for j in range(i + 19, length + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes