FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /studybud
COPY requirements.txt /studybud/
RUN pip install -r requirements.txt
COPY . /studybud/