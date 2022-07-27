package example

import scala.util.control._
import scala.util.control.Breaks._

object NestedLoop {
    def main(args: Array[String]): Unit = {
        var num1 = List(1,2,3,4,5)
        var num2 = List(11,12,13)

        val outerLoop = new Breaks
        val innerLoop = new Breaks

        outerLoop.breakable {
            for(n1 <- num1) {
                println(s"num1 value $n1")

                innerLoop.breakable {
                    for( n2 <- num2) {
                        println(s"num2 value $n2")

                        if(n2 == 12) {
                            outerLoop.break()
                        }
                    }
                }
            }
        }
    }
}
