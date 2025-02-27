def palindrome_of_length_at_least_n(s):
    n = len(s)
    if n < 122:
        return set()
    palindromes = set()
    s = s.lower()

    def extendPalindrome(left, right, s):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(1, n):
        extendPalindrome(i - 1, i, s)
        extendPalindrome(i, i + 1, s)
    filtered_palindromes = {p for p in palindromes if len(p) >= 122 and p.isalpha()}
    return filtered_palindromes