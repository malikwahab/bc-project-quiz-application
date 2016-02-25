from firebase import firebase
import json
from quiz import Quiz

firebase_app = firebase.FirebaseApplication("https://torrid-heat-3767.firebaseio.com", None)


#json_results = json.loads(results)

def get_quizzes():
	results = firebase_app.get("quizzes", None)
	titles = []
	for key in results:
		titles.append(key)
	return titles

def get_quiz(title):
	result = firebase_app.get("quizzes", title)
	if type(result) != type(None):
		result_dict = json_dict(result)
		return Quiz(result_dict)
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
		options = ''
		for key in question['options']:
			options += question['options'][key]
		question['options'] = options
		quiz_dict['questions'].update({i: question})
		i+=1
	return quiz_dict