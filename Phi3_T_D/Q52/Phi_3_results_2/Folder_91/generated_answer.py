def palindrome_of_length_n(s):
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 6):
        if s[i:i + 7] == s[i:i + 7][::-1]:
            set_palindromes.add(s[i:i + 7])
    return set_palindromes