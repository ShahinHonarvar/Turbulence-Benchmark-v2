def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    if len(letters) < 4:
        return set()
    letters.sort()
    result = set()
    for i in range(len(letters) - 3):
        for perm in set(itertools.permutations(letters[i:i + 4])):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result