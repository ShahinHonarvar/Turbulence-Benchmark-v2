def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 4):
        for j in range(i + 5, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring.capitalize())
    return result