package example

import scala.util.matching.Regex

object RegExDemo {
    def main(args: Array[String]): Unit = {
        val msg = "Scala is _cala 8cala $cala Scalable and cool, Scela Scula Scola Scyla Scila Sc8la Sc88la Sc90la ScAla, Sc12345la Scaala Scaaaaaala"
        val pattern = "Scala\\s".r

        println(pattern findFirstIn msg)
        println((pattern findAllIn msg).mkString(","))

        // println(pattern replaceFirstIn(msg, "Python"))
        // println(pattern replaceAllIn(msg, "Python"))

    }
}
