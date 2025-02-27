def palindromes_of_specific_lengths(s):
    relevant_substring = s[23:78]
    palindromes = set()

    def is_english_letter(char):
        return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

    def find_palindromes(center, length, bounds):
        left, right = (center - length // 2, center + length // 2)
        if left < bounds[0] or right > bounds[1]:
            return
        if all((is_english_letter(c) for c in relevant_substring[left:right + 1])):
            palindromes.add(relevant_substring[left:right + 1].lower())
        find_palindromes(center + 1, length, bounds)
    for length in range(13, 41, 2):
        find_palindromes(23, length, (23, 78))
    for length in range(14, 41, 2):
        find_palindromes(23, length, (23, 78))
    return palindromes