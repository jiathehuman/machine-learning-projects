FROM python:3.11-slim
COPY ./flask_demo /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python flask_predict_api.py