package models

// Triage is responsible for taking a Keepable and storing it in a Keeper according to its properties
type Triage interface {
	Identifier() string

	Create(Keepable) error
	Read(string) (Keepable, error)
	Update(string, func(Keepable) (Keepable, error)) error
	Delete(Keepable) error
}
