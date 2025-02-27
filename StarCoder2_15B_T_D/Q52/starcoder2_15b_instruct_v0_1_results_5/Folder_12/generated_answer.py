def palindrome_of_length_n(s):
    if len(s) < 23:
        return set()
    palindromes = set()
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes