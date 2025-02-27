def extend_palindrome(s, i, direction):
    length = len(s)
    while 0 <= i < length and s[i].isalpha():
        i += direction
    return i

def palindrome_expansion(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
        count += 1
    return count

def palindrome_of_length_at_least_n(s):
    length = len(s)
    palindromes = set()
    for i in range(len(s)):
        if i - 119 >= 0:
            left = i - 119
            right = i
        else:
            continue
        count = palindrome_expansion(s, left, right) + 1
        if count >= 119:
            palindrome = s[left + 1:right + 1].lower()
            palindromes.add(palindrome)
    for i in range(length - 1, 118 - 1, -1):
        left = i - 1
        right = i
        count = palindrome_expansion(s, left, right) + 1
        if count >= 119:
            palindrome = s[left:right + 1].lower()
            palindromes.add(palindrome)
    return palindromes