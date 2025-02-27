def return_binary_or_hexa(args):
    start, finish = (args[50], args[92])
    s = sum((i for i in range(start + 1, finish) if i not in args[50:92]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()