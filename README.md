# Quizzy A Console quiz Application

Quizzy is a quiz application, that allows you to take quizzes in the console. Quizzes can be imported from a json file and saved to the library. There is also an online reprositry for publishing quiz and also downloading a quiz to a local library.


### Version
0.0.1

### Json Format

This is a guide on creating quiz in Json

```sh
{
	"title": "Know Lagos",
	"category": "Travel",
	"tags": "Nigeria, general knowledge",
	"duration": 20,
	"questions": {
		"1": {
		"question" : "Where is Lagos located",
		"options" : ["England", "Benin", "USA", "Nigeria"],
		"answer" : 3
		},
		"2": {
		"question" : "What is the capital of Lagos",
		"options" : ["MaryLand", "Yaba", "Ikeja", "V/Island"],
		"answer" : 2
		},
		"3": {
		"question" : "Who is the Governor of Lagos",
		"options" : ["Raji Fasola", "Muhammed Buhari", "Ambode Akinwumi", "Abu Bello"],
		"answer" : 2
		},
		"4": {
		"question" : "Which of the following is not in Lagos",
		"options" : ["Tunga", "Yaba", "Ojota", "Ikorodu"],
		"answer" : 0
		},
		"5": {
		"question" : "The Yoruba name for Lagos is",
		"options" : ["Mushin", "Eko", "Oshodi", "Ojota"],
		"answer" : 1
		}
	}
}
```


## Usage

List all quiz Available in the library
```sh
$ listquizzes
```

Take the given quiz
```sh
$ takequiz <quiz_name>
```

Import quiz from json file
```sh
$ importquiz <path_to_json>
```
List quiz available online
```sh
$ onlinequizzes
```
Take online quiz
```sh
$ takeonline <quiz_name>
```
upload quiz to the online repro
```sh
$ uploadquiz <quiz_name>
```
