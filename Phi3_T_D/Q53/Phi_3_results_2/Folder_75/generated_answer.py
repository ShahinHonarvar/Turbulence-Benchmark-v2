def expand_around_center(s, left, right):
    result = set()
    while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
        if s[left].lower() == s[right].lower():
            if right - left + 1 >= 40:
                result.add(s[left:right + 1].lower())
            left -= 1
            right += 1
        else:
            break
    return result

def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        result |= expand_around_center(s, i, i)
        result |= expand_around_center(s, i, i + 1)
    return result