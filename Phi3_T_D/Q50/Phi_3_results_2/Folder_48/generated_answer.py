def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_anagram(pair):
        return normalize(pair[0]) == normalize(pair[1])
    anagram_groups = {}
    for s in strings_list:
        if len(s) >= 3:
            normalized = normalize(s)
            if normalized in anagram_groups:
                anagram_groups[normalized].append(s)
            else:
                anagram_groups[normalized] = [s]
    count = 0
    for group in anagram_groups.values():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                if has_anagram((group[i], group[j])):
                    count += 1
    return count >= 219