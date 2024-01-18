import pyautogui
import limbus_company_function as limbus



pyautogui.click(100, 200) # 게임 화면 클릭

#limbus.continuous_scroll_down() # 스크롤 확대 이미지 크기 확대 -> Confidence 값 확보
def execute_macro(stage=1, priority=True): # 진행하는 층 수와 우선순의 매개변수를 이어받음
    limbus.boss=stage-1 # 현재 진행하는 층 수 전역변수에 저장

    while True : # 무한 반복
        if limbus.find_image_on_screen_position(limbus.current_position_img) : # 현재 플레이어의 위치를 찾고 좌표 결괏값 반환

            if priority: # 일반 전투 모드에서는 특수방부터 우선 검색
                if limbus.search_store() or limbus.search_rest() : # 상점방 탐색
                    print("특수방 발견")
                    continue
      

                elif limbus.search_Why() : # 우선 ???방 탐색
                    print("물음표 방 발견")
                    continue
                elif limbus.search_sento() : #일반 전투방 진입 시
                    print("전투방 발견")
                    limbus.while_sento()
                    continue
                elif limbus.search_sentto() or limbus.search_senttto() : # 하드 전투방과 환상체 전투방 진입 시
                    print("하드 전투방, 환상체 전투방 발견")
                    limbus.while_sento() # 전투시작
                    print("하드, 환상체 전투방 전투 진행중...")
                    if limbus.EGO_select() : # EGO gift 고를 수 있게 설계
                        print("EGO gift 선택 완료")
                        continue
            else : # 저 너머에 특수방이 존재한다면 전투방 먼저 우선순위 할당
                if limbus.search_sento():  # 일반 전투방 진입 시
                    print("전투방 발견")
                    limbus.while_sento()
                    continue
                elif limbus.search_sentto() or limbus.search_senttto():  # 하드 전투방과 환상체 전투방 진입 시
                    print("하드 전투방, 환상체 전투방 발견")
                    limbus.while_sento()  # 전투시작
                    print("하드, 환상체 전투방 전투 진행중...")
                    if limbus.EGO_select():  # EGO gift 고를 수 있게 설계
                        print("EGO gift 선택 완료")
                        continue
                elif limbus.search_store() or limbus.search_rest():  # 상점방 탐색
                    print("특수방 발견")
                    continue

                elif limbus.search_Why():  # 우선 ???방 탐색
                    print("물음표 방 발견")
                    continue
            if limbus.search_Boss() :# 그마저도 없으면 보스방 탐색
                print("보스방 진입")
                limbus.while_sento() # 전투시작
                print("전투 진행중...")
                limbus.EGO_select() # 보스방 전투 종료 후 EGO gift선택
                print("EGO gift 선택 완료")
                continue




