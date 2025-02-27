def is_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def expand_palindrome(s, left, right):
    while left >= 0 and right < len(s) and is_letter(s[left]) and is_letter(s[right]):
        if s[left] != s[right]:
            break
        left -= 1
        right += 1
    return s[left + 1:right]

def palindromes_of_specific_lengths(text):
    result_set = set()
    for length in range(17, 56):
        for i in range(23, len(text) - length + 2):
            palindrome = expand_palindrome(text, i, i + length - 1)
            if palindrome and palindrome == palindrome[::-1]:
                result_set.add(palindrome)
    return result_set