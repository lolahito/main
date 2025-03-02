
import numpy as np

def check( a: np.ndarray, b: np.ndarray ):
	size = [ 1 ]
	ret = True
	rotated = rotate( b )
	for _ in a.shape:
		size.append( size[-1] * _ )

	for i in range(size[-1]):
		c = tuple( reversed( [ ( i % size[_+1] )//size[_] for _ in range(len(size)-1) ] ) )
		for shape in rotated:
			tmp = False
			for _ in range( len( a.shape ) ):
				if c[_] + shape.shape[_] > a.shape[_]:
					tmp = True
					break
			if tmp:
				continue
			tmp = False
			for x in range( shape.shape[0] ):
				for y in range( shape.shape[1] ):
					#tmp = tmp or ( shape[x][y] and a[c[0] + x][c[1] + y] )
					tmp = tmp or ( shape[ x, y ] and a[ tuple_add( (x, y), c ) ] )
			ret = ret and tmp
			if not ret:
				break
		if not ret:
			break

	return ret

def rotate( a: np.ndarray ):
	ret = [ a ]
	for _ in range( 3 ):
		ret.append( np.rot90( ret[-1] ) )

	return ret

def tuple_add( a, b ):
	return tuple( map( lambda x, y: x + y, a, b ) )
