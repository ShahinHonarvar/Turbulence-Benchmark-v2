def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def extend_palindrome(left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            lp = (left, right)
            palindromes.add(s[left:right + 1].capitalize())
            left -= 1
            right += 1
    for i in range(n):
        extend_palindrome(i, i)
        extend_palindrome(i, i + 1)
    valid_palindromes = {p for p in palindromes if len(p) >= 13 and p.isalpha()}
    return valid_palindromes