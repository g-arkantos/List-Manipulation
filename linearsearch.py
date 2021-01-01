import re
def linear_search(lst,element):
	element=str(element)
	print(lst)
	for element in lst:
		print("lst: ", len(lst))
		print("Search.element: " ,element)
		#if element==i:
		print('found in position:', lst.index(element) )
		break 
def main():
	liste=str(input('Enter the list here: '))
	liste=re.split("\s",liste)
	print("type: ", type(liste) )
	search=int(input('Enter you search element: '))
	linear_search(liste,search)
if __name__=='__main__':
	main()	


