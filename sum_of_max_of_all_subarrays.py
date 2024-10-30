# Python3 implementation of the above approach
import sys 

seg_max = 51
	
# Array to store segment tree.
# In first we will store the maximum
# of a range
# In second, we will store index of
# that range
seg_tree = [[] for i in range(seg_max)]

# Function to build segment tree
def buildMaxTree(l, r, i, arr):
	global n, seg_tree, seg_max
	# Base case
	if l == r:
		seg_tree[i] = [arr[l], l]
		return seg_tree[i]

	# Finding the maximum among left and right child
	seg_tree[i] = max(buildMaxTree(l, int((l + r) / 2), 2 * i + 1, arr), buildMaxTree(int((l + r) / 2) + 1, r, 2 * i + 2, arr))

	# Returning the maximum to parent
	return seg_tree[i]

# Function to perform range-max query in segment tree
def rangeMax(l, r, arr, i, sl, sr):
	global n, seg_tree, seg_max
	
	# Base cases
	if sr < l or sl > r:
		return [-sys.maxsize, -1]
	if sl >= l and sr <= r:
		return seg_tree[i]

	# Finding the maximum among left and right child
	return max(rangeMax(l, r, arr, 2 * i + 1, sl, int((sl + sr) / 2)), rangeMax(l, r, arr, 2 * i + 2, int((sl + sr) / 2) + 1, sr))

def Max(f, s):
	if f[0] > s[0]:
		return f
	else:
		return s

# Function to find maximum sum subarray
def maxSumSubarray(arr, l, r):
	# base case
	if l > r:
		return 0

	# range-max query to determine
	# largest in the range.
	a = rangeMax(l, r, arr, 0, 0, n - 1)

	# divide the array in two parts
	return a[0] * (r - a[1] + 1) * (a[1] - l + 1) + maxSumSubarray(arr, l, a[1] - 1) + maxSumSubarray(arr, a[1] + 1, r)

# Input array
arr = [ 1, 3, 1, 7 ]

# Size of array
n = len(arr)

# Builind the segment-tree
buildMaxTree(0, n - 1, 0, arr)

print(maxSumSubarray(arr, 0, n - 1))

# This code is contributed by decode2207.
