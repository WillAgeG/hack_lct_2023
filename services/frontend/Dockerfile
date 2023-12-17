FROM node:13.12.0-alpine as build

WORKDIR /app

COPY package.json package.json

COPY package-lock.json package-lock.json

RUN npm i

COPY . .

RUN mkdir /frontend_static/

CMD ["cp", "-r", "/app/src/.", "/frontend_static/."]
