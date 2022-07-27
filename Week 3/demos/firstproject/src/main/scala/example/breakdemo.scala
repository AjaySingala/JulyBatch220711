package example

import scala.util.control.Breaks._

object breakdemo {
    def main(args: Array[String]): Unit = {
        var nums = List(1,2,3,4,5,6,7,8,9,10)

        breakable {
            for(x <- nums) {
                print(s"$x ")
                if(x >= 5)
                    break
            }
        }
    }
}
