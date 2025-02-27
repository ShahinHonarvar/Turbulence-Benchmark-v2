def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            n1 = normalize(strings[i])
            n2 = normalize(strings[j])
            if n1 == n2 and len(strings[i]) >= 3:
                count += 1
                if count > 116:
                    return False
                seen.add(n1)
    return True