import numpy as np

def calculate(list_elements):
	if len(list_elements) < 9:
        	raise ValueError ('List must contain nine numbers.')
        
	array = np.array(list_elements)
	matrix = array.reshape(3,3)
    
	calculations = {}
	calculations['mean'] = [list(matrix.mean(axis = 0,)), list(matrix.mean(axis=1)), array.mean()]
    
	calculations['variance'] = [list(matrix.var(axis = 0)), list(matrix.var(axis=1)), array.var()]
	calculations['standard deviation'] = [list(matrix.std(axis =0)), list(matrix.std(axis=1)), array.std()]
	calculations['max'] = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), array.max()]
	calculations['min'] = [list(matrix.min(axis=0)), list(matrix.min(axis = 1)), array.min()]
	calculations['sum'] = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), array.sum()]
    
	return calculations
