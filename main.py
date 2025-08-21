import sys
from functools import reduce

def process_case(data):
    if not data:
        return None, data
    x, *rest = data
    try:
        x = int(x)
    except ValueError:
        return -1, rest
    if len(rest) < x:
        return -1, rest[x:]
    nums = rest[:x]
    rest = rest[x:]

    try:
        nums = list(map(int, nums))
    except ValueError:
        return -1, rest

    if len(nums) != x:
        return -1, rest

    negs = filter(lambda n: n <= 0, nums)
    total = reduce(lambda acc, n: acc + n**4, negs, 0)
    return total, rest

def handle_cases(n, data):
    if n == 0:
        return []
    result, rest = process_case(data)
    return [result] + handle_cases(n - 1, rest)

def main():
    content = sys.stdin.read().strip().split()
    if not content:
        return
    n, *rest = content
    n = int(n)
    results = handle_cases(n, rest)
    sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
