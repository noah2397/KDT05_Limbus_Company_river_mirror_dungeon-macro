from PIL import Image
import pyautogui
import numpy as np
def search_image_in_region(image_paths, search_image_path, region):
    for image_path in image_paths:
        # 대상 이미지 열기
        main_image = Image.open(image_path)

        # 검색할 이미지 열기
        search_image = Image.open(search_image_path)

        # 대상 영역에서 이미지 검색
        region_pixels = main_image.crop(region)
        # 이미지를 넘파이 배열로 변환
        region_array = np.array(region_pixels)

        # 넘파이 배열을 리스트로 변환
        print(region_array)
        result = compare_images(region_pixels, search_image)

        # 검색 결과 출력
        if result:
            print("이미지를 찾았습니다.")
        else:
            print("이미지를 찾지 못했습니다.")

def compare_images(image1, image2):
    # 이미지 크기가 다르면 False 반환
    if image1.size != image2.size:
        return False

    # 픽셀 값 비교
    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            print(pixel1, pixel2)

            # 픽셀 값이 다르면 False 반환
            if pixel1 != pixel2:
                return False

    # 모든 픽셀 값이 일치하면 True 반환
    return True

# 테스트를 위한 이미지 파일 경로 및 검색할 영역 설정
main_image_paths = [(rf'.\current_position{i}.png') for i in range(2)]
search_image_path = r"sento0.png"
search_region = (100, 100, 2100, 1300)  # 검색할 영역의 좌표 (left, top, right, bottom)
pyautogui.click(100,100, interval=1)
pyautogui.click(2100,1300, interval=1)
pyautogui.click(127,48, interval=1)
pyautogui.click(141,53, interval=1)

# 검색 함수 호출
search_image_in_region(main_image_paths, search_image_path, search_region)
