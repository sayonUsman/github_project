def binary_search(list, search_item):
	
	left_index = 0
	
	right_index = len(list) - 1
	
	while left_index <= right_index:
		
		mid_index = left_index + (right_index - left_index) // 2
		
		if list[mid_index] == search_item:
			
			return mid_index
			
		elif list[mid_index] < search_item:
			
			left_index = mid_index + 1
			
		else:
			
			right_index = mid_index - 1
			
			
list = list(map(int, input("Please enter the items of list:\n").split()))

search_item = int(input("Pleae enter the search item:\n"))

index_item = binary_search(list, search_item)

print("The index of search item is", index_item)