import urllib.request as req
import pandas as pd

df_total = pd.DataFrame()
page_num = 5988
while True:
    code = req.urlopen(f"https://www.2cpu.co.kr/sell?&page=5989&page={page_num}")
    df = pd.read_html(code)[0]
    df = df.iloc[::2, 1:]
    df.columns = ["제목", "글쓴이", "날짜", "조회", "추천"]
    df = df[(~df["제목"].str.contains("광고")) & (~df["제목"].str.contains("필독"))]
    if len(df) == 0:
        break
    df_total = df_total.append(df)
    page_num += 1
df_total.reset_index(drop=True, inplace=True)
df_total.to_excel("./2cpu 컴퓨터.xlsx", index=False)
