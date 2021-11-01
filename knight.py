


"""
position = input()
x = int(ord(position[0])-ord('a')+1)
y = int(position[1])
steps = [ (-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
result = 0
for step in steps:
    nex_x = x + step[0]
    nex_y = y + step[1]
    if nex_x > 0 and nex_x < 9 and nex_y > 0 and nex_y < 9:
        result += 1

print(result)
"""