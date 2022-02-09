package store

import (
	"context"
	"fmt"

	"github.com/willcliffy/examples/golang-api-with-data-store/models"
)

func CreateWidget(ctx context.Context, w models.Widget) error {
	return fmt.Errorf("not implemented")
}

func GetWidget(ctx context.Context, id int64) (models.Widget, error) {
	return models.Widget{}, fmt.Errorf("not implemented")
}

func UpdateWidgetName(ctx context.Context, w models.Widget) error {
	return fmt.Errorf("not implemented")
}

func UpdateWidgetPrice(ctx context.Context, w models.Widget) error {
	return fmt.Errorf("not implemented")
}
