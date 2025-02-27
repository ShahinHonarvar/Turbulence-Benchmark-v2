def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    n = 137
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                result.add(s[i:j + 1])
    return result