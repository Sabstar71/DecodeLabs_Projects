from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from predictor import predict_car

app = FastAPI(
    title="Car Evaluation Classifier",
    description="Machine Learning Car Evaluation System",
    version="1.0"
)

# ----------------------------
# Static Files
# ----------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# ----------------------------
# Home Page
# ----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": None
        }
    )


# ----------------------------
# Prediction
# ----------------------------

@app.post("/", response_class=HTMLResponse)
async def predict(
    request: Request,
    buying: str = Form(...),
    maint: str = Form(...),
    doors: str = Form(...),
    persons: str = Form(...),
    lug_boot: str = Form(...),
    safety: str = Form(...)
):

    result = predict_car(
        buying,
        maint,
        doors,
        persons,
        lug_boot,
        safety
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": result
        }
    )
# ----------------------------
# API Endpoint
# ----------------------------

@app.get("/api")
async def api_info():

    return {
        "Project": "Car Evaluation Classifier",
        "Algorithm": "Random Forest",
        "Accuracy": "97%"
    }