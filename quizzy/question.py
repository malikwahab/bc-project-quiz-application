class Question(object):

	def __init__(self, question_dict):
		self.question_dict = question_dict

	def is_correct_answer(self, answer):
		correct_answer_index = self.get_answer_index()
		correct_answer = self.get_answer_text()
		if answer.isnumeric():
			if correct_answer_index == int(answer):
				return True
		else:
			if correct_answer.lower() == answer.lower():
				return True
		return False

	def get_answer_index(self):
		return self.question_dict['answer']

	def get_answer_text(self):
		answer_index = self.get_answer_index()
		return self.question_dict['options'][answer_index]

	def get_options(self):
		return self.question_dict['options']

	def get_question(self):
		return self.question_dict['question']
