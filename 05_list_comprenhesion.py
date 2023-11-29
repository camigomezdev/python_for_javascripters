languages = [
	"Java",
	"Javascript",
	"Python",
	"Rust",
	"Go"
]

new_list = [f"{language} 🍄"
            for language in languages
            if "J" in language]

print(new_list)
# ['Java 🍄', 'Javascript 🍄']