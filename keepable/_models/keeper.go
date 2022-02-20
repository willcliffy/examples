package models

type KeeperType uint8
const (
	KeeperType_Level1 KeeperType = 10 // In-memory storage
	KeeperType_Level2 KeeperType = 20 // External cache layer
	KeeperType_Level3 KeeperType = 30 // Database layer
)

type Keeper interface {
	Identifier() string
	Type() KeeperType

	Create(Keepable) error
	Read(string) (Keepable, error)
	Update(string, func(Keepable) (Keepable, error)) error
	Delete(Keepable) error
}
