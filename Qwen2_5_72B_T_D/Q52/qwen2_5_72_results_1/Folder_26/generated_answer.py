def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 366
    s = ''.join((c for c in s if c.isalpha()))
    found_palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            found_palindromes.add(substring)
    return found_palindromes