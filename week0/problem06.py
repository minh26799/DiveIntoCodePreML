import matplotlib.pyplot as plt

THICKNESS = 0.00008
folded_thickness_array = [THICKNESS]
for i in range(0,43):
    folded_thickness_array.append(folded_thickness_array[i]*2)
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(folded_thickness_array)
plt.show()
# In this case, the more the calculation is executed, the bigger the value is.
# Therefore, when draw a graph to dis play the value of folded thickness, those first times is really small compare to the fourty-three times.
# As a result, we cannot have a good view of the changing value in some first times.