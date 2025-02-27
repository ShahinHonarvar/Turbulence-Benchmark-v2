def palindromes_between_indices(s):
    substr = s[2:6].lower()
    seen = set()

    def backtrack(start, path):
        if len(path) >= 4 and path == path[::-1]:
            seen.add(''.join(path))
        for i in range(start, len(substr)):
            backtrack(i + 1, path + [substr[i]])
    backtrack(0, [])
    return seen