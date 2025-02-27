def palindromes_between_indices(s):
    low = 5
    if s == '' or len(s) < 5:
        return set()
    counter = {}
    for c in s[:6]:
        counter[c.lower()] = counter.get(c.lower(), 0) + 1

    def can_form_palindrome(counts):
        odd_count = 0
        for c in counts:
            if counts[c] % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True
    palindromes = set()
    for key in counter:
        if counter[key] >= 2:
            mid = key * ((counter[key] - 1) // 2)
            palindromes.add(mid + mid[::-1])
            mid += key
            palindromes.add(mid + mid[::-1])
    if can_form_palindrome(counter):
        palindromes.add(''.join([k * (v // 2 - 1) + 'a' + k * (v // 2 - 1) for k, v in counter.items() if v >= 2]) + ''.join((k * (v // 2 - 1) for k, v in counter.items() if v >= 2 and k != 'a')))
    return palindromes