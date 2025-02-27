def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        l -= 1
        r += 1
    return s[l + 1:r]

def palindrome_of_length_at_least_n(input_string):
    n = 17
    result = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        odd_length = expand_around_center(input_string, i, i)
        if len(odd_length) >= n:
            result.add(odd_length.upper())
        even_length = expand_around_center(input_string, i, i + 1)
        if len(even_length) >= n:
            result.add(even_length.upper())
    return result