
y = ["this", "is", "a", True, "test"]
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[:6]
print(downstairs)

upstairs = areas[6:]
print(upstairs)

x = ["a", "b", "c"]
x = x + ['d']
print(x)

areas[-1] = 10.50
print(areas)
areas[4] = "chill zone"

areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)
help(round)


x = "monty python says hi!"

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0))

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.append(24.5)
areas.append(15.45)
areas

import numpy as np
x = np.array([["a", "b", "c", "d"],["e", "f", "g", "h"]])
x[1][2]

x = np.array([[1, 2, 3],
              [1, 2, 3]])
y = np.array([[1, 1, 1],
              [1, 2, 3]])
z = x - y

z