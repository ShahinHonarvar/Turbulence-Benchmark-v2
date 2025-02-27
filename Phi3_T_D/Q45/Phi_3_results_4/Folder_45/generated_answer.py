def generate_palindromes(chars, length):
    if length <= 0:
        return []
    if length == 1:
        return [char.lower() for char in chars]
    if length == 2:
        return [char + char.lower() for char in chars if char.lower() == char.lower()[::-1]]
    palindromes = []
    for i in range(len(chars) - length + 1):
        prefix = chars[i].lower()
        suffix = chars[i + length - 1].lower()
        inner_palindromes = generate_palindromes(chars[i + 1:i + length - 1], length - 2)
        for palindrome in inner_palindromes:
            palindromes.append(prefix + palindrome + suffix)
            for j in range(1, length - 1):
                palindromes.append(palindrome[:j] + chars[i + j].lower() + palindrome[j:])
    return palindromes

def palindromes_between_indices(s):
    english_chars = [char.lower() for char in s[5:10]]
    palindromes = set((p for length in range(4, len(english_chars) + 1) for p in generate_palindromes(english_chars, length)))
    return palindromes