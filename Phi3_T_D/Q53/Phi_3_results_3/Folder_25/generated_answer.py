def palindrome_of_length_at_least_n(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def expand_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(len(s)):
        palindrome_odd = expand_center(i, i)
        palindrome_even = ''
        if i + 1 < len(s):
            palindrome_even = expand_center(i, i + 1)
        if len(palindrome_odd) >= 38 and all((c in alphabet for c in palindrome_odd)):
            palindromes.add(palindrome_odd)
        if len(palindrome_even) >= 38 and all((c in alphabet for c in palindrome_even)):
            palindromes.add(palindrome_even)
    return palindromes