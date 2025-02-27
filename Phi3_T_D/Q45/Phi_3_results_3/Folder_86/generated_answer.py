def palindromes_between_indices(s):
    target_str = s[6:10]
    characters = ''.join(set(target_str.lower()))
    results = set()

    def backtrack(path):
        if len(path) >= 4 and path == path[::-1]:
            results.add(path)
            return
        for char in characters:
            if len(path) + 1 <= 4:
                backtrack(path + char)
    backtrack('')
    return results