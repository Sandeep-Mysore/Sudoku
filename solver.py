def print_grid(arr):
	for i in range (0,9):
		for j in range(0,9):
			print arr[i][j]
		print ""
	

def used_in_row(arr,row,n):
	for j in range(0,9):
			if(arr[row][j]==n):
				return False
	return True

def used_in_col(arr,col,n):
	for j in range(0,9):
			if(arr[j][col]==n):
				return False
	return True

def used_in_box(arr,row,col,n):
	for i in range (row,row+3):
		for j in range(col,col+3):
			if(arr[i][j]==n):
				return False
	return True

def check_location(arr,row,col,n):
	return used_in_row(arr,row,n) and used_in_col(arr,col,n) and used_in_box(arr,row-row%3,col-col%3,n)

def find_empty_location(arr,l):
	for i in range (0,9):
		for j in range(0,9):
			if(arr[i][j]==0):
				l[0]=i
				l[1]=j
				return True
	return False

def solve_sudoku(arr):
	l=[0,0]
	if(not find_empty_location(arr,l)):
		return True
	row=l[0]
	col=l[1]
	for n in range(1,10):
		
		if(check_location(arr,row,col,n)):
			arr[row][col]=n
			if(solve_sudoku(arr)):
				return True
			arr[row][col]=0
	return False

