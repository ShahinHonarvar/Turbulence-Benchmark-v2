def palindromes_of_specific_lengths(s):

    def is_valid_char(c):
        return 'a' <= c <= 'z'

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1] and all((is_valid_char(c) for c in sub_s))
    s = s.lower()
    start, end = (18, min(88, len(s)))
    result_set = set()
    for length in range(12, 15):
        for i in range(start, end - length + 1):
            if is_palindrome(s[i:i + length]):
                result_set.add(s[i:i + length])
    return result_set