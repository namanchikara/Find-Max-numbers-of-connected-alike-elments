## Simpler version of FindMax.py

arr = [
    '1 0 1 2 2 2 2 1 1'.split(),
    '1 0 1 1 2 2 0 0 0'.split(),
    '1 1 1 2 2 2 2 1 0'.split()
]


def validXY(x,y):
    if x > -1 and y > -1 and x < len(arr) and y < len(arr[0]):
        return True
    return False


from collections import defaultdict
visited = defaultdict(lambda : False)

def connected(x,y):
    count = 1
    visited[(x,y)] = True
    if validXY(x+1,y) and not visited[(x+1,y)] and arr[x+1][y] == arr[x][y]:
        count += connected(x+1,y)

    if validXY(x,y+1) and not visited[(x,y+1)] and arr[x][y+1] == arr[x][y]:
        count += connected(x,y+1)

    if validXY(x-1,y) and not visited[(x-1,y)] and arr[x-1][y] == arr[x][y]:
        count += connected(x-1,y)

    if validXY(x,y-1) and not visited[(x,y-1)] and arr[x][y-1] == arr[x][y]:
        count += connected(x,y-1)

    return count

ans = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if not visited[(i,j)]:
            ans.append(connected(i,j))
print(ans)
