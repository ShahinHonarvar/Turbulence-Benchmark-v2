def palindromes_between_indices(s):
    substring = s[2:10]
    unique_chars = set(substring.lower())
    if len(unique_chars) < 7:
        return set()
    all_chars = ''.join(unique_chars)
    all_perms = set()
    for i in range(len(all_chars)):
        for j in range(i + 7, len(all_chars) + 1):
            perm = ''.join(all_chars[i:j])
            if perm == perm[::-1]:
                all_perms.add(perm)
    return all_perms