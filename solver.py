class Solver:
	def __init__(self, board) -> None:
		self.board = board
	
	def _possible(self, y, x, n):
		if n in self.board.row(y):
			# print(f'found {n} at row {y}')
			return False

		if n in self.board.column(x):
			# print(f'found {n} at col {x}')
			return False
		
		try:
			if n in self.board.box(round(x%3.1) + (3 * (y//3.1))):
				# print(f'found {n} in box {(2 * (x%3.1)) + (3 * ((y//3.1)-1))}')
				return False
		except TypeError:
			print(f'failed at: ({y}, {x}, {n})')
			raise IndexError()
		
		# print(n, 'not found')
		return True

	def solve(self):
		for x in range(9):
			for y in range(9):
				if self.board.tiles[y][x] == 0:
					# print(f'0 found at ({y, x}) y,x')
					for n in range(1, 10):
						if self._possible(y + 1, x + 1, n):
							self.board.tiles[y][x] = n
							# self.board.view()
							r = self.solve()
							if not r:
                                # Backtrack
								self.board.tiles[y][x] = 0
						#else:
							# print(n, 'is impossible')
					return False
		return True
		print('Solved' if self.board.is_solved else 'Not solved')
