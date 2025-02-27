def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[15:90]
    palindromes = set()

    def is_english_letter(char: str) -> bool:
        return 'a' <= char.lower() <= 'z'

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    for length in range(40, 73):
        for start in range(15, 90 - length + 1):
            if all((is_english_letter(char) for char in substring[start:start + length].lower())):
                if is_palindrome(substring[start:start + length].lower()):
                    palindromes.add(substring[start:start + length].lower())
    return palindromes