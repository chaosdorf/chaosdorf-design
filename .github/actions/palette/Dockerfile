FROM alpine:3.17
RUN apk add python3 py3-pip git
RUN python3 -m pip install "palettelib @ git+https://github.com/justjanne/palettelib@f18bab2de55d54c1c560ba2419b49d51fe7367ac"
COPY generate.py /generate.py
ENTRYPOINT [ "/bin/sh", "-c" ]
