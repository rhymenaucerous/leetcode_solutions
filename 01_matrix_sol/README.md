# leetcode_solutions
My solutions for github problems

# Solve attempt 1
This solution is a depth first approach to solving the problem. Each for loop iteration finds all values that are next to zero and increments one of the copies values. It then subtracts all of those values to zero and re-runs the loop. This solution works great when the distance to the nearest zero is low. When there are high distances to the next zero the solution can take a much longer period of time and fails at 49/50 test cases.

# Solve attempt 2
the second attemp was much quicker with a breadth first approach to the problem. All members of the matrix are multiplied by infinity (so we know which haven't been updated) and the indexes (x, y coordinates) that correspond to values in the matrix which are 0 are added to a queue. Each of their neighbors are searched for higher values and if they are higher then they are updated with just one higher than the index being searched. IF they have been updated, then they are added to the queue for their neighbors to be searched. For this situation, then, the optimal method is not found but it is significantly faster than our first attempt.

End of README.md file
