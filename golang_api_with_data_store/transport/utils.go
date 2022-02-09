package transport

import (
	"encoding/json"
	"net/http"
)

func EncodeResponse(w http.ResponseWriter, status int, response interface{}) error {
	w.WriteHeader(status)
	w.Header().Set("Content-Type", "application/json")

	if response == nil {
		return nil
	}

	return json.NewEncoder(w).Encode(response)
}

func PanicOnError(err error) {
	if err != nil {
		panic(err)
	}
}
