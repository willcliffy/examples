package models

type Keepable interface {
	Identifier() KeepableIdentifier

	Size()       KeepableSize
	Lifespan()   KeepableLifespan
	Volatility() KeepableVolatility

	Payload()    interface{}
}


