
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #한글 깨짐 방지
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Character:

  def __init__(self, speed):
    self.speed = speed


class Item:

  def __init__(self, item_type, speed_change):
    self.item_type = item_type
    self.speed_change = speed_change


class Player:

  def __init__(self, name):
    self.name = name # 플레이어의 이름 저장
    self.speed = 0 # 플레이어의 속도: 선택한 character의 속도!
    self.round_speed = 0 # 아이템 적용 후 플레이어의 속도
    self.play_records = [0]*5 # 플레이어의 경기 기록: 라운드별 주행 시간[초]


  def add_play_record(self, record_in_hr):
    """
    - 플레이어의 경기 기록을 받아 저장합니다.
    - 시간 단위로 들어온 기록을 초 단위의 기록으로 변환해 저장해야합니다. 
    - Game 클래스의 play_round() 함수에서 호출됩니다. 
    """
    # TODO : 플레이어의 경기 기록을 초 단위로 변환해 저장해주세요.
    for i in range(5):
        record_in_sec=record_in_hr*3600
        self.play_records[i]=record_in_sec


class Game:

  def __init__(self):
    self.num_rounds = 3
    self.player_list = [] # 플레이어의 목록. 이후에 set_players를 이용해 수정
    self.item_list = [] # 아이템의 목록. 이후에 set_item_list를 이용해 수정
    self.character_list = []
    self.item_speed = [0]*5 #아이템 적용한 속력
    self.records_sum = [0]*5

  def set_players(self):
    """
    - 5명의 플레이어를 생성하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """
    
    print("******************* 게임 접속 *******************")
    # TODO : 사용자로부터 플레이어의 이름을 입력받아 Player 객체를 생성하고 플레이어 목록(self.player_list)에 추가해주세요. 
    for i in range(5):
        self.name=input("Player"+str(i+1)+"의 이름을 입력해주세요: ")
        self.player_list.append(self.name)



  def start_game(self):
    """
    - 게임 규칙의 [게임 시작 전] 부분을 담당하는 함수입니다. 
    - 3 종류의 캐릭터와 2 종류의 아이템을 초기화하고, 사용자의 입력을 받아 각 플레이어의 속도를 설정합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """
    print("******************* 캐릭터 선택 *******************")
    # TODO (1): 범위 내의 속도를 가진 세 종류의 캐릭터를 생성해주세요. 
    for i in range(3): 
        self.character_list.append(random.randint(100, 180))


    # TODO (2): 사용자의 입력을 받아 플레이어의 고유 속도를 설정하고, 선택된 캐릭터의 속도를 출력해주세요. 
    for i in range(len(self.player_list)): 
        print(self.player_list[i]+"의 캐릭터 선택 차례입니다. 1, 2, 3중 하나의 값을 입력해주세요. ", end='')
        s=input()
        if s=='1':
            self.speed=self.character_list[0]
            print(self.player_list[i]+"의 고유 속도는 시속 "+str(self.speed)+"입니다.")
        elif s=='2':
            self.speed=self.character_list[1]
            print(self.player_list[i]+"의 고유 속도는 시속 "+str(self.speed)+"입니다.")
        elif s=='3':
            self.speed=self.character_list[2]
            print(self.player_list[i]+"의 고유 속도는 시속 "+str(self.speed)+"입니다.")
        else:
            print("잘못된 입력입니다. 1, 2, 3중 하나의 값만 선택해야 하는데 이번만 그냥 넘어갑니다~^~^")
        
    
    # TODO (3): 두 종류의 아이템을 생성해 아이템 목록(self.item_list)에 추가해주세요.
    self.item_list=['banana_slip', 'booster']


  def play_round(self):
    """
    - 게임 규칙의 [라운드 시작 전], [라운드 진행], [라운드 종료 후] 부분을 담당하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    #### [라운드 시작 전]
    # TODO (1) - 1: 트랙의 길이를 결정해 변수에 저장하고, 출력해주세요. 
    track=random.randint(5, 30)
    print("이번 라운드의 트랙 길이는 "+str(track)+"km입니다.")
    

    # TODO (1) - 2: 5명의 플레이어에게 아이템을 랜덤하게 적용시키고, 적용된 아이템과 적용 후 플레이어의 속도를 출력해주세요. 
    print("[아이템 적용]")
    P=Player("name")
    for i in range(len(self.player_list)):
        item=random.choice(self.item_list)
        self.item_speed[i]=P.round_speed+self.speed
        if item=='banana_slip':
            st=" 때문에 "
            st2="화이팅 ㅠㅠ"
        elif item=='booster':
            st=" 덕분에 "
            st2="화이팅 ~~"

        print("Player "+self.player_list[i]+"는 "+str(item), end='')
        if item=='banana_slip':
            print(st+"시속 ", end='')
            P.round_speed=random.randint(20, 40)
            print(str(self.item_speed[i]), end='')
        elif item=='booster':
            print(st+"시속 ", end='')
            P.round_speed=random.randint(30, 60)
            print(str(self.item_speed[i]), end='')
        print("로 이번 트랙을 질주합니다! ", end='')
        if item=='banana_slip':
            print(st2)
        elif item=='booster':
            print(st2)
        
    #### [라운드 진행] , [라운드 종료 후]
    # TODO (2) : 플레이어가 트랙을 도는 데 걸린 시간을 초 단위로 출력하고, 플레이어의 경기 기록에 추가해주세요. Player 클래스의 함수를 사용해야합니다.  
    print("[경기 진행중...]")
    print("[라운드 결과]")
    for i in range(len(self.player_list)):
        tmp=track/self.item_speed[i]
        P.add_play_record(tmp)
        self.records_sum[i]+=tmp*3600
        print("Player "+self.player_list[i]+"의 주행시간: "+str(tmp*3600))


  def game_result(self):
    """
    - 게임 규칙의 [게임 종료 후] 부분을 담당하는 함수입니다. 
    - 1, 2, 3순위까지 플레이어의 이름과 합산기록을 출력합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    - 파이썬의 sorted() 함수와 sort() 함수를 잘 이용하시면 편합니다. sorting key 등을 검색해보시기를 추천합니다. 
    """
    # TODO : 사용자를 합산 기록 순으로 정렬하고, 상위 3명의 경기 기록 합산을 출력합니다.
    records_dic={ name:value for name, value in zip(self.player_list, self.records_sum) }
    sorted_dict=dict(sorted(records_dic.items(), key=lambda x : x[1]))
    key_list=list(sorted_dict.keys())
    value_list=list(sorted_dict.values())
    
    for i in range(3):
        print(str(i+1)+"위: "+str(key_list[i]), end='')
        print("(총 주행 시간: "+str(value_list[i])+"초)")



  def game(self):
    """
    - 게임 운영을 위한 함수입니다. 
    - 별도의 코드 작성이 필요 없습니다. 
    """
    self.set_players()
    self.start_game()

    print("\n******************* 게임 시작 *******************")
    for i in range(3):
      print(f"============= ROUND {i+1} =============")
      self.play_round()
      print()
    print()

    print("******************* 명예의 전당 *******************")
    self.game_result()
    



if __name__ == '__main__':
  """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
  game = Game()
  game.game()