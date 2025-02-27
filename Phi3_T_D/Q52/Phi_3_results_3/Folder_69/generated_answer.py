def palindrome_of_length_n(s):
    set_palindromes = set()
    n = 472
    str_length = len(s)
    if str_length < n:
        return set_palindromes
    for i in range(str_length - n + 1):
        substring = s[i:i + n]
        if substring.lower() == substring[::-1].lower():
            set_palindromes.add(substring)
    return set_palindromes