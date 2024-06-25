// Q1. 1부터 n까지의 합을 구하는 함수
function add_num(n){
    let sum=0
    for(let i=1; i<n+1; i++){
        sum+=i
    }
    return sum
}

console.log(add_num(10))