def palindromes_between_indices(s):
    letters = s[4:10]
    letters = letters.lower()
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    half_palindrome = []
    for letter, count in letter_counts.items():
        half_palindrome.extend([letter] * (count // 2))
    half_palindrome.sort()
    used = [False] * len(half_palindrome)
    result = set()

    def backtrack(index, path):
        if len(path) > 2 and path == path[::-1]:
            result.add(''.join(path))
        if index == len(half_palindrome):
            return
        for i in range(index, len(half_palindrome)):
            if not used[i]:
                used[i] = True
                path.append(half_palindrome[i])
                backtrack(i + 1, path)
                path.pop()
                used[i] = False
    backtrack(0, [])
    return result