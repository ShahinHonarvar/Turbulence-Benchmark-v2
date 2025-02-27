def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 147:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(text):
    unique_palindromes = set()
    for i in range(len(text)):
        for palindrome in expand_around_center(text, i, i):
            unique_palindromes.add(palindrome)
        for palindrome in expand_around_center(text, i, i + 1):
            unique_palindromes.add(palindrome)
    return unique_palindromes