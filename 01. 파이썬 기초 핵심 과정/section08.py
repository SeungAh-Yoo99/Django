# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용2(클래스) #메모리를 많이 차지 하기 때문에 권장하지 않음.
from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex2 : ", fb.fib2(1600))
print("ex2 : ", fb().title)

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins # 기본으로 가지고 있기 때문에 명시적으로 import 해주지 않아도 된다.
p.prt1()
p.prt2()
print(dir(builtins))