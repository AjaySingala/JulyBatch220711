package example

object NestedFn {
    def main(args: Array[String]): Unit = {
        println(max(10,5,20))
        println(max(5,20,10))
        println(max(110,25,15))

        // println(max2(100,200))  // Error!
    }

    def max(x: Int, y: Int, z: Int): Int = {
        def max2(a: Int, b: Int) : Int = if (a > b) a else b

        max2(x, max2(y,z))

        // // Alternate.
        // val round1 = max2(y,z)
        // val round2 = max2(x,round1)
        // round2
    }
}