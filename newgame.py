import random
import pygame


pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름 

#FPS
clock = pygame.time.Clock()

#배경 이미지 삽입
background = pygame.image.load("C:\\Users\\이승현\\Desktop\\DO iT\\pygmae_basic\\park.png")

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\이승현\\Desktop\\DO iT\\pygmae_basic\\character2.png")
character_size = character.get_rect().size #이미지 크기 구함
character_width = character_size[0] # 가로크기
character_height = character_size[1] # 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 640-70을 빼면 캐릭터 위치


#이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 5

#똥 만들기
enemy = pygame.image.load("C:\\Users\\이승현\\Desktop\\DO iT\\pygmae_basic\\ddong.png")
enemy_size = enemy.get_rect().size #이미지 크기 구함
enemy_width = enemy_size[0] # 가로크기
enemy_height = enemy_size[1] # 세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) #enemy에 랜덤값 부여 
enemy_y_pos = 0
enemy_speed = 10



# 폰트 설정
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보 
start_ticks = pygame.time.get_ticks() #시작 틱을 받아옴


#이벤트 루프
running = True #게임이 진행중인가 확인함
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정 


    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창을 끄는 x버튼을 눌렀을때 이 구문이 실행됩니다. 
            running = False # 게임이 실행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로 이동
                to_x -= character_speed # to_x = to_x - 5랑 똑같음 
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로 이동
                to_x += character_speed
           
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춘다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
           

    character_x_pos += to_x 

    #가로 경계값 처리 캐릭터가 배경에서 벗어나지 않도록
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
     

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width) # 똥 위치 랜덤으로 나오도록



    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
       

    screen.blit(background, (0, 0)) #배경 그리기 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기 

    pygame.display.update() # 게임화면을 다시 그리기 pygame에서 필수 

pygame.time.delay(2000) # 2초대기
# pygame 종료
pygame.quit()