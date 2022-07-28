package example

object LazyValDemo {
    def main(args: Array[String]): Unit = {
        lazy val message = {
            println("Initializing for the first time.")
            202
        }

        println("Calling 'message' first time...")
        println(message)

        println("Calling 'message' again...")
        println(message)
    }
}
