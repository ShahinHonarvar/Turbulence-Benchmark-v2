from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letter_frequencies = {}
    for char in substring:
        if char.isalpha():
            if char in letter_frequencies:
                letter_frequencies[char] += 1
            else:
                letter_frequencies[char] = 1
    candidates = set()
    for attempt in permutations(letter_frequencies.items()):
        half = ''
        for char, count in attempt:
            half += char * (count // 2)
        for i in range(len(half) + 1):
            left = half[:i]
            right = half[i:][::-1]
            middle = ''.join([c * (frequencies % 2) for c, frequencies in attempt])
            palindrome = left + middle + right
            if len(palindrome) >= 5:
                candidates.add(palindrome)
    return candidates