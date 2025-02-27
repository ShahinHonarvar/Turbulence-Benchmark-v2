def palindrome_of_length_n(s):
    unique_palindromes = set()
    length = 392
    s = s.lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            unique_palindromes.add(substring)
    return unique_palindromes