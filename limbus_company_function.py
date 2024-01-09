import pyautogui
from PIL import Image
import time
#=======================================================================================
#                                      변수
#=======================================================================================
#pyautogui.FAILSAFE=False
boss=0 # 현재 돌고 있는 던전 층 수
x,y=0,0 # 탐색을 시도할 pixel 영역 지정 변수


#=======================================================================================
#                                 이미지 파악 전용 함수
#=======================================================================================
# def find_image_on_screen_position
# def find_image_on_screen
# def continuous_scroll_down
# def drag

#현재 플레이어 위치 좌표 반환 함수(초기값 전용 함수)
def find_image_on_screen_position(image_paths):
    for image_path in image_paths:
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Error: 파일 '{image_path}'을 찾을 수 없습니다.")
            return
        except Exception as e:
            print(f"Error: 이미지를 열 때 오류 발생 - {e}")
            return

        try:
            location = pyautogui.locateOnScreen(image, confidence=0.8)
            if location is not None:
                print(f"이미지가 발견된 좌표: {location[0]}, {location[1]}")
                global x,y
                x,y=location[0],location[1]
                print("플레이어 위치 확인 완료")
                return True
            else:
                print("이미지를 찾을 수 없습니다.")
        except Exception as e:
            pass
            #print(f"Error: 이미지를 찾는 도중 오류 발생 - {e}")


# 이미지 인식 프로그램(전용)
def find_image_on_screen(image_paths, set_cordination=True):
    """
    화면에서 이미지를 찾고 해당 좌표를 출력하는 함수
    :param image_path: 찾을 이미지 파일의 경로
    """
    for image_path in image_paths:
        try:
            # 이미지 파일을 열어서 PIL Image 객체로 변환
            image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Error: 파일 '{image_path}'을 찾을 수 없습니다.")
            return
        except Exception as e:
            print(f"Error: 이미지를 열 때 오류 발생 - {e}")
            return

        # 이미지를 화면에서 찾기
        try:
            # 좌표 기준으로 오른쪽 1000픽셀, 위아래 400픽셀 범위 설정
            # 1층, 3층의 경우 오른쪽으로 진행, 2층, 4층의 경우 왼쪽으로 진행함을 고려
            if set_cordination: # 만약 현재 플레이어의 위치를 찾고 주변 탐색만 한다면 범위를 잡고 아래 코드 실행
                region_left = (x if not boss%2 else x-800 if not x-800 < 0 else 0)
                region_top = (y - 500 if y-500>0 else 0)
                region_right = (x + 1000 if not boss%2 else x)
                region_bottom = (y + 500 if y+500 > 1440 else 1440)
                #pyautogui.moveTo(region_left, region_top)
                #time.sleep(2)
                #pyautogui.moveTo(region_right, region_bottom)
                #time.sleep(2)
                #print(f"{region_left}, {region_top},{region_right},{region_bottom}에서 이미지 탐색")
                location = pyautogui.locateOnScreen(image, confidence=0.8,region=(region_left, region_top, region_right, region_bottom))
            elif set_cordination==False : # 좌표 지정이 꺼져 있다면 무시하고 전체화면에서 이미지 검색
                location = pyautogui.locateOnScreen(image, confidence=0.8)
            if location is not None:
                #print(f"이미지가 발견된 좌표: {location[0]}, {location[1]}")
                pyautogui.moveTo(location[0], location[1])
                pyautogui.click(location[0], location[1], interval=1)
                return True
            else:
                print("이미지를 찾을 수 없습니다.")
        except Exception as e:
            pass
            #print(f"Error: 이미지를 찾는 도중 오류 발생 - {e}")

def continuous_scroll_down(wheel_count=10,flag=1): # 마우스 휠을 사용하여 확대
    """
    연속적으로 마우스 휠을 아래로 스크롤하는 함수
    :param wheel_count: 휠을 얼마나 연속해서 돌릴지 설정 (기본값: 3)
    """
    for _ in range(wheel_count):
        pyautogui.scroll(1*flag)  # -1은 아래로 스크롤을 나타냄

def drag(): # 화면을 끌어잡고 왼쪽/오른쪽으로 끌기
    # 시작 지점 좌표
    start_x, start_y = 1000, 1000
    # 드래그할 거리
    drag_distance = -200
    # 드래그 액션 수행
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()  # 마우스 버튼을 누른 상태로 유지
    # 드래그를 위한 대기 시간 (선택적)
    time.sleep(1)
    # 드래그할 거리만큼 이동
    pyautogui.moveRel(drag_distance, 0, duration=0.1)  # (x, y) 방향으로 이동
    # 드래그 액션 종료
    pyautogui.mouseUp()


#=======================================================================================
#                                 이미지 에셋
#=======================================================================================

#================================= 맵 진행 방 ===========================================
#현재 위치(빨간 기차)
current_position_img=[(rf'.\current_position{i}.png') for i in range(7)]

#일반 전투방
#sento_img=[r'.\sento.png',r'.\sento1.png',r'.\sento2.png',r'.\sento3.png',r'.\sento4.png',r'.\sento5.png',r'.\sento6.png', ...... 너무 많아진다]
sento_img=[(rf'.\sento{i}.png') for i in range(17)] # list_comprehention적용

#하드 전투방
sentto_img=[(rf'.\sentto{i}.png') for i in range(5)]

#환상체 전투방
senttto_img=[(rf'.\senttto{i}.png') for i in range(6)]

# ???방 이미지
why_img=[(rf'.\why{i}.png') for i in range(12)]

# 보스방
boss_img=[(rf'.\boss{i}.png') for i in range(8)]

#상점방
store_img=[(rf'.\store{i}.png') for i in range(6)]

#휴식방
rest_img=[(rf'.\rest{i}.png') for i in range(6)]
#=========================================================================================

#================================= 버튼 이미지 에셋 =========================================
# 승률 버튼 이미지
kachi_img=[r'.\kachi.png']

# 전투 시작 버튼 이미지
start_img=[r'.\start.png']

# 전투방 입장 버튼 이미지
nyujyo_img=[(rf'.\nyujyo{i}.png') for i in range(2)]

# 전투방 입장 -> 시작 이미지
sentoStart_img=[(rf'.\sento_start{i}.png') for i in range(2)]

# 승리 판별 이미지
victory_img=[r'.\victory.png']

# skip버튼 이미지
skip_img=[r'.\skip.png']

# Boss 전투 후 EGO 선택 이미지
ego_select_img=[(rf'.\ego_select{i}.png') for i in range(2)]

# Boss 전투 후 EGO 선택->확정 이미지
ego_select_kakutei=[r'.\ego_select_kakutei.png']

# Boss 전투 후 EGO 선택-> 확정 -> 확인 이미지
ego_select_kakunin=[r'.\ego_select_kakunin.png']

# ??? 방 완료 후 돌아가기 버튼
why_return=[r'.\why_return.png']

#나가기 전 OK버튼
store_ok_img=[r'.\store_ok.png']
#=================================== 미 완성 에셋 =========================================
#파열 텍스트 이미지
pa_img=[f'.\pa.png']



#=======================================================================================
#                               이미지 인식 시퀸스 함수
#=======================================================================================
#================================== 기본 전투 ============================================
def sento() :
    if find_image_on_screen(kachi_img,set_cordination=False): # 전투 "승률"버튼 클릭
        print("승률 버튼 클릭")
        find_image_on_screen(start_img,set_cordination=False)  # 전투 시작(시계) 버튼 클릭
        print("전투 시작")

def while_sento():
    time.sleep(7)  # 전투방 입장 후 로딩 텀 부여
    print("7초 휴식")
    continuous_scroll_down()  # 스크롤 확대
    print("스크롤 확대 완료")
    while not find_image_on_screen(victory_img,set_cordination=False):  # 승리 화면이 나타나기 전까지
        print("전투중.....")
        sento()  # 계속 "승률"-"시작" 반복
    print("전투 승리 후 7초 대기")
    time.sleep(7)  # 승리 후 로딩 텀 부여
#==================================== 에고 선택 함수 =======================================
# 보스 처치 후 EGO 선택 화면
def EGO_select():
    if find_image_on_screen(ego_select_img,set_cordination=False):  # 보스 처치 후 EGO선택 화면
        print("EGO 선택 화면 진입")
        find_image_on_screen(ego_select_kakutei,set_cordination=False)  # EGO선택 후 "EGO기프트 선택"클릭
        time.sleep(5)
        print("EGO 선택 완료 및 대기 5초")
        find_image_on_screen(ego_select_kakunin,set_cordination=False)  # 다음 스테이지로 이동 후 "확인" 클릭
        print("최종 확인 클릭")
        boss=0
#==================================== 탐색 함수 ===========================================
def search_store() :
    if find_image_on_screen(store_img):
        print("상점 발견")
        find_image_on_screen(nyujyo_img, set_cordination=False)
        print("상점 입장")
        while True :
            print("상점 구매 확정 대기중....")
            if find_image_on_screen(store_ok_img,set_cordination=False) :
                break
        continuous_scroll_down(wheel_count=5, flag=-1)
        return True

# 휴식방 탐색 후 입장
def search_rest() :
    if find_image_on_screen(rest_img):
        print("휴식처 발견")
        find_image_on_screen(nyujyo_img, set_cordination=False)
        print("휴식처 입장")
        while True :
            print("휴식처 최종 선택 대기중....")
            if find_image_on_screen(store_ok_img,set_cordination=False) :
                break
        continuous_scroll_down(wheel_count=5, flag=-1)
        return True

# 일반 전투방 탐색 후 입장
def search_sento():
    if find_image_on_screen(sento_img): # 전투 아이콘 클릭(검 1개짜리)
        print("전투방 발견")
        time.sleep(1)
        print("전투방 발견 후 대기")
        if find_image_on_screen(nyujyo_img, set_cordination=False): # "입장" 버튼 클릭
            print("입장 버튼 클릭")
            find_image_on_screen(sentoStart_img,set_cordination=False)  # "전투 시작" 딸깍
            print("전투시작 버튼 클릭")
            return True

# 하드 전투방 탐색 후 입장
def search_sentto():
    if find_image_on_screen(sentto_img): # 하드 전투 아이콘 클릭(검 2개짜리)
        print("하드 전투방 발견")
        time.sleep(1)
        print("하드 전투방 발견 후 대기")
        if find_image_on_screen(nyujyo_img, set_cordination=False): # "입장" 버튼 클릭
            print("입장 버튼 클릭")
            find_image_on_screen(sentoStart_img,set_cordination=False)  # "전투 시작" 딸깍
            print("전투시작 버튼 클릭")
            return True

# 환상체 전투방 탐색 후 입장
def search_senttto():
    if find_image_on_screen(senttto_img): # 환상체 전투방 아이콘 클릭
        print("환상체 전투방 발견")
        time.sleep(1)
        print("환상체 전투방 발견 후 대기")
        if find_image_on_screen(nyujyo_img, set_cordination=False): # "입장" 버튼 클릭
            print("입장 버튼 클릭")
            find_image_on_screen(sentoStart_img,set_cordination=False)  # "전투 시작" 딸깍
            print("전투시작 버튼 클릭")
            return True

# 보스방 탐색 후 입장
def search_Boss():
    global boss
    if find_image_on_screen(boss_img, set_cordination=False): # 보스 방 클릭
        print("보스방 발견")
        time.sleep(1)
        print("보스방 발견 후 대기")
        time.sleep(1)
        while True:
            print("입장 버튼 탐색")
            if find_image_on_screen(nyujyo_img, set_cordination=False) : # "입장" 버튼 클릭
                print("입장 버튼 클릭")
                find_image_on_screen(sentoStart_img,set_cordination=False)  # "전투 시작" 딸깍
                print("전투시작 버튼 클릭")
                boss += 1
                break
        return True

# ???방 탐색 후 입장
def search_Why():
    if find_image_on_screen(why_img) :  # 물음표 방 탐색
        print("물음표 방 탐색")
        if find_image_on_screen(nyujyo_img, set_cordination=False) : # 입장 클릭
            print("물음표 방 진입 완료")
            find_image_on_screen(skip_img,set_cordination=False) # 스킵 클릭 -> 유저가 클릭 유도
            print("skip 버튼 클릭 완료")
            while True :
                print("EGO 선택지 결정 대기중....")
                if find_image_on_screen(why_return,set_cordination=False) :
                    break
            time.sleep(3)
            find_image_on_screen(ego_select_kakunin, set_cordination=False)  # 다음 스테이지로 이동 후 "확인" 클릭
            print("최종 확인 클릭")
            continuous_scroll_down(wheel_count=5, flag=-1)


