let languages = [
	"Java",
	"Javascript",
	"Python",
	"Rust",
	"Go"
]

let new_list = languages
	.filter(language => language.includes("J"))
	.map(language => `${language} 🍄`)

console.log(new_list)
// ['Java 🍄', 'Javascript 🍄']