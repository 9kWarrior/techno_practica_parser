from csvFromTxt import sorted_df
import matplotlib.pyplot as plt
import numpy as np
i = 0
x = sorted_df["Mass"]
y = sorted_df["WinsAchieved"]
z = sorted_df["Speed"]
onlyTimer = sorted_df["DeadByTimer"]

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection='3d')
sorted_x, sorted_y, sorted_z = zip(*sorted(zip(x, y, z)))
ax.plot(sorted_x, sorted_y, sorted_z, color='green', marker='o', linestyle='dashed',
     linewidth=0.1, markersize=4)
ax.set_xlabel("Mass")
ax.set_ylabel("WinsAchieved")
ax.set_zlabel("Speed")
plt.show()
# print(sorted_df["BotNumber"])