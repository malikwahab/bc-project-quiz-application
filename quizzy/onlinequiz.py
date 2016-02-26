from firebase import firebase
import json
from quiz import Quiz
from database import QuizToDb
import random
import string

firebase_app = firebase.FirebaseApplication("https://torrid-heat-3767.firebaseio.com", None)


#json_results = json.loads(results)

def get_quizzes():
	results = firebase_app.get("quizzes", None)
	titles = []
	for key in results:
		titles.append(results[key]['title'])
	return titles

def get_quiz(title):
	results = firebase_app.get("quizzes", None)
	for key in results:
		if results[key]['title'] == title:
			result = firebase_app.get("quizzes", key)
			if type(result) != type(None):
				result_dict = json_dict(result)
				quiz_obj = Quiz(result_dict)
				db = QuizToDb('testdb.db')
				try:
					db.save_quiz(quiz_obj)
				except sqlite3.IntegrityError:
					return False
				return True
	return False

def json_dict(json_obj):
	quiz_dict = {}
	quiz_dict['title'] = json_obj['title']
	quiz_dict['key'] = json_obj['key']
	quiz_dict['duration'] = json_obj['duration']
	quiz_dict['tags'] = json_obj['tags']
	quiz_dict['category'] = json_obj['category']
	quiz_dict['questions'] = {}
	i = 1
	
	for question in json_obj['questions']:
		if question == None:
			continue
		new_question = {}
		new_question['question'] = question['question']
		question['answer'] = question['answer']
		options = []
		for key in question['options']:
			options.append(question['options'][key])
		question['options'] = options
		quiz_dict['questions'].update({i: question})
		i+=1
	return quiz_dict

def key_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join([random.choice(chars) for i in range(size)])

def upload_quiz(title):
	db = QuizToDb('testdb.db')
	quiz_dict = db.get_quiz_title_dict(title)
	if quiz_dict:
		quiz_dict['key'] = key_generator()
		post_result = firebase_app.post('quizzes', data=quiz_dict)
		return post_result
	return False