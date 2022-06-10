FROM python:3.8

WORKDIR /

COPY printer.py ./

CMD ["python", "./printer.py"]