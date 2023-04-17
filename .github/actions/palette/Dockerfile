FROM alpine:3.17
RUN apk add python3 py3-pip git
RUN python3 -m pip install "palettelib @ git+https://github.com/justjanne/palettelib@main"
COPY generate.py /generate.py
ENTRYPOINT [ "/bin/sh", "-c" ]
