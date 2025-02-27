def palindrome_of_length_at_least_n(text):

    def expand_around_center(left, right, s, res):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left].lower() == s[right].lower() and right - left + 1 >= 49:
                res.add(s[left:right + 1])
                left -= 1
                right += 1
            else:
                break
    result = set()
    for i in range(len(text)):
        expand_around_center(i, i, text, result)
        expand_around_center(i, i + 1, text, result)
    return result