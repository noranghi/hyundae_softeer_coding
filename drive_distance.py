import sys

A, B = map(int, input().split())

if A and B >= 0 and A and B <= 100000:
    if A > B:
        print("A")
    elif A < B:
        print("B")
    elif A == B:
        print("same")