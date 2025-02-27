def expand_around_center(s, left, right):
    palindromes = set()
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= 95:
            palindromes.add(s[left:right + 1])
        left -= 1
        right += 1
    return palindromes

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    all_palindromes = set()
    for i in range(len(s)):
        odd_palindromes = expand_around_center(s, i, i)
        even_palindromes = expand_around_center(s, i, i + 1)
        all_palindromes.update(odd_palindromes)
        all_palindromes.update(even_palindromes)
    return all_palindromes