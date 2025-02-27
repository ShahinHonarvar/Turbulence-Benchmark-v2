def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def extend_palindrome(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if is_palindrome(s[left:right + 1]):
                results.add(s[left:right + 1])
            left -= 1
            right += 1
    results = set()
    for i in range(len(s)):
        extend_palindrome(i - 1, i + 1)
        extend_palindrome(i, i + 1)
    return {p for p in results if len(p) >= 20}