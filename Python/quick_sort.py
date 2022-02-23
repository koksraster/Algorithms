import random as r

def quick_sort(lst):
	if len(lst) < 2:
		return lst
	else:
		 basic = lst[0]
		 less  = [i for i in lst[1:] if i <= basic]
		 greater = [i for i in lst[1:] if i > basic]
		 return quick_sort(less) + [basic] + quick_sort(greater)

r_radius = r.randint(5,10)
lst = []

for i in range(1, r_radius):
	r_count = r.randint(1,100)
	lst.append(r_count)

print("Неотсортированный список -", lst)
q_s = quick_sort(lst)

print("Отсортированный список -", q_s)
