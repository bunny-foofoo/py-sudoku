from board import Sudoku
from solver import Solver

def test_seeded_board(seed):
	board = Sudoku(seed=seed)
	board.view()
	print('Solved' if board.is_solved else 'Not solved')

def test_solve(seed):
	sol = Solver(Sudoku(seed=seed))
	sol.board.view()
	print('solver running')
	sol.solve()
	sol.board.view()
	print('Solved' if sol.board.is_solved else 'Not solved')

if __name__ == '__main__':
	print('Board creation ... & Solved state checking')
	test_seeded_board(seed=['40927', '000400030', [0, 1, 6,   0, 8, 0,   0, 0, 7], '00060902', '804501763', '265708409', '10006','04200038','000800104'])

	print()

	test_seeded_board(seed=[
		'154893762',
		'798652134',
		'362741985',
		'427536891',
		'513978426',
		'986124573',
		'249385617',
		'831467259',
		'675219348',
	])

	print()

	print('Solving ...')
	test_solve(['40927', '000400030', [0, 1, 6,   0, 8, 0,   0, 0, 7], '00060902', '804501763', '265708409', '10006','04200038','000800104'])

	print()

	print('Solving ...')
	test_solve([
		'154893762',
		'798652134',
		'362741985',
		'427536891',
		'513978426',
		'986124573',
		'249385617',
		'831467259',
		'675219340',
	])