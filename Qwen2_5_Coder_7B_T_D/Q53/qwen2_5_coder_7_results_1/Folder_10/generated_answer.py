def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    n = 92
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result