import sys

l = list(map(int, input().split()))

if l[0] == 1:
    ans = "ascending"
elif l[0] == 8:
    ans = "descending"
else:
    ans = "mixed"

if ans != "mixed":
    if ans == "ascending":
        for i in range(1, 8):
            if l[i] == l[i-1] + 1:
                continue;
            else:
                ans = "mixed"
                break;
    if ans == "descending":
        for i in range(1, 8):
            if l[i] == l[i-1] - 1:
                continue;
            else:
                ans = "mixed"
                break;
print(ans)