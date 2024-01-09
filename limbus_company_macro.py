import pyautogui
from PIL import Image
import time
import limbus_company_function as limbus



pyautogui.click(100, 200) # 게임 화면 클릭
#limbus.continuous_scroll_down() # 스크롤 확대 이미지 크기 확대 -> Confidence 값 확보

while True :
    if limbus.find_image_on_screen_position(limbus.current_position_img) : # 현재 플레이어의 위치를 찾고 좌표 결괏값 반환

        if limbus.search_store() or limbus.search_rest() : # 상점방 탐색
            print("특수방 발견")
            pass

        elif limbus.search_Why() : # 우선 ???방 탐색
            print("물음표 방 발견")

        elif limbus.search_sento() : #일반 전투방 진입 시
            print("전투방 발견")
            limbus.while_sento()
            print("일반 전투방 전투 진행중...")

        elif limbus.search_sentto() or limbus.search_senttto() : # 하드 전투방과 환상체 전투방 진입 시
            print("하드 전투방, 환상체 전투방 발견")
            limbus.while_sento() # 전투시작
            print("하드, 환상체 전투방 전투 진행중...")
            if limbus.EGO_select() : # EGO gift 고를 수 있게 설계
                print("EGO gift 선택 완료")
                pass

        elif limbus.search_Boss() :# 그마저도 없으면 보스방 탐색
            print("보스방 진입")
            limbus.while_sento() # 전투시작
            print("전투 진행중...")
            limbus.EGO_select() # 보스방 전투 종료 후 EGO gift선택
            print("EGO gift 선택 완료")





