import argparse
import pandas as pd
import numpy as np
import sys

'''

'''
class DataFill(object):
	def __init__(self, params):
		self.column = params.column
		self.command = params.command
		try:
			self.df = pd.read_csv(params.input_file, keep_default_na=True, encoding='utf-8')
		except FileNotFoundError:
			print("File Parse Meet Unexpected Error, Please Check It")

		# get the na section
		need_fill = self.df.isnull().any()
		self.data_tmp = dict(need_fill)

	def col_stat(self):
		# miss value
		if self.command == 'miss':
			if self.column in self.data_tmp.keys():
				print(self.column)
				if self.data_tmp.get(self.column) == True:
					try:
						# do action
						self.df[params.column] = self.df[params.column].fillna(np.nan)
					except ArithmeticError:
						print("Error")
				else:
					print("No Need DO Update Action")

		# average value
		elif self.command == 'average':
			if self.column in self.data_tmp.keys():
				print(self.column)
				if self.data_tmp.get(self.column) == True:
					try:
						# do action
						self.df[params.column] = self.df[params.column].fillna(self.df[self.column].mean())
					except ArithmeticError:
						print("Error")
				else:
					print("No Need DO Update Action")

		# fixed value
		elif self.command == 'fixed':
			if params.fixed_value is None:
				raise BaseException("variable [fixed_value] is missing")
			else:
				fixed_value = params.fixed_value
				if fixed_value.strip() == "":
					raise BaseException("variable [fixed_value] is missing")
				else:
					# do action
					if self.column in self.data_tmp.keys():
						print(self.column)
						if self.data_tmp.get(self.column) == True:
							try:
								# do action
								self.df[params.column] = self.df[params.column].fillna(fixed_value)
							except ArithmeticError:
								print("Error")
						else:
							print("No Need DO Update Action")

		# median value
		elif self.command == 'median':
			if self.column in self.data_tmp.keys():
				print(self.column)
				if self.data_tmp.get(self.column) == True:
					# do action
					self.df[params.column] = self.df[params.column].fillna(self.df[self.column].median())
				else:
					print("No Need DO Update Action")
		else:
			raise Exception('This stat is not currently supported.')

		# re-write the output file
		self.df.to_csv(params.output_file, index=False, encoding='utf-8')
		print(self.df)


if __name__ == "__main__":
	# define a flag
	flag = True

	parser = argparse.ArgumentParser(description='Data Fill Testing')
	parser.add_argument("--column", type=str, help='Column of the csv dataset')
	parser.add_argument("--command", type=str, help='Command')
	parser.add_argument("--fixed_value", type=str, help='Fixed Value')
	parser.add_argument("--input_file", type=str, help='Input csv dataset')
	parser.add_argument("--output_file", type=str, help='Output csv dataset')
	params, _ = parser.parse_known_args()

	# verify the standard command format
	if params.column is None:
		flag = False
		raise BaseException("variable [column] is missing")

	if params.command is None:
		flag = False
		raise BaseException("variable [command]  is missing")

	if params.input_file is None:
		flag = False
		raise BaseException("variable [source file] is missing")

	# decide to do or not
	if flag is False:
		sys.exit(1)

	# init
	csv_fill = DataFill(params)
	# call the main function
	csv_fill.col_stat()
