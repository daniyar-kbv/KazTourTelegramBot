FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /kaztour_bot
RUN mkdir /kaztour_bot/static
RUN mkdir /kaztour_bot/media
RUN mkdir /kaztour_bot/tmp

WORKDIR /kaztour_bot

ADD requirements.txt /kaztour_bot/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /kaztour_bot/

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

COPY ./entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]