package example

object TupleDemo {
    def main(args: Array[String]): Unit = {
        val data = getCustomerData()
        println(s"Customer data is: $data")
        data.productIterator.foreach{ i => println(s"Value is $i") }
    }

    def getCustomerData() = {
        val customerInfo = (101, "John", "Smith", 55, 125.75f)
        customerInfo
    }
}