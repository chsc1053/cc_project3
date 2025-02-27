FROM python:3.9-alpine

WORKDIR /home/data

COPY ./IF-1.txt ./AlwaysRememberUsThisWay-1.txt ./script.py ./

CMD ["python", "script.py"]