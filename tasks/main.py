from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import router as task_router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_router)

# uvicorn main:app --host 127.0.0.1 --port 9000 --reload

# if __name__ == '__main__':
#     uvicorn.run("main:app", host='127.0.0.1', port=9000, reload=True)
