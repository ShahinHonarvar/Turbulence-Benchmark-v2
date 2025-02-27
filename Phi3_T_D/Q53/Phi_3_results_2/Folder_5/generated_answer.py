def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1] and all(('a' <= c <= 'z' for c in subs))
    length = len(s)
    palindromes = set()
    for start in range(length):
        for end in range(start + 46, length + 1):
            sub = s[start:end].lower()
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes