def palindrome_of_length_n(input_str):
    results = set()
    str_len = len(input_str)
    min_ch = 'a'
    max_ch = 'z'

    def is_palindrome(s):
        return s == s[::-1]

    def expand_around_center(left, right):
        while left >= 0 and right < len(input_str) and (input_str[left].lower() >= min_ch) and (input_str[left].lower() <= max_ch) and (input_str[right].lower() >= min_ch) and (input_str[right].lower() <= max_ch):
            if is_palindrome(input_str[left:right + 1]):
                results.add(input_str[left:right + 1])
            if right - left < 222:
                break
            left -= 1
            right += 1
    for i in range(str_len):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return results