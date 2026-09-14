// Package toybox provides small helper functions, mirroring the Python package's own
// mathutils/stringutils split -- a real, non-Python file for testing gladiatar-memory's
// multi-language structural scanning.
package toybox

import "strings"

// Add returns the sum of two integers.
func Add(a, b int) int {
	return a + b
}

// Reverse returns the input string reversed.
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// Greeter holds a name and can produce a greeting.
type Greeter struct {
	Name string
}

// Greet returns a friendly greeting for the Greeter's name.
func (g Greeter) Greet() string {
	return "Hello, " + strings.TrimSpace(g.Name) + "!"
}
