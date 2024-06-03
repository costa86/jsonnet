package main

import (
	"fmt"
	"log"
	"os"

	"github.com/google/go-jsonnet"
)

func main() {
	vm := jsonnet.MakeVM()

	// snippet := `{
	// 	person1: {
	// 	    name: "Alice",
	// 	    welcome: "Hello " + self.name + "!",
	// 	},
	// 	person2: self.person1 { name: "Bob" },
	// }`
	snippet := os.Args[1]

	jsonStr, err := vm.EvaluateAnonymousSnippet("example1.jsonnet", snippet)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(jsonStr)
}
