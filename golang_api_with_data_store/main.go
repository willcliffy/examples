package main

import (
	"net/http"

	"github.com/go-chi/chi"
	"github.com/willcliffy/examples/golang-api-with-data-store/transport"
)

func NewRouter() chi.Router {
	r := chi.NewRouter()

	r.Get("/widget/{id}",  transport.GetWidgetHandler)
	r.Post("/widget",      transport.CreateWidgetHandler)
	r.Put("/widget/name",  transport.UpdateWidgetNameHandler)
	r.Put("/widget/price", transport.UpdateWidgetPriceHandler)

	return r
}

func main() {
	router := NewRouter()

	err := http.ListenAndServe(":8080", router)
	if err != nil {
		panic(err)
	}
}
