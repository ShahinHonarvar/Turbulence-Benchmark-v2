def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    if length < 69:
        return palindromes
    for i in range(length - 68):
        substring = string[i:i + 69]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes