from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 放开所有跨域，先保证前端能请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 墨西哥比分接口
@app.get("/api/mexico")
def mexico_ecuador():
    return {"match":"墨西哥VS厄瓜多尔","score":["1-0","2-0","1-1"]}
