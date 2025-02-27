def is_palindrome(s):
    return s == s[::-1]

def expanded_palindrome_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(input_string):
    res = set()
    for i in range(len(input_string)):
        temp = expanded_palindrome_center(input_string, i, i)
        if len(temp) >= 149 and is_palindrome(temp):
            res.add(temp)
        temp = expanded_palindrome_center(input_string, i, i + 1)
        if len(temp) >= 149 and is_palindrome(temp):
            res.add(temp)
    return res