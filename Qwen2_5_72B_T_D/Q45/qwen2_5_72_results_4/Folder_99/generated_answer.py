def palindromes_between_indices(s):
    substring = s[4:9].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    palindromes = set()

    def can_form_palindrome(freq):
        odd_count = sum((1 for v in freq.values() if v % 2 != 0))
        return odd_count <= 1

    def form_palindromes(freq, half_palindrome, length):
        if length >= 3:
            palindrome = half_palindrome + half_palindrome[::-1]
            palindromes.add(palindrome)
        for char in freq:
            if freq[char] > 1:
                freq[char] -= 2
                form_palindromes(freq, half_palindrome + char, length + 2)
                freq[char] += 2
    if can_form_palindrome(char_count):
        form_palindromes(char_count, '', 0)
    return palindromes