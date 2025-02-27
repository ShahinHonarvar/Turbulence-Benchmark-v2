def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 28, len(s) + 1):
            subs = s[i:j]
            if is_palindrome(subs):
                palindromes.add(subs)
    return palindromes