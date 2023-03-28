import java.util.EmptyStackException

class ArrayListStack<E> : Stack<E> {

    private var stack: ArrayList<E> = ArrayList()
    override fun push(element: E) {
        stack.add(element)
    }

    override fun pop(): E? {
        if (stack.size == 0){
            return null
        }
        return stack.removeAt(stack.size - 1)
    }

    override fun top(): E {
        if (stack.isEmpty()){
            throw EmptyStackException()
        }
        return stack[stack.lastIndex]
    }

    override fun isEmpty(): Boolean {
        return stack.isEmpty()
    }

    override fun size(): Int {
        return stack.size
    }
}