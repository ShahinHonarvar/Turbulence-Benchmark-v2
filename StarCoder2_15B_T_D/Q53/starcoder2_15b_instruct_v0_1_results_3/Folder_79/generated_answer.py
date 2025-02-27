def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 17:
                result.add(s[i:j])
    return result