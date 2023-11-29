let n_cats = 10

if (n_cats < 3) {
    console.log("So sad")
}
else if (n_cats >= 3 && n_cats <= 5) {
    console.log("Nice!")
}
else {
    console.log("You are a lucky person!")
}

// You are a lucky person!

let n_cats = 3
let message = n_cats >= 3 ? "Nice!" : "So sad"
console.log(message)
// Nice!
