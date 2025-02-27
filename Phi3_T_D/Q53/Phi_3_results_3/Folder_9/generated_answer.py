def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right].lower()

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        odd_len_palindrome = expand_around_center(s, i, i)
        if len(odd_len_palindrome) >= 95:
            palindromes.add(odd_len_palindrome)
        even_len_palindrome = expand_around_center(s, i, i + 1)
        if len(even_len_palindrome) >= 95:
            palindromes.add(even_len_palindrome)
    return palindromes