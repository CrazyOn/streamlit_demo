import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Hello World!")
    st.write("Welcome to Streamlit!")
    # 创建一个 DataFrame
    data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

    # 创建一个折线图
    st.line_chart(data)

    slope1 = st.slider("斜率1 (Slope1):", -10.0, 10.0, 1.0)
    intercept1 = st.slider("截距1 (Intercept1):", -10.0, 10.0, 0.0)
    slope2 = st.slider("斜率2 (Slope2):", -10.0, 10.0, 1.0)
    intercept2 = st.slider("截距2 (Intercept2):", -10.0, 10.0, 0.0)
    slope3 = st.slider("斜率3 (Slope3):", -10.0, 10.0, 1.0)
    intercept3 = st.slider("截距3 (Intercept3):", -10.0, 10.0, 0.0)

    # 生成 x 值
    x_values = np.linspace(-10, 10, 100)
    # 计算对应的 y 值
    y_values1 = slope1 * x_values + intercept1
    y_values2 = slope2 * x_values + intercept2
    y_values3 = slope3 * x_values + intercept3

    # 创建坐标系
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values1, label=f'y1 = {slope1}x + {intercept1}')
    ax.plot(x_values, y_values2, label=f'y2 = {slope2}x + {intercept2}')
    ax.plot(x_values, y_values3, label=f'y3 = {slope3}x + {intercept3}')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    # 显示网格和坐标轴
    ax.grid(True)
    ax.legend()

    # 显示图形
    st.pyplot(fig)

if __name__ == "__main__":
    main()
