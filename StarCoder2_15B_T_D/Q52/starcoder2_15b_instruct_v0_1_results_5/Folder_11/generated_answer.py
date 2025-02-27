import re

def palindrome_of_length_n(string):
    pattern = '.(?i)(?:\\w{77})(?<-1>\\w)'
    return set(re.findall(pattern, string))