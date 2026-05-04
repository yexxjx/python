import pandas as pd

# [13] 판다스 병합, .merge(x, y, on="공통컬럼명",how="inner/outer/left/right")
df_info=pd.DataFrame({"Id" : [1,2,3], "Name" : ["Ant","Bee","Cat"]})
df_score=pd.DataFrame({"Id" : [2,3,4], "Score" : [88,92,85]})

# 두 판다스 간에 Id가 같은(교집합) 자료 병합
result=pd.merge(df_info,df_score,on="Id",how="inner")
print(result)

result=pd.merge(df_info, df_score,on="Id",how="left")
print(result)

# [14] 판다스 합치기, .concat([x,y],axis=0(행), 1(열),ignore_index=True/False)
result=pd.concat([df_info,df_score],axis=0,ignore_index=True)
print(result) # 세로연결

result=pd.concat([df_info,df_score],axis=1)
print(result) # 가로연결

new_score=pd.Series([85,90,88], name="Score") # 새로운 열
df_info["NewScore"]=new_score
print(df_info)

# [15] 정렬
# .sort_value(by="정렬기준", ascending=True(오름)/False(내림) )
# .sort_value(by=["1차정렬", '2차정렬], ascending=[1차정렬, 2차정렬  )
# .sort_index(axis=0(행)/1(열), ascending=True(오름)/False(내림) )
x=pd.DataFrame({
    "Name":["Ant","Bee","Cat","Dog"],
    "Age":[27,27,22,32],
    "Score":[88,95,85,90]
})
df=pd.DataFrame(x)
result=df.sort_values(by="Score",ascending=False) # 점수 기준 내림차순
print(result)

# 나이 기준 오름차순이므로 점수 기준으로 내림차순 즉) 나이 정렬 후 도일한 나이끼리 정수 내림차순
result=df.sort_values(by=["Age","Score"],ascending=[True, False])
print(result)

# 열이름(라벨) 내림순으로 정렬
result=df.sort_index(axis=1,ascending=False)
print(result)

# [16] 그룹, .groupby("그룹기준")["집계기준"].집계함수()
df=pd.DataFrame({
    "Category":["A","A","B","B","A","B"],
    "Type":["X","Y","X","Y","X","Y",],
    "Values":[10,20,30,40,50,60]
})

result=df.groupby("Category")["Values"].sum() # 카테고리 별 값 합계
print(result)

result=df.groupby("Type")["Values"].mean() # 타입 별 값 평균
print(result)

result=df.groupby(["Category","Type"])["Values"].sum() # 다중그룹
print(result)

result=df.groupby(["Category","Type"])["Values"].agg(["sum","mean","count"]) # 다중 집계
print(result)
