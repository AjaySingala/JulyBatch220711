package example

object First {
	val x = 10		// Field.

	def main(args: Array[String]) : Unit = {
		println("Hello and welcome to your first Scala program...")
		//foo(10)
	}

	def foo(y: Int) : Unit = {		// y is a method parameter.
		val z = 20			// z is a local variable.
		println(x)
		println(y)
	}
}
