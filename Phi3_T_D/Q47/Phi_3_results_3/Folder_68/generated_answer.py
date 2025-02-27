def is_palindrome(s, left, right):
    while left < right:
        if not 'a' <= s[left].lower() <= 'z':
            left += 1
        elif not 'a' <= s[right].lower() <= 'z':
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

def palindromes_of_specific_lengths(s):
    sub = s[:51]
    palindromes = set()
    for length in range(50, 101):
        for left in range(len(sub) - length + 1):
            if is_palindrome(sub, left, left + length - 1):
                palindromes.add(sub[left:left + length])
    return palindromes