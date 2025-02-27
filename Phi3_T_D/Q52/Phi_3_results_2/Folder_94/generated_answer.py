def palindrome_of_length_n(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    result = set()
    s = s.lower()
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            result.add(substring)
    return result