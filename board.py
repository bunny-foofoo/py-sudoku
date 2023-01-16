class Sudoku:
	def __init__(self, seed = None) -> None:
		self.tiles = []
		for y in range(9):
			self.tiles.append([0]*9)
		if seed is not None:
			for y, seedling in enumerate(seed):
				if seedling:
					plant = []
					diff = 9 - len(seedling)
					for _ in seedling:
						plant.append(_ if not isinstance(_, str) else int(_))
					plant = plant + ([0] * diff)
					self.tiles[y] = plant

	def box(self, n):
		x = 3 * int(n // 3.1) # seems like this could be improved
		a = int(3 * ((n - 1) % 3))
		return self.tiles[x][a:a + 3] + self.tiles[x + 1][a:a + 3] + self.tiles[x + 2][a:a + 3]
	
	def row(self, n):
		return self.tiles[n - 1]
	
	def column(self, n):
		return [y[n - 1] for y in self.tiles]
	def col(self, n):
		return self.column(n)
	
	def view(self):
		n1 = 0
		for y in self.tiles:
			n1 += 1
			n2 = 0
			for x in y:
				print(x if x != 0 else ' ', end=' ')
				n2 += 1
				if n2 is 3 or n2 is 6:
					print('│', end=' ')
			print()
			if n1 is 3 or n1 is 6:
				print('─'*6, end='')
				print('┼', end='')
				print('─'*7, end='')
				print('┼', end='')
				print('─'*6)
	
	@property
	def rows(self):
		return (self.row(i) for i in range(9))

	@property
	def columns(self):
		return (self.column(i) for i in range(9))

	@property
	def boxes(self):
		return (self.box(i) for i in range(9))

	@property
	def arrays(self):
		for row in self.rows:
			yield row
		for col in self.columns:
			yield col
		for box in self.boxes:
			yield box

	@property
	def is_solved(self):

		n = 1
		c = 0
		for d in self.arrays:
			if sum(d) != 45:
				return False
		return True