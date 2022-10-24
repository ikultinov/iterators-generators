
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, some_obj):
		self.some_obj = some_obj
		self.new_list = []

	def unpacking(self):
		for elements in self.some_obj:
			for element in elements:
				self.new_list.append(element)
		return self.new_list

	def __iter__(self):
		self.cnt = 0
		self.element = iter(self.unpacking())
		return self

	def __next__(self):
		if self.cnt == len(self.new_list):
			raise StopIteration
		next_element = next(self.element)
		self.cnt += 1
		return next_element


if __name__ == '__main__':
	for item in FlatIterator(nested_list):
		print(item)

	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)
