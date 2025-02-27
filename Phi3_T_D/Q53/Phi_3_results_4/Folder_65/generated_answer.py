def expand_around_center(s, left, right):
    palindromes = set()
    l, r = (left, right)
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        palindromes.add(s[l:r + 1].lower())
        l -= 1
        r += 1
    return palindromes

def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    for i in range(len(s)):
        odd_palindromes = expand_around_center(s, i, i)
        for p in odd_palindromes:
            if len(p) >= 15:
                palindrome_set.add(p)
        even_palindromes = expand_around_center(s, i, i + 1)
        for p in even_palindromes:
            if len(p) >= 15:
                palindrome_set.add(p)
    return palindrome_set