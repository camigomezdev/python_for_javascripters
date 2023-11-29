languages = [
	"Java",
	"Javascript",
	"Python",
	"Rust",
	"Go"
]

new_list = filter(lambda language: "J" in language, languages)
new_list = map(lambda language: f"{language} 🍄", new_list)

print(list(new_list))
# ['Java 🍄', 'Javascript 🍄']