import streamlit as st
import pandas as pd

st.title("Zaim集計アプリ")

uploaded_file = st.file_uploader("ファイルアップロード", type='csv')

# メイン画面

if uploaded_file is not None:
    # csv読み込み
    df = pd.read_csv(uploaded_file,encoding="cp932")
    # 必要な項目のみピックアップ
    pickupRow = df.loc[:,['日付','品目','メモ','支出','お店']]
    # メモ欄の空欄を50に置換
    pickupRow = pickupRow.fillna(50)

    partnerPayment = pickupRow['メモ']*pickupRow['支出']
    partnerPayment_sum = partnerPayment.sum() / 100
    st.header('相手の支払額')
    st.subheader(f'{partnerPayment_sum} 円')
    st.header('読み込みデータ表示')
    st.write(pickupRow)