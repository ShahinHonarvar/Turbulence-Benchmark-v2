def palindrome_of_length_n(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = set()
    s = s.lower()
    for i in range(len(s)):
        left, right = (i, i + 255)
        substring = s[left:right]
        if len(substring) < 255:
            break
        if all((c in valid_chars for c in substring)):
            if substring == substring[::-1]:
                result.add(substring)
    return result