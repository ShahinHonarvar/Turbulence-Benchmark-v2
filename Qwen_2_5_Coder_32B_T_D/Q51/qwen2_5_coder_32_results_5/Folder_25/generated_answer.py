def if_contains_anagrams(s):
    s = [x.lower() for x in s if len(x) >= 3]
    count = 0
    seen = {}
    for word in s:
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            seen[sorted_word] += 1
            count += seen[sorted_word] - 1
        else:
            seen[sorted_word] = 1
    return count <= 67