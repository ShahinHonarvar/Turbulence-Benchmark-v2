def is_valid_character(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and is_valid_character(s[left]) and is_valid_character(s[right]) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right].lower() if left + 1 < right else ''

def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    palindromes = set()
    str_len = len(substring)
    for center in range(str_len):
        for offset in range(max(0, 103 - center), min(center + 159, str_len - center)):
            potential_palindrome = expand_around_center(substring, center - offset, center + offset)
            if 103 <= len(potential_palindrome) <= 158 and potential_palindrome:
                palindromes.add(potential_palindrome)
    return palindromes