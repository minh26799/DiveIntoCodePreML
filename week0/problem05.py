THICKNESS = 0.00008
folded_thickness_array = [THICKNESS]
for i in range(0,43):
    folded_thickness_array.append(folded_thickness_array[i]*2)
print("Thichness: {} meters.\nThe Length of array: {} elements".format(folded_thickness_array[43], len(folded_thickness_array)))