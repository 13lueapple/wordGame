import pygame
import random

# 초기 설정
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Non-Overlapping Rectangles")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 직사각형 정보
rects = []
rect_width, rect_height = 50, 50
max_rects = 100  # 최대 생성할 직사각형 수

def create_non_overlapping_rect(existing_rects, max_attempts=100):
    """
    겹치지 않는 직사각형을 생성합니다.
    :param existing_rects: 기존 직사각형 리스트
    :param max_attempts: 위치를 찾기 위한 최대 시도 횟수
    :return: 새로운 직사각형(Rect 객체) 또는 None(실패 시)
    """
    for _ in range(max_attempts):
        x = random.randint(0, screen_width - rect_width)
        y = random.randint(0, screen_height - rect_height)
        new_rect = pygame.Rect(x, y, rect_width, rect_height)

        # 기존 직사각형과 겹치는지 확인
        if not any(new_rect.colliderect(existing_rect) for existing_rect in existing_rects):
            return new_rect
    return None  # 적합한 위치를 찾지 못한 경우

# 메인 루프
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 직사각형 생성
    if len(rects) < max_rects:
        new_rect = create_non_overlapping_rect(rects)
        if new_rect:
            rects.append(new_rect)

    # 직사각형 그리기
    for rect in rects:
        pygame.draw.rect(screen, BLUE, rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
