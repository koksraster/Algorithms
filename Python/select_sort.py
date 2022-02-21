import random as r

def search_small(lst):
	small_index = lst[0]
	small = 0

	for i in range(1, len(lst)):
		if lst[i] < small_index:
			small_index = lst[i]
			small = i
	return small

def select_sort(lst):
	new_lst = []

	for i in range(len(lst)):
		small = search_small(lst)
		new_lst.append(lst.pop(small))
	return new_lst

r_radius = r.randint(5,10)
lst = []

for i in range(1, r_radius):
	r_count = r.randint(1,100)
	lst.append(r_count)

print("Неотсортированный список -", lst)

sort = select_sort(lst)
print("Отсортированный список -", sort)
