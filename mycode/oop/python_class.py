class SoccerPlayer(object):
    # constructor - 객체가 생성될 때 호출되는 메서드 (생성자)
    def __init__(self, name, position, back_number=20):
        #attribute
        #print('생성자 함수 호출됨')
        self.name = name
        self.position = position
        self.back_number = back_number

    # method (action) - 등번호 속성을 변경하는 메서드
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number
    
    #객체 주소 대신 원하는 다른 속성 값을 반환해주는 메서드
    def __str__(self):
        #print('객체의 속성 값을 반환해주는 메서드')
        return "Hello, My name is %s. I play in %s in center. Back_Number is %d " % (self.name, self.position, self.back_number)

def main():
    # 객체 생성
    jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
    print(jinhyun)

    dooly = SoccerPlayer('둘리','GK') # __init__에서 back_number=20 (default) 설정되어 있기 때문에
    print(dooly)

    print("현재 선수의 등번호는 :", jinhyun.back_number)
    jinhyun.change_back_number(5)
    print("현재 선수의 등번호는 :", jinhyun.back_number)

# import가 아닌, 실행이 됐을 때만 main()함수가 실행됨
if __name__=="__main__":
    main()
