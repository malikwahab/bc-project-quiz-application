import unittest
from quiz import Quiz
from question import Question

class QuizTest(unittest.TestCase):
	quiz_dict = {
		"title": "Quiz from Json",
		"category": "Programming",
		"tags": "Computer, Network",
		"duration": 20,
		"questions": {
			"1": {
			"question" : "How Hard is python",
			"options" : ["Very hard", "Not hard at all", "hard", "No comment"],
			"answer" : 2
			},
			"2": {
			"question" : "What is vvvhdvcb",
			"options" : ["hakjks", "eyewfanf", "kdknf fskc", "dhakb  cfdscb"],
			"answer" : 1
			},
			"3": {
			"question" : "jkjgfn cnkjnefn dcvnfo vaiofnv",
			"options" : ["hfhoiwjf sfnoi", "haae fn", "cway", "milk"],
			"answer" : 0
			},
			"4": {
			"question" : "what is SQLite3",
			"options" : ["Ruby Library", "Java Module", "Python Library", "Library"],
			"answer" : 3
			},
			"5": {
			"question" : "Who is the president of Nigeria?",
			"options" : ["Muhammed Buhari", "Goodluck Jonathan", "Olusegun Obasanjo", "Raji Fasola"],
			"answer" : 0
			}
		}
	}
	quiz = Quiz(quiz_dict)

	def test_initialization(self):
		self.assertEqual(self.quiz_dict, self.quiz.quiz_dict)
	def test_initializtion2(self):
		self.assertEqual(self.quiz.number_of_questions, 5)
	def test_get_question(self):
		question = self.quiz.get_question("1")
		self.assertEqual(question.get_question(), "How Hard is python")
	def test_get_question_all(self):
		questions = self.quiz.get_all_questions()
		self.assertEqual(len(questions), 5)
	def test_get_question_all2(self):
		questions = self.quiz.get_all_questions()
		question = questions[0]
		self.assertEqual(type(question), Question)
	def test_get_title(self):
		title = self.quiz.get_title()
		self.assertEqual(title, "Quiz from Json")
	def test_get_duration(self):
		duration = self.quiz.get_duration()
		self.assertEqual(duration, 20)
	def test_get_category(self):
		self.assertEqual("Programming", self.quiz.get_category())
	def test_in_quiz(self):
		self.assertTrue(self.quiz.in_quiz("title"))
	def test_in_quiz2(self):
		self.assertFalse(self.quiz.in_quiz("key"))
	def test_get_key(self):
		self.assertFalse(self.quiz.get_key())
	def test_get_difficulty(self):
		self.assertFalse(self.quiz.get_difficulty())
	def test_evaluate(self):
		answer_dict = {"1":"0", "2":"1", "3":"1", "4":"2", "5":"0"}
		score = self.quiz.evaluate(answer_dict)
		expect_score = {"score":2, "wrong":[1,3,4], "percentage":40.0}
		self.assertEqual(score["score"], expect_score["score"])

if __name__ == "__main__":
    unittest.main()