import os
import unittest
from diskspace import diskspace

class DiskSpaceTest(unittest.TestCase):

	def test_subprocess_check_output(self):
		command = 'du -d 1 ../01--GesielFreitas'
		return_output = diskspace.subprocess_check_output(command)
		
		self.assertIsInstance(return_output, bytes)
		self.assertIsNotNone(return_output)

	
	def test_bytes_zero(self):
		bit = 0
		bytes_size = diskspace.bytes_to_readable(bit)
		self.assertEqual('0.00B', bytes_size)
		self.assertNotEqual('1.00B', bytes_size)
		self.assertIsNotNone(bytes_size)
		self.assertIsInstance(bytes_size, str)

	def test_bytes_two(self):

		bytes_size = diskspace.bytes_to_readable(2)
		self.assertEqual('1.00Kb', bytes_size)
		self.assertIsInstance(bytes_size, str)



