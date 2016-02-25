import sqlite3
from quiz import Quiz

class QuizToDb(object):


	def __init__(self, db):
		self.db = sqlite3.connect(db)
		self.cursor = self.db.cursor()
		try:
			self.db.execute(
				''' CREATE TABLE IF NOT EXISTS questions(
					id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
					question TEXT NOT NULL,
					options TEXT NOT NULL,
					answer CHAR(2) NOT NULL,
					quiz_id INTEGER NOT NULL
					);
				''')

			self.db.execute(
				''' CREATE TABLE IF NOT EXISTS quiz(
					id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
					key TEXT UNIQUE,
					title TEXT UNIQUE NOT NULL,
					tags TEXT NOT NULL,
					category TEXT NOT NULL,
					duration TEXT NOT NULL,
					difficulty TEXT
					);
				''')
			self.db.execute(
				'''CREATE TABLE IF NOT EXISTS test_session(
					id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
					quiz_id INTEGER NOT NULL,
					is_compelete INT NOT NULL,
					question_on INT,
					answers TEXT NULL,
					date_created TEXT NOT NULL,
					is_locked INT NOT NULL
					);
				''')
		except sqlite3.OperationalError as e:
			print(e)

	def save_question(self, question, quiz_id):
		question_text = question.get_question()
		options_list = question.get_options()
		options = ''
		for i in range(len(options_list)-2):
			options += options_list[i]+'|'
		answer = question.get_answer_index()
		self.cursor.execute("INSERT INTO questions(question, options, answer, quiz_id) VALUES(?, ?, ?, ?)", (question_text, options, answer, quiz_id))

	def save_quiz(self, quiz):
		key = ''
		duration = ''
		difficulty = ''
		if quiz.in_quiz('key'):
			key = quiz.get_key()
		title = quiz.get_title()
		tags = quiz.get_tags()
		category = quiz.get_category()
		if quiz.in_quiz('duration'):
			duration = quiz.get_duration()
		if quiz.in_quiz('difficulty'):
			difficulty = quiz.get_difficulty()
		try:
			if not key or key == '':
				return "Keys specifeid but given no Value"
			else:
				self.cursor.execute("INSERT INTO quiz(key, title, tags, category, duration, difficulty) VALUES(?, ?, ?, ?, ?, ?)", (key,  title, tags, category, duration, difficulty))
		except sqlite3.IntegrityError as e:
			raise(e)
			return "Quiz With the same name or key already Exist in the database"+"\n"
		quiz_id = self.cursor.lastrowid
		for question in quiz.get_all_questions():
			self.save_question(question, quiz_id)
		self.db.commit()
	
	def listquizzes(self):
		results = self.cursor.execute("SELECT title FROM quiz")
		rows = results.fetchall()
		quizzes = []
		for row in rows:
			quizzes.append(row[0])
		return quizzes


	def get_quiz(self, id):
		results = self.cursor.execute("SELECT * FROM quiz WHERE id = {}".format(id))
		rows = results.fetchall()
		if len(rows) < 1:
			return "No Quiz with the specified ID"
		return self.get_quiz_dict(rows[0])

	def get_all_quiz(self):
		results = self.cursor.execute("SELECT * FROM quiz")
		rows = results.fetchall()
		return rows

	def get_quiz_title(self, title):
		results = self.cursor.execute("SELECT * FROM quiz WHERE title = '{}'".format(title))
		rows = results.fetchall()
		if len(rows) < 1:
			return "No Quiz with the specified Title"
		return self.get_quiz_dict(rows[0])
	def get_quiz_property(self, quiz_property, data):
		results = self.cursor.execute("SELECT * FROM quiz WHERE {} = {}".format(quiz_property, data))
		if len(rows) < 1:
			return False
		return self.get_quiz_dict(rows[0])
	def get_quiz_dict(self, quiz_db_data):
		quiz = {}
		quiz_id = quiz_db_data[0]
		key = quiz_db_data[1]
		title = quiz_db_data[2]
		tag = quiz_db_data[3]
		category = quiz_db_data[4]
		duration = quiz_db_data[5]
		difficulty = quiz_db_data[6]

		if key != '0':
			quiz['key'] = key
		quiz['title'] = title
		quiz['tag'] = tag
		quiz['category'] = category
		quiz['duration'] = duration
		quiz['difficulty'] = difficulty
		
		question_results = self.cursor.execute("SELECT * FROM questions WHERE quiz_id = {}".format(quiz_id))
		questions = question_results.fetchall()
		quiz['questions'] = {}

		for i in range(len(questions)):
			num = i+1
			question = {}
			question['question'] = questions[i][1]
			question['options'] = questions[i][2].split("|")
			question['answer'] = questions[i][3]
			quiz['questions'].update({num: question})
		return Quiz(quiz)
