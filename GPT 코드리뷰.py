import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    # 목적: 난수를 사용하여 2차원 데이터를 생성하고 반환합니다.
    # 이 함수를 통해 임의의 데이터로 실험 가능합니다.
    np.random.seed(0)
    return np.random.randn(100, 2)

def plot_descriptive_statistics(ax, data):
    # 목적: 주어진 데이터의 변수 1과 변수 2에 대한 평균과 중앙값을 막대 그래프로 시각화합니다.
    # 그래프는 각 변수에 대한 평균과 중앙값을 나란히 보여줍니다.
    a, b = data[:, 0], data[:, 1]
    ax.bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='변수 1')
    ax.bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='변수 2')
    ax.legend()
    ax.set_title('기술통계량: 평균 및 중앙값')

def plot_correlation_analysis(ax, data):
    # 목적: 주어진 데이터의 변수 1과 변수 2 간의 상관관계를 히트맵으로 시각화합니다.
    # 히트맵은 상관 계수를 표시하여 변수 간의 관계를 보여줍니다.
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=ax)
    ax.set_title('상관관계 분석')

def plot_histogram(ax, data):
    # 목적: 주어진 데이터의 변수 1과 변수 2에 대한 히스토그램을 그립니다.
    # 히스토그램은 각 변수의 분포를 시각적으로 확인할 수 있게 합니다.
    a, b = data[:, 0], data[:, 1]
    ax.hist(a, bins=15, color='blue', alpha=0.7, label='변수 1')
    ax.hist(b, bins=15, color='green', alpha=0.7, label='변수 2')
    ax.legend()
    ax.set_title('변수의 히스토그램')

def plot_scatter_plot(ax, data):
    # 목적: 주어진 데이터의 변수 1과 변수 2 간의 산점도를 그립니다.
    # 산점도는 두 변수 간의 관계를 시각적으로 확인할 수 있게 합니다.
    a, b = data[:, 0], data[:, 1]
    ax.scatter(a, b, alpha=0.7)
    ax.set_xlabel('변수 1')
    ax.set_ylabel('변수 2')
    ax.set_title('변수 1 대 변수 2의 산점도')

def main():
    # 목적: 위에서 정의한 함수들을 사용하여 데이터를 생성하고 다양한 통계적 시각화를 수행합니다.
    data = generate_data()
    
    # 2x2 서브플롯을 가진 플롯 생성
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 각 서브플롯에 대한 함수 호출
    plot_descriptive_statistics(axes[0, 0], data)
    plot_correlation_analysis(axes[0, 1], data)
    plot_histogram(axes[1, 0], data)
    plot_scatter_plot(axes[1, 1], data)

    # 레이아웃 조정 및 플롯 표시
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
