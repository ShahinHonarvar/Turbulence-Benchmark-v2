def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    string_len = len(s)
    for center in range(2 * string_len - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < string_len and (s[left] == s[right]):
            if right - left + 1 >= 115:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    return palindromes