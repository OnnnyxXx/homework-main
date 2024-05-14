import uvicorn
from fastapi import FastAPI
from router import router as task_router

app = FastAPI()

app.include_router(task_router)

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000, reload=True)
