def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = max(len(s), 3)
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() in alphabet) and (s[right].lower() in alphabet):
            if is_palindrome(s[left:right + 1]):
                palindromes.add(s[left:right + 1])
            if len(s[left:right + 1]) >= 32:
                return
            left -= 1
            right += 1
    for i in range(len(s)):
        expand_around_center(i, i)
        if i + 1 < len(s) and s[i].lower() == s[i + 1].lower():
            expand_around_center(i, i + 1)
    return palindromes