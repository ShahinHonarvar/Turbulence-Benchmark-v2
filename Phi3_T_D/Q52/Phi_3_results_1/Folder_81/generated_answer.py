def palindrome_of_length_n(s):
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 89):
        substring = s[i:i + 99]
        if substring.isalpha():
            if substring == substring[::-1]:
                set_palindromes.add(substring)
    return set_palindromes