package example

import scala.io.Source
import java.io.IOException
import java.io.FileNotFoundException

object ExceptionDemo {
    def main(args: Array[String]): Unit = {
        try {
            println("Dividing numbers...")
            println(divide(10,2))
            //println(divide(10,0))

            // println("Reading contents of file demo.txt...")
            // Source.fromFile("Demo.txt").foreach {
            //     print
            // }

        //     println("Demo'ing generic exception handling...")
        //     foo()
        }
        catch {
            case aex: ArithmeticException => {
                println("You tried to divide by zero!")
            }
            case fex: FileNotFoundException => {
                println("Trying to read a file that does not exist.")
            }
            case ex: Throwable => {
                println(s"Something went wrong! $ex")
            }
        }
        finally {
            println("This will execute no matter what!")
        }
    }

    def divide(x:Int, y:Int): Any = {
        x / y
    }

    def foo() : Unit = {
        throw new Exception("This is a custom exception for demo.")
    }

}