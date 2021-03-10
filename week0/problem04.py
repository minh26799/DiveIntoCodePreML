import time
start = time.time()
#####
THICKNESS = 0.00008
folded_thickness = THICKNESS*2
for i in range(42):
    folded_thickness *= 2
print("Thichness: {} meters".format(folded_thickness))
#####
elapsed_time = time.time() - start
print(elapsed_time)
print("time : {: .20f}[s]".format(elapsed_time))
"""
In this part, I test for the normal calculation by using multiple operator * and using the loop to calculate.
However, I think because the code here is not really complicated,
the execution time is too small to have a accuracy comparison
"""
