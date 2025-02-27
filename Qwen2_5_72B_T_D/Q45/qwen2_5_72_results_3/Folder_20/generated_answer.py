def palindromes_between_indices(s):
    substring = s[2:9]
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1
    half_palindrome = []
    for letter, count in letter_counts.items():
        half_palindrome.extend([letter] * (count // 2))

    def generate_palindromes(half, used):
        if len(half) == len(half_palindrome):
            full_palindrome = ''.join(half + half[::-1])
            if len(full_palindrome) >= 4:
                return {full_palindrome}
            return set()
        palindromes = set()
        for i in range(len(half_palindrome)):
            if i not in used:
                new_used = used | {i}
                new_half = half + [half_palindrome[i]]
                palindromes.update(generate_palindromes(new_half, new_used))
        return palindromes
    return generate_palindromes([], set())