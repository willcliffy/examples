package transport

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/willcliffy/examples/golang-api-with-data-store/models"
	"github.com/willcliffy/examples/golang-api-with-data-store/store"
)

func GetWidgetHandler(w http.ResponseWriter, r *http.Request) {
	idString := r.URL.Query().Get("id")

	id, err := strconv.ParseInt(idString, 10, 64)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusBadRequest, err.Error()))
	}

	widget, err := store.GetWidget(r.Context(), id)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusInternalServerError, err.Error()))
		return
	}

	PanicOnError(EncodeResponse(w, http.StatusOK, widget))
}

func CreateWidgetHandler(w http.ResponseWriter, r *http.Request) {
	var widget models.Widget

	err := json.NewDecoder(r.Body).Decode(&widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusBadRequest, err.Error()))
		return
	}

	err = store.CreateWidget(r.Context(), widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusInternalServerError, err.Error()))
		return
	}

	PanicOnError(EncodeResponse(w, http.StatusOK, widget))
}

func UpdateWidgetNameHandler(w http.ResponseWriter, r *http.Request) {
	var widget models.Widget

	err := json.NewDecoder(r.Body).Decode(&widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusBadRequest, err.Error()))
		return
	}

	err = store.UpdateWidgetName(r.Context(), widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusInternalServerError, err.Error()))
		return
	}

	PanicOnError(EncodeResponse(w, http.StatusOK, widget))
}

func UpdateWidgetPriceHandler(w http.ResponseWriter, r *http.Request) {
	var widget models.Widget

	err := json.NewDecoder(r.Body).Decode(&widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusBadRequest, err.Error()))
		return
	}

	err = store.UpdateWidgetPrice(r.Context(), widget)
	if err != nil {
		PanicOnError(EncodeResponse(w, http.StatusInternalServerError, err.Error()))
		return
	}

	PanicOnError(EncodeResponse(w, http.StatusOK, widget))
}
