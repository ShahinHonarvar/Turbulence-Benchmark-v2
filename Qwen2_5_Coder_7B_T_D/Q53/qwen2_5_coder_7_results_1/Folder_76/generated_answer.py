def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 137
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if substr == ''.join(reversed(substr)) and substr.isalpha():
                result.add(substr)
    return result