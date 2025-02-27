def is_palindrome(word):
    return word == word[::-1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left].isalpha():
        if is_palindrome(s[left:right + 1]):
            yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s)):
        for p in expand_around_center(s, i, i):
            if len(p) >= 60:
                result_set.add(p)
        for p in expand_around_center(s, i, i + 1):
            if len(p) >= 60:
                result_set.add(p)
    return result_set