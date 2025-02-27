def palindromes_between_indices(s):
    subset = s[4:10]
    letters = sorted(list(set(subset.lower())))

    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(path, start):
        if len(path) >= 7:
            if is_palindrome(''.join(path)):
                result.add(''.join(path))
            return
        for i in range(start, len(letters)):
            backtrack(path + [letters[i]], i)
    result = set()
    backtrack([], 0)
    return result