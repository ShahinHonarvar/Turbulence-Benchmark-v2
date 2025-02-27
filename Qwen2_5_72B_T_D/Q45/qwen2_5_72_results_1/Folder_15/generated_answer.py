def palindromes_between_indices(s):
    substr = s[1:3].lower()
    char_freq = {}
    for char in substr:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    def can_form_palindrome(freq):
        odd_counts = sum((1 for count in freq.values() if count % 2 != 0))
        return odd_counts <= 1

    def generate_palindromes(freq, length):
        if length < 3:
            return set()
        half_length = length // 2
        half_palindrome = []
        for char in freq:
            for _ in range(freq[char] // 2):
                half_palindrome.append(char)
                freq[char] -= 2
        half_palindrome.sort()
        palindromes = set()

        def backtrack(left, right):
            if len(left) == half_length:
                middle = [char for char in freq if freq[char] > 0]
                palindrome = left + middle + left[::-1]
                palindromes.add(''.join(palindrome))
                return
            for i in range(right, len(half_palindrome)):
                if i > right and half_palindrome[i] == half_palindrome[i - 1]:
                    continue
                backtrack(left + [half_palindrome[i]], i + 1)
        backtrack([], 0)
        for char in freq:
            freq[char] += 2
        return palindromes
    palindromes = set()
    for length in range(3, sum(char_freq.values()) + 1):
        if can_form_palindrome(dict(char_freq)):
            palindromes.update(generate_palindromes(dict(char_freq), length))
    return palindromes