from csvFromTxt import sorted_df
import matplotlib.pyplot as plt
x = sorted_df["BasicPunchLvl"]
y = sorted_df["WinsAchieved"]

fig = plt.figure(figsize = (10, 10))
sorted_x, sorted_y = zip(*sorted(zip(x, y)))
plt.plot(sorted_x, sorted_y, color='green', marker='o', linestyle='dashed',
     linewidth=0.1, markersize=2)
plt.xlabel("BasicPunchLvl")
plt.ylabel("WinsAchieved")
plt.show()