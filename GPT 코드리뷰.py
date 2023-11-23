import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data():
    # 난수 발생을 시드 고정하여 매번 동일한 데이터 생성
    np.random.seed(0)
    return np.random.randn(100, 2)

def plot_descriptive_statistics(ax, data):
    # 데이터에서 변수 1과 변수 2에 대한 평균과 중앙값을 막대 그래프로 표시
    a, b = data[:, 0], data[:, 1]
    ax.bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='변수 1')
    ax.bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='변수 2')
    ax.legend()
    ax.set_title('기술통계량: 평균 및 중앙값')

def plot_correlation_analysis(ax, data):
    # 데이터의 상관관계를 히트맵으로 시각화
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=ax)
    ax.set_title('상관관계 분석')

def plot_histogram(ax, data):
    # 변수 1과 변수 2의 히스토그램을 각각 그림
    a, b = data[:, 0], data[:, 1]
    ax.hist(a, bins=15, color='blue', alpha=0.7, label='변수 1')
    ax.hist(b, bins=15, color='green', alpha=0.7, label='변수 2')
    ax.legend()
    ax.set_title('변수의 히스토그램')

def plot_scatter_plot(ax, data):
    # 변수 1과 변수 2의 산점도를 그림
    a, b = data[:, 0], data[:, 1]
    ax.scatter(a, b, alpha=0.7)
    ax.set_xlabel('변수 1')
    ax.set_ylabel('변수 2')
    ax.set_title('변수 1 대 변수 2의 산점도')

def main():
    # 데이터 생성
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
