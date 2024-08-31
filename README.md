
Step1: We first check if the number of positions is negative. If so, a ValueError is raised.

Step2: The effective number of rotations is calculated using positions % n. This ensures that even if the number of positions is greater than the length of the array, the rotations are handled correctly.

Step3: We then slice the array into two parts and concatenate them in reversed order to achieve the left rotation.
