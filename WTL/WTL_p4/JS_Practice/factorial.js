

function factorial1( num){
    fact = 1
    for(i=1;i<=num;i++){
        fact *= i
    }
    return fact
}
function factorial2(num){
    fact = 1
    while(num>0){
        fact *= num
        num -= 1
    }
    return fact
}

let num = prompt("enter the number ")
console.log(factorial1(num))
console.log(factorial2(num))

function iseven(num){
    if((num ^ 1) == (num + 1)){
       return true 
    }
    else{
        return false
    }
}

console.log(iseven(num))