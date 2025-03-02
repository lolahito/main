
import numpy as np

def iteration ( dim : tuple, n : int ):

	if not n:
		return

	size = [ 1 ] 
	for _ in dim:
		size.append(size[-1] * _ )

	stat = np.zeros( size[-1] + 1, dtype=np.bool )
	k = np.zeros( size[-1], dtype=np.bool )

	i = 0
	c = 0

	while i >= 0:
		if size[-1] - i + c < n :
			i -= 1
			c -= int( k[i] )
		if c == n:
			for _ in range( i, size[-1] ):
				k[_] = False

			yield np.array( k[ : size[-1] ], dtype=np.bool ).reshape( dim )

			i -= 1
			c -= int( k[i] )
		if k[i]:
			stat[i] = not stat[i]
		if stat[i] and  not k[i]:
			i -= 1
			c -= int( k[i] )
			continue
		k[i] = not k[i]
		c += int( k[i] )
		i += 1
		stat[i] = False

if __name__ == "__main__":
	#pdb.set_trace()
	print( list( iteration( (5, 5), 0 ) ) )
