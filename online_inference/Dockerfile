FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

ENV PATH_TO_MODEL="/app/models/model.sav"
ENV MODEL_URL="https://drive.google.com/uc?id=1Az47NJk2Tn30MkrkqlfcAraekf3wam4W"

# preparation
RUN pip install -r requirements.txt && /app/scripts/download_model.sh

EXPOSE 5000

CMD ["python", "/app/src/app.py"]