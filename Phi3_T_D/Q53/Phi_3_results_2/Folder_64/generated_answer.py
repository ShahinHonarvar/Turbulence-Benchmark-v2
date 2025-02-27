import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = 9
    result_set = set()
    while length <= len(s):
        for start in range(len(s) - length + 1):
            palindrome_candidate = s[start:start + length]
            if palindrome_candidate == palindrome_candidate[::-1] and re.match('^[a-z]+$', palindrome_candidate):
                result_set.add(palindrome_candidate)
        length += 1
    return result_set