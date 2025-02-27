def palindrome_of_length_n(s):
    set_palindrome = set()
    s = s.lower()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if substring == substring[::-1]:
            set_palindrome.add(substring)
    return set_palindrome