fun main(args: Array<String>) {
    //Where need is greatest should be greatest is need where
    //b) Simplicity is genius should be genius is simplicity
    var stringStack: Stack<String> = ArrayListStack()
//    println("Enter a sentence to be reversed: ")
//    val Input = readLine()!!
//    while (Input != null){
    stringStack.push("Where")
    stringStack.push("need")
    stringStack.push("is")
    stringStack.push("greatest")
    stringStack.push("should")
    stringStack.push("be")
    stringStack.push("greatest")
    stringStack.push("is")
    stringStack.push("need")
    stringStack.push("where")
    var reverseString = " "
    val i = stringStack.size()
    var j = 0
    while (j < i){
       var k = stringStack.pop()
        reverseString += (" " + k)
        j += 1
    }
    println(reverseString)

}
