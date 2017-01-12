import os

class SampleData:
	def __init__(self,forward_file, reverse_file):
		self.forward_file = forward_file
		self.reverse_file = reverse_file
		self.database_name = ''
		self.file_of_fastq_files = ''
		self.basename = self.calculate_basename(forward_file)
		self.filtered_forward_file=''
		self.filtered_reverse_file=''
		
	def calculate_basename(self,filename):
		basename = os.path.basename(filename)
		basename = basename.replace('.gz','')
		basename = basename.replace('_1.fastq','')
		return basename
