from IPython.display import set_matplotlib_formats, display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import mglearn

from mglearn import plot_helpers
from cycler import cycler

set_matplotlib_formats('pdf', 'png') #이미지는 무조건 pdf로 저장, 그래프는 투명배경 지원하는 png로 저장
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 300 #저장되는 이미지의 해상도 설정
plt.rcParams['figure.dpi'] = 100 #화면에 표시되는 그림의 해상도 설정
plt.rcParams['image.cmap'] = "viridis" #이미지의 색상맵 설정
plt.rcParams['image.interpolation'] = "none" #이미지의 보간 설정
plt.rcParams['savefig.bbox'] = "tight" #저장된 이미지의 주변 공백 설정
plt.rcParams['lines.linewidth'] = 2 #선의 너비 설정
plt.rcParams['legend.numpoints'] = 1 #범례의 마커 수 설정
#그래프의 선 색상 및 스타일을 순환하여 적용
plt.rc('axes', prop_cycle=( 
    cycler('color', plot_helpers.cm_cycle.colors) +
    cycler('linestyle', ['-', '-', '--',
                           (0,(3,3)), (0,(1.5,1.5))]))
    )
np.set_printoptions(precision=3, suppress=True) #NumPy의 출력 형식을 설정
pd.set_option('display.max_columns', 8) #pandas의 출력 형식을 설정
pd.set_option('display.precision', 2) #pandas의 출력 형식을 지정

#이 모듈을 다른 곳에서 import할 때, 이 목록에 있는 것들만 import됨
__all__ = ['np', 'mglearn', 'display', 'plt', 'pd']