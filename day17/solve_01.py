x_target = (153, 199)
y_target = (-114, -75)
xt_min = min(x_target)
xt_max = max(x_target)
yt_min = min(y_target)
yt_max = max(y_target)

maxHeight = 0
possibleSolutions = []

for vx_s in range(1,150):
    for vy_s in range(1,150):
        vx = vx_s
        vy = vy_s
        
        x = 0
        y = 0
        maxVal = 0

        while y > yt_max:
            x += vx
            if vx != 0:
                vx -= 1
            y += vy
            vy -= 1

            maxVal = max(y, maxVal)

            if xt_min <= x <= xt_max and yt_max >= y >= yt_min:
                maxHeight = max(maxHeight, maxVal)

print(maxHeight)