def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def get_substring(s, start, end):
        return s[start:end + 1]

    def get_permutations(s):
        if len(s) == 0:
            return ['']
        perms = []
        for i in range(len(s)):
            ch = s[i]
            rem = s[:i] + s[i + 1:]
            for perm in get_permutations(rem):
                perms.append(ch + perm)
        return perms
    substring = get_substring(s, 4, 9)
    permutations = get_permutations(substring)
    palindromes = set()
    for perm in permutations:
        if is_palindrome(perm) and len(perm) >= 7:
            palindromes.add(perm.lower())
    return palindromes