import unittest
from NewSolution import solution

class TestSolution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue (solution(10,20,"+"),30)
	def test_subtraction(self):
		self.assertTrue (solution(10,20,"-"),10)
	def test_division(self):
		self.assertTrue (solution(10,20,"%"),2)
	def test_multiplication(self):
		self.assertTrue (solution(10,20,"*"),200)
	def test_modulers(self):
		self.assertTrue (solution(15,2,"%"),1)

if __name__ == '__main__':
    unittest.main()


		