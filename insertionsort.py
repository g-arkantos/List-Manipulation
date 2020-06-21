def insertion_sort(lst):
	for i in range(1,len(lst)):
		temp=lst[i]
		j=i-1
		while (j>=0) and (lst[j]>temp):
			lst[j+1]=lst[j]
			j=j--
		lst[j+1]=temp
	return lst	



def main():
	lst=list(eval(input('Enter the contents to the list: ')))
	print(insertion_sort(lst))
if __name__=='__main__':
	main()