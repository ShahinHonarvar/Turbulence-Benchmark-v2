def expand(s, left, right):
    lst = list(s)
    while left >= 0 and right < len(lst) and (lst[left].lower() == lst[right].lower()):
        left -= 1
        right += 1
    return (left + 1, right)

def palindrome_of_length_at_least_n(s):
    set_palindromes = set()
    for i in range(len(s)):
        if i - 73 + 1 >= 0:
            left, right = expand(s, i - 73 + 1, i)
            palindrome = ''.join(s[left:right]).lower()
            if len(palindrome) >= 74:
                set_palindromes.add(palindrome)
    for i in range(len(s) - 1):
        left, right = expand(s, i, i + 1)
        palindrome = ''.join(s[left:right]).lower()
        if len(palindrome) >= 74 and right - left == 74:
            set_palindromes.add(palindrome)
    return set_palindromes