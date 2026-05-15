# 4. 서비스: 
import pandas as pd
import httpx

class ProductService:
    def __init__(self):([
        {'id':1, 'name':'콜라','price':1000},
        {'id':2, 'name':'사이다','price':1500}])

        # 7. 서비스 함수
    def products(self):
        return self.df.to_dict(orient='records')
    
    # 8. 외부 서버(API 또는 스프링) 와 통신하기
    # httpx.AsyncClient vs axios
    async def getSpring(self):
        async with httpx.AsyncClient() as client:
            response=await client.get("http://localhost:8080/api/product")
            print(response)
            return response.json() # 



productService=ProductService() # 서비스 객체 생성