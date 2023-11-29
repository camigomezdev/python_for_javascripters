for (let x = 0; x < 6; x++) {
    console.log(x)
}
// 0,1,2,3,4,5

myArray = [1, 2, 3, 4]
for (value of myArray) {
    console.log(value)
}
// 1,2,3,4

myObj = {
    color: 'blue',
    fruit: 'apple',
    pet: 'dog'
}

for (key in myObj) {
    console.log(`${key} -> ${myObj[key]}`)
}
// color -> blue
// fruit -> apple
// pet -> dog