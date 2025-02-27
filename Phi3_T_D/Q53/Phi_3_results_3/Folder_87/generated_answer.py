def expand_around_center(s, left, right):
    result = set()
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and (right - left + 1 >= 18):
        s1 = s[left:right + 1]
        if s1.isalpha():
            result.add(s1)
        left -= 1
        right += 1
    return result

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        palindromes.update(expand_around_center(s, i, i))
        if i + 1 < len(s) and s[i].lower() == s[i + 1].lower():
            palindromes.update(expand_around_center(s, i, i + 1))
    return palindromes