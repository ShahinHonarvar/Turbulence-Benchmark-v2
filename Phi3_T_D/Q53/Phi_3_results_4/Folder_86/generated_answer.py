def longest_palindrome(s, k):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            left -= 1
            right += 1
        return s[left + 1:right] if right - left - 1 >= k else ''
    palindromes = set()
    for i in range(len(s)):
        p1 = expand_around_center(i, i)
        if len(p1) >= k:
            palindromes.add(p1)
        p2 = expand_around_center(i, i + 1)
        if len(p2) >= k:
            palindromes.add(p2)
    return palindromes

def palindrome_of_length_at_least_n(input_string):
    lower_case_string = input_string.lower()
    return set(filter(lambda x: x.isalpha() and len(x) >= 133, map(longest_palindrome, [lower_case_string] * len(lower_case_string), [133] * len(lower_case_string))))