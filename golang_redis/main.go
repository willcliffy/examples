package main

import (
	"context"
	"encoding/json"
	"fmt"
	"time"

	"github.com/go-redis/redis/v8"
)

const (
	RedisStructKey = "struct_key"

	RedisStructField1 = "field1"
	RedisStructField2 = "field2"
	RedisStructField3 = "field3"
)

type StructSimple struct {
	Field1 string `redis:"field1"`
	Field2 int64  `redis:"field2"`
	Field3 bool   `redis:"field3"`
}

func (s StructSimple) Equal(other StructSimple) bool {
	return s.Field1 == other.Field1 && s.Field2 == other.Field2 && s.Field3 == other.Field3
}

type StructComplex struct {
	Field4 string       `json:"field4" redis:"field4"`
	Field5 int64        `json:"field5" redis:"field5"`
	Field6 bool         `json:"field6" redis:"field6"`

	Field7 time.Time    `json:"field7" redis:"field7"`
	Field8 []string     `json:"field8" redis:"field8"`

	Field9 StructSimple `json:"field9" redis:"field9"`
}

func (s StructComplex) Equal(other StructComplex) bool {
	if s.Field4 == other.Field4 && s.Field5 == other.Field5 && s.Field6 == other.Field6 &&
		s.Field7.Equal(other.Field7) && len(s.Field8) == len(other.Field8) && s.Field9.Equal(other.Field9) {
		for i := 0; i < len(s.Field8); i++ {
			if s.Field8[i] != other.Field8[i] {
				return false
			}
		}

		return true
	}

	return false
}

func (s StructComplex) MarshalBinary() ([]byte, error) {
	return json.Marshal(s)
}

func (s *StructComplex) UnmarshalBinary(data []byte) error {
	return json.Unmarshal(data, &s)
}

func main() {
	redisDb := redis.NewClient(&redis.Options{
		Addr: "redis:6379",
	})
	defer redisDb.Close()

	redisDb.FlushAll(context.Background())

	verbose := true

	fmt.Printf("starting with verbose = %v\n", verbose)

	HashCacheMain(redisDb, verbose)
	MarshalCacheMain(redisDb, verbose)

	redisDb.FlushAll(context.Background())

	fmt.Printf("done\n")
}

// Funky way of caching a struct using Redis hashes.
//
// This is useful when:
// - You are caching a struct whose fields are all basic types or implement the BinaryMarshaler interface.
// - You need to account for the possibility that some but not all of the fields may change while cached
//   and the updated value needs to be reflected.
//
// Example: a scoreboard system. 
//  Say that each player has a score and a name.
//  If a player earns a point, the score is updated. If the player's name changes, the name is updated.
//  Using this method, you needn't unmarshal, read, update, remarshal, and cache the whole scoreboard,
//  you can simply increment the appropriate player's score in the hash.
//
// Note: this is not a good way to cache a struct that contains slices or maps, or any other field 
//  that does not implement BinaryMarshaler/BinaryUnmarshaler.
func HashCacheMain(redisDb *redis.Client, verbose bool) time.Duration {
	if verbose {
		fmt.Printf("> Hash Cache Main\n")
	}

	start := time.Now().UTC()

	s_cached := StructSimple{
		Field1: "value1",
		Field2: 2,
		Field3: true,
	}

	// Cache
	hsetCmd := redisDb.HSet(context.Background(), RedisStructKey,
		RedisStructField1, s_cached.Field1,
		RedisStructField2, s_cached.Field2,
		RedisStructField3, s_cached.Field3)
	panicOnErr(hsetCmd.Err())

	// Read
	hgetCmd := redisDb.HGetAll(context.Background(), RedisStructKey)
	panicOnErr(hgetCmd.Err())
	panicOnNil(hgetCmd.Val())
	s_received := StructSimple{}
	panicOnErr(hgetCmd.Scan(&s_received))

	if verbose {
		fmt.Printf("  Cached:   %+v\n", s_cached)
		fmt.Printf("  Received: %+v\n", s_received)
	}

	if !s_cached.Equal(s_received) {
		panic("not equal")
	}

	// Update
	if verbose {
		fmt.Printf("  > Updating single field in cached struct\n")
	}

	s_cached.Field2++

	hupdateCmd := redisDb.HIncrBy(context.Background(), RedisStructKey, RedisStructField2, 1)
	panicOnErr(hupdateCmd.Err())

	// Read
	hgetCmd = redisDb.HGetAll(context.Background(), RedisStructKey)
	panicOnErr(hgetCmd.Err())
	panicOnNil(hgetCmd.Val())

	s_received = StructSimple{}
	panicOnErr(hgetCmd.Scan(&s_received))

	if verbose {
		fmt.Printf("    Cached:   %+v\n", s_cached)
		fmt.Printf("    Received: %+v\n", s_received)
	}

	if !s_cached.Equal(s_received) {
		panic("not equal")
	}

	redisDb.FlushAll(context.Background())

	return time.Since(start)
}

// This is a standard way of caching a struct.
//
// This is useful when:
// - you need to cache a struct that contains more than basic types
// - you don't expect any fields to change while cached
// - you don't need to reflect the changes to the struct while cached
//
// Example: a simple invite system. Say that each invite contains two IDs and some code to a lobby.
// Say that if the inviter leaves the lobby, the invite is removed.
// Since both the IDs and the code are immutable, you can cache the whole invite and then read it as needed.
func MarshalCacheMain(redisDb *redis.Client, verbose bool) {
	if verbose {
		fmt.Printf("> Marshal Cache Main\n")
	}

	s_cached := StructComplex{
		Field4: "value4",
		Field5: 5,
		Field6: true,

		Field7: time.Now(),
		Field8: []string{"value8"},

		Field9: StructSimple{
			Field1: "value9_field1",
			Field2: 9,
			Field3: false,
		},
	}

	// Cache
	setCmd := redisDb.Set(context.Background(), RedisStructKey, s_cached, 0)
	panicOnErr(setCmd.Err())

	// Read
	getCmd := redisDb.Get(context.Background(), RedisStructKey)
	panicOnErr(getCmd.Err())
	panicOnNil(getCmd.Val())

	s_received := StructComplex{}
	panicOnErr(getCmd.Scan(&s_received))

	if verbose {
		fmt.Printf("  Cached:   %+v\n", s_cached)
		fmt.Printf("  Received: %+v\n", s_received)
	}

	if !s_cached.Equal(s_received) {
		panic("not equal")
	}

	redisDb.FlushAll(context.Background())
}

func panicOnErr(err error) {
	if err != nil {
		panic(err)
	}
}

func panicOnNil(val interface{}) {
	if val == nil {
		panic("nil")
	}
}
