# 키워드 파라미터
def connect(server, port):
    url=f'http://{server}:{port}'
    return url

print(connect('localhost','8080'))
print(connect(port='80',server='aa.com'))
print(connect('naver.com',port='8090'))

# Argument Default Value (java만 불가)
def add(a=10, b=20):
    return a + b

def minus(a=10, b=30):
    return a-b

x=add()
y=add(5)

print(x)
print(y)
print(minus(100))

# var_parameter (가변 파라미터) -tuple 타입
def kwargs_test(a,b,*p):
    print(type(p))
    print(a,b,p)
    return a+b+sum(p) #세 번째 파라미터에는 여러 개의 param 올 수 있음

print(kwargs_test(10,20)) #p=0
print(kwargs_test(10,20,30,40)) #p=(30,40)

# var_parameter (가변 파라미터) -dict 타입
def kwargs_dict(**p):
    print(p,type(p))
    for k,v in p.items():
        print(k,v)

kwargs_dict(a=100,b=300,c=400)

# return - 값을 여러 개 반환 (tuple 타입)
def swap(a,b):
    return b,a

result = swap(10,20)
print(result, type(result))

x,y = swap(10, 20)
print(f'X={x}, Y={y}')





