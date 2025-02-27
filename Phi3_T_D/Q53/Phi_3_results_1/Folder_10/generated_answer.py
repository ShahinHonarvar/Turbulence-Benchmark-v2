def palindrome_of_length_at_least_n(s):

    def expand(center, left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left].lower() != s[right].lower():
                break
            if right - left + 1 >= m:
                palindromes.add(s[left:right + 1].upper())
            left -= 1
            right += 1
    palindromes = set()
    n = 92
    m = n - 1
    for i in range(len(s)):
        expand(i, i, i)
        expand(i, i, i + 1)
    return palindromes