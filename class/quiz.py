class Quiz(object):
	"""

	"""

	def __init__(self, quiz_dict):
		"""
		initialize the a quiz dictionary which holds the
		all the quiz information
		"""
		self.quiz_dict = quiz_dict
		self.set_number_of_questions()

	def get_question(self, number):
		return self.quiz_dict["questions"][number]
	def get_all_questions(self):
		return self.quiz_dict["questions"]
	def get_title(self):
		return self.quiz_dict['title']
	def get_duration(self):
		return self.quiz_dict['duration']
	def get_tags(self):
		tags = self.quiz_dict['tags']
		tags = tags.split(",")
		stripped_tags = []
		for tag in tags:
			stripped_tags.append(tag.strip())
		return stripped_tags
	def get_id(self):
		return self.quiz_dict['id']
	def set_number_of_questions(self):
		questions = self.get_all_questions()
		self.number_of_questions = questions.__len__()

	def evaluate(self, answer_dict):
		# Assumes that answer to every question is provided
		score = 0
		wrong_questions = []
		for key in answer_dict:
			question = self.get_question(key)
			answer = answer_dict[key]
			if question.is_correct_answer(answer):
				score += 1
			else:
				wrong_questions.append(key)
		percentage = 100*float(score)/float(self.number_of_questions)
		return {"score": score, "percentage": percentage, "wrong": wrong_questions}
