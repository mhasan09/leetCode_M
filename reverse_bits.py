def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) ^ (n & 1)
        n = n >> 1
    return result
