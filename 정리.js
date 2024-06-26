/*
Console
- console.log() : console창 확인
- console창에서 직접 쳤을 때 띄어쓰기 할 때 Shift + Enter

# 변수 선언
let num = 10   // 변수를 선언할 때는 앞에 let을 쓴다.
console.log(num)
let num
num // 아직 값이 정의되지 않았기 때문에 undefined라고 뜬다.
num = 2
num => 2출력

** 변수 선언시 주의 사항 **
변수 이름은 원하는 대로 지을 수 있지만, 아무렇게나 지으면 코드를 이해하기 어려워집니다. 
특히 다른 개발자들과 협업을 하기 위해서는 프로그래밍 언어와 회사에 따라 정해진 '네이밍 컨벤션(Naming convention)'을 따라야 합니다. 
소문자로 쓰고 밑줄(underscore, _)로 잇는 snake case(first_name)와 
뒤에 오는 단어의 첫글자를 대문자로 쓰는 camel case(firstName)를 많이 쓰는 편입니다. 
대부분의 프로그래밍 언어에서 _ 외의 특수문자는 변수명에 포함할 수 없어요.


# 자료형(data type)과 기본 연산
- 숫자형
    - +,-,*,/,% 
    - ++, --, +=
- 문자열
    - "ㅇㅇㅇ"
    - 'ㅇㅇㅇ'

# 불(Boolean) 자료형
- True, False
- && , || , ==, !=, !

# 함수
function 함수이름(필요한 변수들) {
	  내릴 명령들을 순차적으로 작성
}

함수이름(필요한 변수들) // 사용하기

# 조건문
if (조건) {
    조건을 만족할 때 실행할 것
}

// 또는,
if (조건) {
    조건 만족 시 실행
} else {
    조건 불만족 시 실행
}


# 반복문
for (1. 시작조건; 2. 반복조건; 4. 더하기) {
	3. 조건을 만족할 때 실행
}


*/

// JavaScript 기능
let 변수='star'
변수.toUpperCase() // 알파벳 모두 대문자로 "STAR"
let txt = '서울시-마포구-망원동'
let names = txt.split('-'); // ['서울시','마포구','망원동']
let result = names.join('>'); // '서울시>마포구>망원동'


let b_list = [1,2,'hey',3] // 로 선언 가능. 

// 리스트에 요소 넣기
b_list.push('헤이')
b_list                     // [1, 2, 'hey', 3, "헤이"] 를 출력

// 리스트의 길이 구하기
b_list.length              // 5를 출력

let a_list = [1, 4, 2, [3, 1]]
// 리스트와 리스트를 이어붙이고 싶다면
let c_list = a_list.concat(b_list)
c_list              // [1, 4, 2, [3, 1], 1, 2, 'hey', 3, "헤이"]
console.log(c_list)

//딕셔너리 
let b_dict = {'name':'Bob','age':21} 


//jQuery
document.getElementById("element").style.display = "none"; // $('#element').hide();와 같음
