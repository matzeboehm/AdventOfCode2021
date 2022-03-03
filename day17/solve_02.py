x_target = (153, 199)
y_target = (-114, -75)

xt_min = min(x_target)
xt_max = max(x_target)
yt_min = min(y_target)
yt_max = max(y_target)

maxHeight = 0
possibleSolutions = []

def uniqueSolutions(vx_s, vy_s):
        vx = vx_s
        vy = vy_s
        
        x = 0
        y = 0

        while True:
            if x > xt_max:
                return False
            elif vx == 0 and not xt_min <= x <= xt_max:
                return False
            elif vx == 0 and y < yt_min:
                return False
           
            if xt_min <= x <= xt_max and yt_max >= y >= yt_min:
                return True

            x += vx
            y += vy
            
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1

for vx_s in range(1, 200):
    for vy_s in range(-116, 116):
        if uniqueSolutions(vx_s, vy_s):
            possibleSolutions.append((vx_s, vy_s))

print(len(possibleSolutions))