import unittest
from question import Question

class QuestionTest(unittest.TestCase):
	question_dict = {
		"question" : "How Hard is python",
		"options" : ["Very hard", "Not hard at all", "hard", "No comment"],
		"answer" : 2
	}

	question = Question(question_dict)

	def test_init(self):
		self.assertEqual(self.question_dict, self.question.question_dict)
	def test_get_question(self):
		self.assertEqual(self.question.get_question(), "How Hard is python")
	def test_get_options(self):
		self.assertEqual(self.question.get_options(), ["Very hard", "Not hard at all", "hard", "No comment"])
	def test_get_answer_text(self):
		self.assertEqual(self.question.get_answer_text(), "hard")
	def test_answer_answer_index(self):
		self.assertEqual(self.question.get_answer_index(), 2)
	def test_is_correct(self):
		self.assertTrue(self.question.is_correct_answer("2"))
	def test_is_correct2(self):
		self.assertFalse(self.question.is_correct_answer("1"))

if __name__ == "__main__":
    unittest.main()