import unittest
import os
import tempfile
import shutil
from plasmidtron.PlotKmers import PlotKmers

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','plotkmers')

class TestPlotKmers(unittest.TestCase):
	
	def test_get_kmers_from_db(self):
		'''Given a database extract the kmers into an array'''
		temp_working_dir = tempfile.mkdtemp(dir=os.path.abspath(data_dir))
		p = PlotKmers([],temp_working_dir,1,31,255, False, 'kmerplot.png', 100)
		kmers  = p.get_kmers_from_db(os.path.join(data_dir,'simple_kmers'))
		self.assertEqual(kmers, ['AAAAAAAAAAAGAAAAAAAAAAAAA', 'AAAAAAAAAAGAAAAAAAAAAAAAA'])
		shutil.rmtree(temp_working_dir)
	
	def test_three_samples(self):
		'''Given 3 samples with some shared kmers make a plot'''
		temp_working_dir = tempfile.mkdtemp(dir=os.path.abspath(data_dir))
		p = PlotKmers([os.path.join(data_dir,'sample1.fa'), os.path.join(data_dir,'sample2.fa'), os.path.join(data_dir,'sample3.fa')], temp_working_dir, 1, 21, 255, False, 'kmerplot.png', 100)
		p.generate_plot()
		self.assertTrue(os.path.exists(p.output_filename()))
		shutil.rmtree(temp_working_dir)