package models

type KeepableIdentifier uint64

type KeepableComplexity uint64
const (
// Complexitity here seems to be broken down into several levels:

// Basic Types, Structures, Composites, and Recursive properties

// Basic types: string, int, float, bool, etc. Recursion does not apply
// Structures: struct                          Recursion applies
// Composites: slice, map, pointer, channel    Recursion applies

// - structures contains basic types
// - structures contains composites
// - structures contains other structures
// - structures contains other instances of themselves

// TODO - structures have the additional property of being "flat" which is related to recursive properties. not sure where or if this fits in

// COMPOSITES are homogeneous
// - COMPOSITE 1 - contains basic types
// - COMPOSITE 2 - contains structures
// - COMPOSITE 3 - contains COMPOSITE 1s
// - COMPOSITE 4 - contains COMPOSITE 2s

// STRUCTURES are heterogeneous
// - STRUCT 01 - contains only basic types
// - STRUCT 02 - contains basic types; COMPOSITE 1s
// - STRUCT 03 - contains basic types; COMPOSITE 1s and 2s
// - STRUCT 04 - contains basic types; COMPOSITE 1s, 2s, and 3s
// - STRUCT 05 - contains basic types; COMPOSITE 1s, 2s, 3s, and 4s

// TODO - I do not yet fully understand the consequences of forcing allowed COMPOSITE types to be one less than that of the allowed STRUCTURE types.
// At what struct level may a struct contain itself?
// - STRUCT 06 - contains basic types; STRUCT 1s
// - STRUCT 07 - contains basic types; COMPOSITE 1s; STRUCT 1s and 2s
// - STRUCT 08 - contains basic types; COMPOSITE 1s and 2s; STRUCT 1s, 2s, and 3s
// - STRUCT 09 - contains basic types; COMPOSITE 1s, 2s, and 3s; STRUCT 1s, 2s, 3s, and 4s
// - STRUCT 10 - contains basic types; COMPOSITE 1s, 2s, 3s, and 4s; STRUCT 1s, 2s, 3s, 4s, and 5s
)

type KeepableSize uint8
const (
	KeepableSize_1 KeepableSize = 10 // simple data types
	KeepableSize_2 KeepableSize = 20 // small, flat structs with no "complex" data
	KeepableSize_3 KeepableSize = 30 // large, flat structs with no "complex" data
	KeepableSize_4 KeepableSize = 40 // nested structs with no "complex" data
	KeepableSize_5 KeepableSize = 50 // nested structs with some "complex" data
	KeepableSize_6 KeepableSize = 60 // large, nested structs with "complex" data
)

type KeepableLifespan uint8
const (
	KeepableLifespan_1 KeepableLifespan = 10 // data is permanent, and will never be completely removed
	KeepableLifespan_2 KeepableLifespan = 20 // data is semi-permanent, and could be removed under certain conditions
	KeepableLifespan_3 KeepableLifespan = 30 // data is temporary, and could be removed under certain conditions
	KeepableLifespan_4 KeepableLifespan = 40 // data is temporary, and could be removed under certain conditions or after a certain amount of time
	KeepableLifespan_5 KeepableLifespan = 50 // data is highly volatile, and could be removed under certain contidions, after a certain amount of time, or at any time without warning
)

type KeepableVolatility uint8
const (
	KeepableVolatility_1 KeepableVolatility = 10 // data is never expected to change
	KeepableVolatility_2 KeepableVolatility = 20 // data is expected to change infrequently (e.g. once per month)
	KeepableVolatility_3 KeepableVolatility = 30 // at most, data is expected to change once every few days
	KeepableVolatility_4 KeepableVolatility = 40 // at most, data is expected to change once per hour
	KeepableVolatility_5 KeepableVolatility = 50 // at most, data is expected to change once per minute
	KeepableVolatility_6 KeepableVolatility = 60 // at most, data is expected to change once per second
	KeepableVolatility_7 KeepableVolatility = 70 // data is expected to change more than once per second
)