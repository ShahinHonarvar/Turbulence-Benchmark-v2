def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()

    def is_palindrome(subs):
        return subs == subs[::-1]
    for i in range(len(s) - 172):
        substr = s[i:i + 173]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes