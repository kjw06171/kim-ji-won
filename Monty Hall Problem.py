import random
import matplotlib.pyplot as plt

# 사용자로부터 반복 횟수 입력 받기
while True:
    try:
        trial = int(input("실험 횟수를 입력하세요 (예: 100000): "))
        if trial <= 0:
            print("0보다 큰 숫자를 입력하세요.")
            continue
        break
    except ValueError:
        print("숫자를 입력해주세요.")

# 결과를 저장할 변수 초기화
no_change = 0  # 선택을 바꾸지 않은 경우의 승리 횟수
change = 0     # 선택을 바꾼 경우의 승리 횟수

# 실험 수행
for _ in range(trial):
    # 자동차가 랜덤하게 배치된 문
    car = random.randint(0, 2)

    # 플레이어의 초기 선택
    player_choice = random.randint(0, 2)

    # 호스트가 열 수 있는 문을 선택 (자동차가 없고 플레이어가 선택하지 않은 문)
    empty_door = [i for i in range(3) if i != player_choice and i != car]
    host_opens = random.choice(empty_door)

    # 남아있는 문 계산 (플레이어가 선택하지 않았고 호스트가 열지 않은 문)
    remaining_door = [i for i in range(3) if i != player_choice and i != host_opens][0]

    # 선택을 바꾸지 않은 경우
    if player_choice == car:
        no_change += 1
    else:  # 선택을 바꾼 경우
        change += 1

# 결과 계산
no_change_prob = (no_change / trial) * 100
change_prob = (change / trial) * 100

# 결과를 시각적으로 표시
plt.bar(['Change', 'No Change'], [change_prob, no_change_prob], color=['blue', 'red'])
plt.title(f'Monty Hall Problem - Win Probability ({trial} trials)')
plt.ylabel('Winning Probability (%)')
plt.xlabel('Strategy')
plt.ylim(0, 100)
plt.show()
