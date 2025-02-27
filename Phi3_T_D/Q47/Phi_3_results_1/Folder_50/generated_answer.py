def is_palindrome(s):
    return s.lower() == s[::-1].lower() and s.isalpha()

def extend_palindromes(s, left, right, collected):
    current_length = right - left + 1
    while left >= 0 and right < len(s) and is_palindrome(s[left:right + 1]):
        if 10 <= current_length <= 35:
            collected.add(s[left:right + 1].lower())
        left -= 1
        right += 1

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(36, min(93, len(s))):
        extend_palindromes(s, i, i, palindromes)
        extend_palindromes(s, i, i + 1, palindromes)
    return palindromes