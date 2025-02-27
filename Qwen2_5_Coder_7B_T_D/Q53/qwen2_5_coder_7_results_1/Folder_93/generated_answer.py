def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 90, len(s) + 1):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result