"""
File: matform.py

Author: Gerard Geer <gerarddgeer@gmail.com>

License: MIT License

Allows users to enter a matrix in a _delightful_ manner, formats it
for Wolfram Alpha, then copies it to the clipboard automatically.
"""

# Import clipboard library to access clipboard.
import pyperclip

# A list to store the rows of the matrix.
rows = []

# A string to store the current row being entered.
row_buffer = 'null'

# A string to store the Wolfram-formatted result.
formatted = '';

def formatMatrix(elements):
	"""
	Formats a list of strings into a Wolfram matrix.
	
	Parameters:
		data (1D or 2D list): The data to format.
		
	Returns:
		The row, formatted.
		
	Preconditions:
		The given row is properly formatted.
		
	Postconditions:
		None.
	"""
	# Open brace.
	f = '{'
	# Go through the elements of the data and comma
	# delimit them.
	for i in range(len(elements)):
		
		# Get the current element.
		element = elements[i]
		# If that element is a list, err, row,
		# we recurse down and format it.
		if isinstance(element, list):
			element = formatMatrix(element)
		# Append the element to the string we're building.
		f += element
		# If it's not the last element, we also need
		# to add the delimiting comma.
		if i < len(elements)-1:
			f += ','
		
	# Close and return our formatted matrix.
	f += '}'
	return f
	
def main():
	"""
	The main function of the matrix formatter.
	"""
	# Get the first row from the user.
	row_buffer = input('r --> ')
	
	# if a non zero string is entered, we go ahead and parse it.
	while len(row_buffer) > 0:
		# Split the string over spaces.
		elements = row_buffer.split()
		# Append the returned list to our rows container.
		rows.append(elements)
		# Get the next row.
		row_buffer = input('r --> ')
	
	# Format the matrix.
	formatted = formatMatrix(rows)

	# print and store the formatted matrix.
	print(formatted)
	pyperclip.copy(formatted)
	
if __name__ == '__main__':
	main()