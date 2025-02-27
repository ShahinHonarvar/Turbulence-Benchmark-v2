def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_substrings(length):
        if length > len(s):
            return []
        return [s[i:i + length] for i in range(len(s) - length + 1)]
    palindromes = set()
    s = s.lower()
    length = 66
    while length <= len(s):
        for substr in get_substrings(length):
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                palindromes.add(substr)
        length += 1
    return palindromes