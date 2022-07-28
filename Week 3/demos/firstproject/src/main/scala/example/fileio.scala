package example

import java.io._
import scala.io.Source

object FileIO {
	def main(args: Array[String]) : Unit = {
        //writeFile()
        //readFromCmdLine()
        //readFile()
        // readOneLineAtATime()

        // //val lines = Source.fromFile("test.txt").getLines().toList
        // //val lines = Source.fromFile("test.txt").getLines().toArray
        // val lines = Source.fromFile("test.txt").getLines().mkString
        // println(lines)

        // // Always close a file handle and handle exceptions.
        // try {
        //     val fileHandle = Source.fromFile("test.txt")
        //     for(line <- fileHandle.getLines()) {
        //         println(line.toUpperCase())
        //     }
        //     fileHandle.close()
        // }
        // catch {
        //     case ex: java.io.FileNotFoundException => println(s"file not found error: $ex")
        // }

        readCSV()
    }

    def readCSV(): Unit = {
        println("Month | Income | Expense | Profit")
        val fileHandle = Source.fromFile("finance.csv")
        for(line <- fileHandle.getLines()) {
            val columns = line.split(",").map(_.trim)

            println(s"${columns(0)} | ${columns(1)} | ${columns(2)} | ${columns(3)}")
        }
        fileHandle.close()

        // Use column names.
        println("\nPrint using column names....")
        val fileHandle2 = Source.fromFile("finance.csv")
        for(line <- fileHandle2.getLines()) {
            val Array(month,income,expense,profit) = line.split(",").map(_.trim)

            println(s"${month} | ${income} | ${expense} | ${profit}")
        }
        fileHandle2.close()

        // Drop the first line that is the header.
        println("\nDrop the first line that is the header....")
        val fileHandle3 = Source.fromFile("finance_header.csv")
        for(line <- fileHandle3.getLines().drop(1)) {
            val Array(month,income,expense,profit) = line.split(",").map(_.trim)

            println(s"${month} | ${income} | ${expense} | ${profit}")
        }
        fileHandle3.close()
    }

    def readOneLineAtATime(): Unit = {
        for( line <- Source.fromFile("test.txt").getLines()) {
            println(line)
        }
    }

    def readFile(): Unit = {
        Source.fromFile("test.txt").foreach {
            print
        }
        println()
    }

    def readFromCmdLine(): Unit = {
        print("Enter your name: ")
        val line = scala.io.StdIn.readLine()
        println(s"You entered '$line'")
    }

    def writeFile(): Unit = {
        val writer = new PrintWriter(new File("test.txt"))

        writer.write("Hello there!\n")
        writer.write("This is created from Scala.")
        writer.close()
    }

}
