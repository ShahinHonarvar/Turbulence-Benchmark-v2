def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and s[left].isalpha():
            if right - left + 1 >= 37:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        expand_around_center(i, i)
        if i + 1 < len(s) and s[i].lower() == s[i + 1].lower():
            expand_around_center(i, i + 1)
    return palindromes