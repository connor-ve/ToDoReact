from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

backlog = [
  "cut grass", "get milk", "pay taxes"
]

current = [
  "drinking milk", "pooping", "crying"
]

urgent = [
  "wiping", "farting", "remove arrow"
]

completed = [
  "murdered cat", "escaped to gana"
]

# THIS IS BECAUSE OF CORS because we are on the same host but a different port
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/tasks/{lvl}")
def tasks(lvl):
  match lvl:
    case "backlog":
      return backlog
    case "current":
      return current
    case "urgent":
      return urgent
    case "completed":
      return completed
    case _:
      return {"unknown": "unknown"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)