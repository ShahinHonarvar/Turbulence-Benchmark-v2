def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for i in range(len(s) - 366):
        if is_palindrome(s[i:i + 366]):
            palindromes.add(s[i:i + 366])
    return palindromes