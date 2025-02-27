def expand_around_center(s, left, right):
    length = len(s)
    while left >= 0 and right < length:
        if s[left].lower() != s[right].lower():
            break
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    length = len(s)
    palindromes = set()
    for i in range(length):
        odd_palindrome = list(expand_around_center(s, i, i))
        even_palindrome = list(expand_around_center(s, i, i + 1))
        for palindrome in odd_palindrome + even_palindrome:
            if len(palindrome) >= 29:
                palindromes.add(palindrome.lower())
    return palindromes