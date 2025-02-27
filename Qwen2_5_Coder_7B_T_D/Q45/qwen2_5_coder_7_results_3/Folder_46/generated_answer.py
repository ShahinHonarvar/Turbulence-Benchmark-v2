def palindromes_between_indices(s: str) -> set:
    s = s[4:10].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = set()

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def backtrack(index: int, path: str) -> None:
        if index == len(s):
            if len(path) >= 6 and is_palindrome(path):
                result.add(path)
            return
        for letter in letters:
            backtrack(index + 1, path + letter)
    backtrack(0, '')
    return result