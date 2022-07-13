FROM python:3.8

# set working directory
WORKDIR /app

COPY pokemon_guesser_cli.py ./
COPY requirements.txt ./

RUN pip install --upgrade --no-cache-dir -r ./requirements.txt
RUN apt-get update && \
    apt install -y imagemagick

RUN git clone https://github.com/stefanhaustein/TerminalImageViewer.git

RUN cd TerminalImageViewer/src/main/cpp && \
    apt install -y g++ && \
    make && \
    make install && \
    cd $home/app

CMD [ "python", "./pokemon_guesser_cli.py" ]

