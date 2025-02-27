def palindromes_between_indices(s):
    letters = s[3:8].lower()
    unique_letters = set(letters)
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def backtrack(path, start):
        if len(path) >= 4 and is_palindrome(path):
            palindromes.add(path)
        if len(path) > 4:
            return
        for i in range(start, len(unique_letters)):
            backtrack(path + unique_letters[i], i)
    backtrack('', 0)
    return palindromes