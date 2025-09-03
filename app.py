from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def get_api():
    return "product marking!

@app.get("/health", response_class=PlainTextResponse)
def health_check():
    return "ok"

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
# updated at 1756792221
# updated at 1756793288
# updated at 1756795261
# updated at 1756819537
# updated at 1756857373
# updated at 1756857575
# updated at 1756857792
# updated at 1756858077
# updated at 1756859343
# updated at 1756861880
# updated at 1756862524
# updated at 1756865939
# updated at 1756866525
# updated at 1756867502
# updated at 1756867586
# updated at 1756869289
