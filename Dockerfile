FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /devops_test_project
COPY requirements.txt /devops_test_project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /devops_test_project/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

