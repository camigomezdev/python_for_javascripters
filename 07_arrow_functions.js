function factory (n) {
    return (a) => a * n;
}
const double = factory(2);
const triple = factory(3);

console.log(double(10))
// 20

console.log(triple(10))
// 30
