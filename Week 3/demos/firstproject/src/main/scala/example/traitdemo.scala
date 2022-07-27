package example

trait Animal {
    def speak() : Unit = {                  // non-abstract method.
        println("This animal speaks.")
    }

    def move(): Unit                        // abstract method.

}


class Mammal {
    def features(): Unit = {
        println("A mammal does not lay eggs.")
    }
}

class Dog extends Mammal with Animal {
    override def speak(): Unit = {
        println("Woof!")
    }

    def move(): Unit = {
        println("runs...")
    }
}

object TraitDemo {
    def main(args: Array[String]): Unit = {
        val dog1 = new Dog()
        dog1.speak()
        dog1.move()
        dog1.features()

        // val t1 = new Animal()   // Error!
    }
}