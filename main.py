
import numpy as np
from iterate import iteration
from check import check
import time

start_time = time.perf_counter()
'''
棋盤: (6, 6), (3, 3),
T: (0,0), (0,1), (0,2), (1,1), (2,1)

Z: (0,0), (0,1), (1,1), (1,2)

H: (0,0), (1,0), (2,0), (0,1), (1,1), (0,2), (1,2), (2,2)

口: (0,0), (1,0), (0,1), (1,1), (0,2), (2,2)
'''

def main( argv ):
	
	_ = eval( f"[ {input( 'list of tuples, first 2 are dimensions for board and shape: ' )} ]" )
	print()
	dim = _.pop(0)
	shape = np.zeros( _.pop(0), dtype = np.bool )
	for c in _:
		shape[c] = True
	n, k = run( dim, shape )
	print( f"\nMin: {n}\n{sprintf( k )}" )
	return

def run( dim, shape ):
	import math
	l = 0
	r = math.prod( dim )
	m_min = r
	k_min = None
	while l < r:
		m = ( ( r - l ) >> 1 ) + l
		t = True
		for i, comb in enumerate( iteration( dim, m ) ):
			print( f"checking {m}: {i}", end = '\r' )
			if check( comb, shape ):
				break
		else:
			t = False

		if t:
			# record min condition
			if m < m_min:
				k_min = comb
				m_min = m
			# go lower
			r = m
			print( f"\n{sprintf(comb)}" )
		else:
				# go higher
				l = m + 1
	return m_min, k_min

def sprintf( t: np.ndarray ):
	return str( t ).replace( "False", "X" ).replace( "True", "O" ).replace( "[ ", "[" ).replace( "  ", " " )

if __name__ == "__main__":
	import os
	main( os.sys.argv )
	
	end_time = time.perf_counter()
print(f"程式執行時間: {end_time - start_time:.2f} 秒")
