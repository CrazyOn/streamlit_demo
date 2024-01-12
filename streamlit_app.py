import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Hello World!")
    st.write("Welcome to Streamlit!")
    # 创建一个 DataFrame
    data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

    # 创建一个折线图
    st.line_chart(data)

if __name__ == "__main__":
    main()
