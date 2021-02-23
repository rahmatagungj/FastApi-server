from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API Work's"}


@app.get("/kbbi/{find}")
async def read_item(find):
    try:
        r = requests.get(f"https://kbbi-api-zhirrr.vercel.app/api/kbbi?text={find}")
        r = r.json()
        frasa = r["lema"]
        arti = r["arti"]
        return {"Frasa": frasa, "Arti": arti}
    except:
        return {"message": "Not Found"}


@app.get("/covid/")
async def read_item():
    try:
        r = requests.get("https://api.kawalcorona.com/indonesia/")
        r = r.json()
        for i in r:
            negara = i["name"]
            positif = i["positif"]
            sembuh = i["sembuh"]
            meninggal = i["meninggal"]
            dirawat = i["dirawat"]
            break
        return {
            "Positif": positif,
            "Sembuh": sembuh,
            "Meninggal": meninggal,
            "Dirawat": dirawat,
        }
    except:
        return {"message": "Not Found"}