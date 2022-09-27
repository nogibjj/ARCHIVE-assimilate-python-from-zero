from mylib.logic import random_fruit
import fastapi

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/randofruit")
async def random_fruit_endpoint(count: int = 1):
    """Return a random fruit, forever"""

    if count < 100:
        return [next(random_fruit()) for i in range(count)]
    else:
        count = 100
        print(f"The maximum number of fruits is 100. You requested {count} fruits.")
        return [next(random_fruit()) for i in range(count)]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
