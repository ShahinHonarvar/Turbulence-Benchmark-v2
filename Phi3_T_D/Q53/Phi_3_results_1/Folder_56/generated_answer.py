def expand(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return right - left - 1

def find_all_palindromes(s):
    palindrome_set = set()
    for center in range(2 * len(s) - 1):
        left = center // 2
        right = left + center % 2
        len_mirror = expand(s, left, right)
        if len_mirror >= 84:
            palindrome_set.add(s[left:left + len_mirror].lower())
    return palindrome_set

def palindrome_of_length_at_least_n(s):
    return find_all_palindromes(s)