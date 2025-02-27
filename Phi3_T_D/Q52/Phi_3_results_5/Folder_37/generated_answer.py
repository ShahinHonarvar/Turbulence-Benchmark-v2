def palindrome_of_length_n(s):
    s = s.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s) - 84 + 1):
        substring = s[i:i + 84]
        if all((letter in english_letters for letter in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes