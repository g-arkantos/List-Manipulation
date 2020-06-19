def selection_sort(list1):
	for i in range(0,len(list1)-1):
		minterm=i
		for j in range(i+1,len(list1)):
			if list1[j]<list1[minterm]:
				minterm=j
		if minterm!=i:
			list1[minterm],list1[i]=list1[i],list1[minterm]
		print(list1)		
	return list1			

				
def main():
	list2=list(eval(input('Enter a list to be sorted: ')))
	print('unsorted list: ', list2,)
	selection_sort(list2)
	print( 'sorted list: ', list2)
if __name__=='__main__':
	main()					