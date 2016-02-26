import click
from quiz import Quiz
from question import Question
from database import QuizToDb
import json
import onlinequiz
import time


def list_online_quizzes():
	quizzes = onlinequiz.get_quizzes()
	for quiz in quizzes:
		click.echo(click.style(quiz, fg="magenta"))

def take_online_quiz(title):
	quiz = onlinequiz.get_quiz(title)
	if quiz:
		take_quiz(title)
	else:
		click.echo(click.style("Unable to download test", bg="red"))

def import_quiz(path_to_json):
	with open(path_to_json, "r") as json_data:
		string_quiz = json.load(json_data)

		quiz = Quiz(string_quiz)
		library = QuizToDb("testdb.db")
		library.save_quiz(quiz)

def list_quizzes():
	library = QuizToDb("testdb.db")
	quizzes = library.listquizzes()
	for quiz in quizzes:
		click.echo(click.style(quiz, fg="magenta"))

def review_test_session(quiz, session_info):
	answers = session_info['answers']
	for num in session_info['wrong']:
		question = quiz.get_question(num)
		correct_answer = question.get_answer_index()
		display_question(question, answers[num], correct_answer)


def present_question(question):
	options = question.get_options()
	display_question(question)
	answer = click.prompt(click.style(":", fg="green")).lower()
	for i in range(len(options)):
		if answer == "a" or answer == options[i].lower():
			answer_index = 0
		elif answer == "b" or answer == options[i].lower():
			answer_index = 1
		elif answer == "b" or answer == options[i].lower():
			answer_index = 2
		elif answer == "c" or answer == options[i].lower():
			answer_index = 3
		elif answer == "d" or answer == options[i].lower():
			answer_index = 4
		else:
			answer_index = -1
		return answer_index


def display_question(question, user_answer=False, correct_answer = False):
	text = question.get_question()
	options = question.get_options()
	option_style = ["A", "B", "C", "D", "E"]
	click.echo(click.style(text, fg="white"))
	for i in range(len(options)):
		if user_answer and correct_answer:
			if int(user_answer) == i:
				click.echo(click.style(option_style[i] +")"+options[i], bg="red"))
				continue
			elif int(correct_answer) == i:
				click.echo(click.style(option_style[i] +")"+options[i], bg="green"))
				continue
		click.echo(click.style(option_style[i] +")"+options[i], fg="white"))



def display(quiz):
	title = quiz.get_title()
	duration = quiz.get_duration()
	number_of_questions = quiz.number_of_questions
	click.echo(click.style(title, fg="red", bg="white"))
	click.echo(click.style("%d Questions" % number_of_questions, fg="cyan"))
	click.echo(click.style("You have %s minuutes for this quiz" % duration, fg="cyan"))
	quiz_time = time.time()+float(duration*60)
	questions = quiz.get_all_questions()
	answer_dict = {}
	for i in range(len(questions)):
		if time.time() < quiz_time:
			answer = present_question(questions[i])
			answer_dict.update({i+1:str(answer)})
		else:
			click.echo(click.style("Time Up!!", bg="red"))
			answer = -1
			answer_dict.update({i+1:str(answer)})
	return submit(quiz, answer_dict) 

def submit(quiz, answer_dict):
	evaluation = quiz.evaluate(answer_dict)
	return { "score": evaluation, "answers":answer_dict }


def take_quiz(quiz_title):
	library = QuizToDb("testdb.db")
	quiz = library.get_quiz_title(quiz_title)
	if type(quiz) == str:
		click.echo(click.style(quiz, bg="red"))
		return
	session = display(quiz)
	score = session["score"]
	answers = session["answers"]
	session_info = {'wrong':session['score']['wrong'], 'answers':answers}
	click.echo(click.style("You scored {}%".format(score["percentage"]), fg="cyan"))
	is_review = click.prompt(click.style("Enter r to review your test session, any other to continue".format(score["percentage"]), fg="cyan"))
	if is_review == "r":
		review_test_session(quiz, session_info)

def show_menu():
	menu = click.style("listquizzes", bg='green') + click.style("\t List all quiz avaliable in libary\n", fg="green")
	menu += click.style("importquiz", bg='green') + click.style("<path_to_quiz> \t to import a quiz into library from Json\n", fg="green")
	menu += click.style("takequiz", bg='green') + click.style("<quiz_name> \t to take a quiz\n", fg="green")
	menu += click.style("onlinequizzes", bg='green') + click.style("\t to list quiz online\n", fg="green")
	menu += click.style("takeonline", bg='green') + click.style("\t <quiz_name> to take quiz online\n", fg="green")
	menu += click.style("uploadquiz", bg='green') + click.style("<quiz_name> \t to upload a local quiz online \n", fg="green")
	menu += click.style("help", bg='green') + click.style("\tto get help\n", fg="green")
	menu += click.style("exit", bg='green') + click.style("\t to exit application\n", fg="green")
	return click.prompt(menu)
	#include option to save session, review  wrong question


@click.command()
def menu():
	click.echo(click.style("Welcome to Quizzy", fg='white', bg='red'))
	username = click.prompt(click.style("Enter Your Name:", fg='green'))
	click.echo(click.style("Welcome %s" % username, bg="cyan"))
	user_action = ['']
	
	while user_action[0] != "exit":
		user_action = show_menu().split()

		if user_action[0] == 'listquizzes':
			list_quizzes()
		elif user_action[0] == 'takequiz':
			try:
				quiz_title = user_action[1:]
				title = " ".join(quiz_title)
				take_quiz(title)
			except IndexError:
				click.echo(click.style("No title Given, Specify the title", bg="red"))
		elif user_action[0] == 'importquiz':
			try:
				import_quiz(user_action[1])
			except IndexError:
				click.echo(click.style("Path to file not specified", bg="red"))
		elif user_action[0] == 'onlinequizzes':
			try:
				list_online_quizzes()
			except:
				click.echo(click.style("An Error Occurred", bg="red"))
		elif user_action[0] == 'takeonline':
			try:
				quiz_title = user_action[1:]
				title = " ".join(quiz_title)
				take_online_quiz(title)
			except IndexError:
				click.echo(click.style("No title Given, Specify the title", bg="red"))
		elif user_action[0] == "uploadquiz":
			try:
				onlinequiz.upload_quiz(user_action[0])
			except IndexError:
				click.echo(click.style("No title Given, Specify the title", bg="red"))
		elif user_action[0] == "exit":
			break
		else:
			click.echo(click.style("Invalid Command", bg="red"))


if __name__ == '__main__':
    menu()