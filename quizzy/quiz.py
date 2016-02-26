from question import Question


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
		question_obj = Question(self.quiz_dict["questions"][number])
		return question_obj

	def get_all_questions(self):
		questions = self.quiz_dict["questions"]
		questions_obj = []
		for key in questions:
			question_obj = Question(questions[key])
			questions_obj.append(question_obj)
		return questions_obj

	def get_title(self):
		return self.quiz_dict['title']

	def get_duration(self):
		if self.in_quiz('duration'):
			return self.quiz_dict['duration']
		return False

	def get_category(self):
		return self.quiz_dict['category']

	def get_tags_list(self):
		tags = self.quiz_dict['tags']
		tags = tags.split(",")
		stripped_tags = []
		for tag in tags:
			stripped_tags.append(tag.strip())
		return stripped_tags

	def get_tags(self):
		return self.quiz_dict['tags']

	def in_quiz(self, index):
		if index in self.quiz_dict:
			return True
		else:
			return False

	def get_key(self):
		if self.in_quiz('key'):
			if self.quiz_dict['key'] != '':
				return self.quiz_dict['key']
		return False

	def get_difficulty(self):
		if self.in_quiz('difficulty'):
			return self.quiz_dict['difficulty']
		else:
			return False
	
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
		
	# def is_pass(self):
