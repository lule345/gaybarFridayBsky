FROM python:3.14
WORKDIR /gaybar

RUN pip install atproto
RUN pip install dotenv
COPY src ./src
EXPOSE 443 