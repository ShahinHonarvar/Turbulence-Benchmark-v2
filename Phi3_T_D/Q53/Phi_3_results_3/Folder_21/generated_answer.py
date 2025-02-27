def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(input_string):
    result_set = set()
    for i in range(len(input_string)):
        for palindrome in expand_around_center(input_string, i, i):
            if len(palindrome) >= 112:
                result_set.add(palindrome.lower())
        for palindrome in expand_around_center(input_string, i, i + 1):
            if len(palindrome) >= 112:
                result_set.add(palindrome.lower())
    return result_set