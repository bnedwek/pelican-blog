FROM debian:latest as PELICAN

RUN apt-get update -y
RUN apt-get install -y python3.7 python3-pip

RUN pip3 install pelican[Markdown]

COPY . /static-site

RUN pelican /static-site/content/

FROM nginx:stable-alpine
RUN mv /usr/share/nginx/html/index.html /usr/share/nginx/html/old-index.html
COPY --from=PELICAN /static-site/output/ /usr/share/nginx/html/

EXPOSE 80