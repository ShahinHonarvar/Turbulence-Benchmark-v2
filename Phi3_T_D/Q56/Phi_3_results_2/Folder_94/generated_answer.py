def all_substring_of_size_n(s):
    substr_set = set()
    substring_count = {}
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == len(substring):
            substring_count[substring] = substring_count.get(substring, 0) + 1
            substr_set.add(substring)
    return list(substr_set)