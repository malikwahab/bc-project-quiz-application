import unittest
from database import QuizToDb
from quiz import Quiz

class QuizDbTest(unittest.TestCase):
	
	db = QuizToDb("testdb.db")

	def test_list_quizzes(self):
		#quiz in db at writing time
		expected = ['Sample Quiz', 'Another Sample Quiz','A Cool Title', 'Quiz from Json', 'A moddified version', 'Options should be okay now']
		self.assertEqual(expected, self.db.listquizzes())
	def test_quiz_title(self):
		quiz = self.db.get_quiz_title("Sample Quiz")
		self.assertEqual(type(quiz), Quiz)

if __name__ == "__main__":
    unittest.main()