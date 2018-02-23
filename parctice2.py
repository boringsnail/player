import random
A = [1,85,4815,8,6,78,848,4,48,489,84,48,488,45,132,32]
def partition(A,p,r):
	x = A[p]
	i = p-1
	for j in range(p,r+1):
		if A[j] <= x:
			i += 1
			A[i],A[j] = A[j],A[i]
	A[i],A[p] = A[p],A[i]
	return i
def random_partition(A,p,r):
	i = random.randint(p,r)
	A[i],A[p] = A[p],A[i]
	return partition(A,p,r)
def quicksort(A,p,r):
	if p<r:
		q = random_partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)
quicksort(A,0,len(A)-1)
print (A)

def random_select(A,p,r,i):
	if p == r:
		return A[p]
	q = random_partition(A,p,r)
	k = q-p+1
	if i == k:
		return A[q]
	elif i <k:
		return random_select(A,p,q-1,i)
	else:
		return random_select(A,q+1,r,i-k)

print A


def merger(A,p,q,r):
	n1 = q-p+1
	n2 = r-q
	L = range(n1+1)
	R = range(n2+1)
	for i in range(n1):
		L[i] = A[p+i-1]
	for j in range(n2):
		R[j] = A[q+j]
	i = j = 0
	L[n1] = R[n2] = "m"
	for k in range(p-1,r):
		if L[i] < R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
def merger_sort(A,p,r):
	if p<r:
		q = (p+r)/2
		merger_sort(A,p,q)
		merger_sort(A,q+1,r)
		merger(A,p,q,r)
merger_sort(A,1,len(A))
print A

