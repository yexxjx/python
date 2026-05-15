# 3. 라우터: 웹(서버) 와 연결되는 라우터
from fastapi import APIRouter
router=APIRouter(prefix='/api')

# 4. 서비스 객체 호출
from service import productService

# 4. HTTP 매핑
@router.get("/products")
async def products():
    return productService.products()

@router.get("/spring")
async def getSpring() :
    return await productService.getSpring()