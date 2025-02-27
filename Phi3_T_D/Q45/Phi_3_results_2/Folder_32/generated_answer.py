from itertools import permutations

def palindromes_between_indices(text):
    start, end = (1, 7)
    sub_str = text[start:end + 1].lower()
    letters = [char for char in sub_str if char.isalpha()]
    if len(letters) < 5:
        return set()
    all_permutations = set(permutations(letters, len(letters)))
    palindromes = set()
    for perm in all_permutations:
        word = ''.join(perm)
        if len(word) >= 5:
            front = word[:len(word) // 2]
            back = word[len(word) // 2:]
            back = back[::-1] if len(word) % 2 == 0 else back[-2::-1]
            palindrome = front + back
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes