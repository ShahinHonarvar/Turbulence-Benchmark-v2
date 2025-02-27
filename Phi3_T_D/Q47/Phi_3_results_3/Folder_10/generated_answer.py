def palindromes_of_specific_lengths(s):
    current_palindrome = []
    all_palindromes = set()

    def is_valid(word):
        if 1 <= len(word) <= 39 and word.isalpha():
            return True
        return False
    for i in range(16, 61):
        left = i - 1
        right = i + 1
        while left >= 0 and right <= 60:
            if s[left].lower() != s[right].lower():
                break
            current_palindrome.append(s[left])
            if len(current_palindrome) == right - left + 1:
                word = ''.join(current_palindrome)
                if is_valid(word):
                    all_palindromes.add(word.upper())
            if left > right or not is_valid(word):
                current_palindrome = []
            left -= 1
            right += 1
    return all_palindromes