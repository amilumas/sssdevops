"""
Main python file for the sssdevops example
July 9, 2018
Amulya Pervaje
RTP center MolSSI bootcamp
"""

#import statements go here


def mean(num_1st):
    """ 
	Calculates the mean of a list of numbers
	
	Parameters
	----------
	num_1st : list
	List of numbers to calculate the averge of

	Returns
	--------
	The average/mean of num_1st
	
	avgMean	
	
	Examples
	--------
	>>> mean([1,2,3,4,5])
	3.0
	"""
    Sum = sum(num_1st)
    N = len(num_1st)
    avgMean = float(Sum/N)

    return avgMean
