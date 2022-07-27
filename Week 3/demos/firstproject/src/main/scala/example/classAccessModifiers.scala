package example

class Outer {
    class Inner {
        private def foo(): Unit = {
            println("Inner.foo()...")
        }

        class InnerMost {
            foo()
        }
    }

    // val innerObj = new Inner()
    // innerObj.foo()
}

class ClassA {
    var name = "Default"
    private def foo(): Unit = {
        println("ClassA.foo()...")
        println(s"The name is ${this.name}")
    }

    def foobar(): Unit = {
        println("ClassA.foobar()...")
        foo()
        foobaz()
    }

    protected def foobaz(): Unit = {
        println("ClassA.foobaz()...")
    }
}

class ClassB extends ClassA {
    def test(): Unit = {
        println("ClassB.test()...")
        foobaz()
    }
}

final class ClassX {
    def method1(): Unit = {
        println("ClassX.method1()...")
    }
}

// // final class cannot be inherited.
// class ClassY extends ClassX {

// }

sealed class Car {
    def Start(): Unit = {
        println("Car.Start()...")
    }
}


class BMW extends Car {
    override def Start(): Unit = {
        println("BMW.Start()...")
    }
}

object ClassAccessModifiers {
    def main(args: Array[String]): Unit = {

        val classAObj = new ClassA()
        classAObj.foobar()
        println(classAObj.name)

        val classAObj_new = new ClassA()
        classAObj_new.name = "John Smith"
        classAObj_new.foobar()
        
        classAObj.foobar()

        // //classAObj.foobaz()        // error!

        // val classBObj = new ClassB()
        // classBObj.test()

        // val cx = new ClassX()
        // cx.method1()
        // // val cy = new ClassY()
        // // cy.method1()

        // val car = new Car()
        // car.Start()

        // val bmw = new BMW()
        // bmw.Start()
    }
}