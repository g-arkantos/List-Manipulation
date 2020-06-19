def bubble_sort(list1):
	for i in range(len(list1)-1):
		for j in range(i+1, len(list1)):
			if list1[i]>list1[j]:
				list1[j],list1[i]=list1[i],list1[j]
def main():
	list2=list(eval(input('Enter a list to be sorted: ')))
	print('unsorted list: ', list2,)
	bubble_sort(list2)
	print( 'sorted list: ', list2)
if __name__=='__main__':
	main()				

