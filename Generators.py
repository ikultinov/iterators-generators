nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def flat_generator(list):
	cnt = 0
	count = 0
	while cnt < len(list):
		while count < len(list[cnt]):
			yield list[cnt][count]
			count += 1
		cnt += 1
		count = 0


for item in flat_generator(nested_list):
	print(item)
