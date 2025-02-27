def palindromes_between_indices(s):
    letters = sorted(s[2:4].lower())
    unique_letters = set(letters)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_permutations(prefix, remaining):
        if len(prefix) >= 3 and is_palindrome(prefix):
            palindromes.add(prefix)
        if not remaining:
            return
        for i in range(len(remaining)):
            generate_permutations(prefix + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_permutations('', ''.join(unique_letters))
    return palindromes