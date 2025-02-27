def palindrome_of_length_n(s):
    s = s.lower()
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    result = set()

    def extend_palindrome(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() in valid_letters) and (s[right].lower() in valid_letters):
            if right - left - 1 == 75 and s[left:right + 1] == s[left:right + 1][::-1]:
                result.add(s[left:right + 1].upper())
            left -= 1
            right += 1
    for i in range(len(s)):
        extend_palindrome(i, i)
        extend_palindrome(i, i + 1)
    return result