def palindromes_between_indices(s):
    required_chars = sorted(set(s[1:7].lower()))

    def is_palindrome(chars):
        return chars == chars[::-1]

    def find_all_permutations(arr, l, r):
        if l == r:
            permutation = ''.join(arr)
            if is_palindrome(permutation) and len(permutation) >= 3:
                return {permutation}
            return set()
        permutations = set()
        for i in range(l, r + 1):
            arr[l], arr[i] = (arr[i], arr[l])
            permutations |= find_all_permutations(arr, l + 1, r)
            arr[l], arr[i] = (arr[i], arr[l])
        return permutations
    set_of_palindromes = find_all_permutations(list(required_chars), 0, len(required_chars) - 1)
    return set_of_palindromes