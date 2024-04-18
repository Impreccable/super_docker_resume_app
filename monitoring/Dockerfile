FROM python:3.11

#créer un dossier app dans le container et cd dans app
WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./.streamlit/secrets.toml ./.streamlit/secrets.toml

COPY ./monitoring/ ./monitoring/

CMD streamlit run ./monitoring/dashboard.py

