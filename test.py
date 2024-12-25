import numpy as np
import matplotlib.pyplot as plt

class DifficultyAdjuster:
    def __init__(self, a, b, c, d):
        # 삼차함수 계수: f(x) = ax^3 + bx^2 + cx + d
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.previous_score = None

    def cubic_function(self, x):
        """삼차함수 f(x) 계산."""
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d

    def average_rate_of_change(self, x1, x2):
        """평균 변화율 계산."""
        if x1 == x2:
            return 0  # x1과 x2가 같으면 변화율이 0
        f_x1 = self.cubic_function(x1)
        f_x2 = self.cubic_function(x2)
        return (f_x2 - f_x1) / (x2 - x1)

    def adjust_difficulty(self, current_score):
        """현재 점수를 기반으로 난이도 조정."""
        if self.previous_score is None:
            # 초기 상태에서는 난이도를 기본값으로 설정
            self.previous_score = current_score
            return self.cubic_function(current_score)

        # 평균 변화율 계산
        rate_of_change = self.average_rate_of_change(self.previous_score, current_score)
        
        # 난이도 조정 값 업데이트
        difficulty = self.cubic_function(current_score) + rate_of_change

        # 상태 업데이트
        self.previous_score = current_score

        # 난이도 값 반환
        return max(1, difficulty)  # 난이도는 최소 1로 제한

# 난이도 조절기 초기화 (삼차함수 계수 설정)
adjuster = DifficultyAdjuster(a=0.01, b=-0.1, c=0.5, d=5)

# 예시 점수 데이터 (플레이어의 점수)
scores = [10, 15, 20, 25, 30, 35, 40]

difficulties = []
for score in scores:
    difficulty = adjuster.adjust_difficulty(score)
    difficulties.append(difficulty)
    print(f"Score: {score}, Adjusted Difficulty: {difficulty:.2f}")

# 결과 시각화
plt.plot(scores, difficulties, marker='o', label='Difficulty')
plt.xlabel('Score')
plt.ylabel('Difficulty')
plt.title('Real-time Difficulty Adjustment')
plt.legend()
plt.grid()
plt.show()
