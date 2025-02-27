def palindrome_of_length_at_least_n(s):

    def is_valid(c):
        return 'a' <= c <= 'z'

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and is_valid(s[left]) and is_valid(s[right]):
            if s[left].lower() == s[right].lower():
                right += 1
                left -= 1
            else:
                break
        return s[left + 1:right].lower()
    palindromes = set()
    for center in range(len(s)):
        palindromes.update(expand_around_center(center, center + 1))
        palindromes.update(expand_around_center(center, center))
    return {p for p in palindromes if len(p) >= 51}