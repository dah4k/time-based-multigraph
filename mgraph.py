from string import ascii_uppercase
from string import digits
from time import time

ALPHABET = digits + ascii_uppercase
ALPHABET_SIZE = len(ALPHABET)


# Period is 36^2 seconds (21 minutes)
def digraph(num: int | None = None) -> str:
    if num == None:
        num = int(time())
    return _encode_multigraph(2, num)


# Period is 36^3 seconds (about 12 hours)
def trigraph(num: int | None = None) -> str:
    if num == None:
        num = int(time())
    return _encode_multigraph(3, num)


def _encode_multigraph(N: int, num: int) -> str:
    if num == 0:
        return "0" * N

    result = ""
    bucket = num % (ALPHABET_SIZE**N)
    while bucket != 0:
        bucket, index = divmod(bucket, ALPHABET_SIZE)
        result = ALPHABET[index] + result

    return result.zfill(N)
