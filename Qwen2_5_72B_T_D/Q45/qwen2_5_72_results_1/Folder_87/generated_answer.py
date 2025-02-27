def palindromes_between_indices(s):
    substring = s[3:10].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    results = set()

    def generate_palindrome(half, length):
        if all((v % 2 == 0 for v in char_freq.values())):
            results.add(half + half[::-1])
        elif length % 2 == 1:
            for char in char_freq:
                if char_freq[char] % 2 == 1:
                    modified_freq = char_freq.copy()
                    modified_freq[char] -= 1
                    generate_palindrome(half + char, length - 1)
                    break

    def backtrack(half, length):
        if length == 0:
            generate_palindrome(half, 0)
            return
        for char in list(char_freq):
            if char_freq[char] > 1:
                char_freq[char] -= 2
                backtrack(half + char, length - 2)
                char_freq[char] += 2
    backtrack('', len(substring) - sum((1 for v in char_freq.values() if v % 2 == 1)))
    return {pal for pal in results if len(pal) >= 3}