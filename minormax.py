A = [6,8,18,18,95,26]
def maxormin(A):
	if len(A)%2 != 0:
		mi = A[0]
		ma = A[0]
		for i in range(1,len(A),2):
			if A[i] > A[i+1]:
				ma = A[i]
			else:
				mi = A[i]
	else:
		for i in range(0,len(A),2):
			if A[i] > A[i+1]:
				ma = A[i]
			else:
				mi = A[i]
	return (mi,ma)
print maxormin(A)