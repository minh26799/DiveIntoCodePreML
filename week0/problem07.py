import matplotlib.pyplot as plt

THICKNESS = 0.00008
folded_thickness_array = [THICKNESS]
for i in range(0,43):
    folded_thickness_array.append(folded_thickness_array[i]*2)

plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.rc('font', size = 18) # I change the font size into 18, so the text can be displayed clearly
plt.tick_params(labelsize=20) # Make settings related to axis values
plt.plot(folded_thickness_array, color='yellow') # I change the color of the line to yellow
plt.plot(folded_thickness_array, 'p') # I display each value of folded thickness after each calculation
plt.show()