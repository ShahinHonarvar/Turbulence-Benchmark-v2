def is_palindrome(word):
    return word == word[::-1]

def expand_around_center(s, left, right):
    result = set()
    while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
        if is_palindrome(s[left:right + 1]):
            result.add(s[left:right + 1].lower())
        if right - left < 8:
            break
        left -= 1
        right += 1
    return result

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        palindromes.update(expand_around_center(s, i, i))
        palindromes.update(expand_around_center(s, i, i + 1))
    palindromes = {p for p in palindromes if len(p) >= 9}
    return palindromes