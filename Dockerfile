FROM python:3.14
WORKDIR /gaybar

RUN pip install atproto
RUN pip install dotenv
COPY src ./
EXPOSE 443 
CMD ["python", "./main.py"]