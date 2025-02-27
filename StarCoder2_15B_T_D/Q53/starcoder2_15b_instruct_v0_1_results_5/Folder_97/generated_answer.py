def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 138, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result