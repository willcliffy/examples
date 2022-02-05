FROM golang:1.17

RUN mkdir -p /app
WORKDIR /app

ADD . /app

RUN ["go", "get", "github.com/githubnemo/CompileDaemon"]
RUN go build -o /dist/main /app/main.go

CMD ["/dist/main"]
