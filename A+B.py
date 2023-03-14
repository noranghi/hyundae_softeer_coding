import sys

case = int(input())
i = 0

while i < case:
    a, b = map(int, input().split())
    print(("Case #{}: {}").format(i + 1, a + b))
    i += 1
