"""
Miscellaneous list manipulation
"""



def split(in_list,index):
	"""
	
	Parameters
	------------
	in_list: list
	index: int

	Returns
	----------
	Two lists, spliting in_list by 'index'

	Examples
	_________
	>>> split(['a', 'b', 'c', 'd'],3)
	(['a', 'b', 'c'], ['d'])
	"""
	
	list1 = in_list[:index]
	list2 = in_list[index:]

	return in_list[:index], in_list[index:]

