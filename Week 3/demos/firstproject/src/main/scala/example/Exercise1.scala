package example

class Person(val fname: String, val lname: String, val city: String) {
    var Firstname = fname
    var Lastname = lname
    var City = city

    def printDetails(): Unit ={
        print(s"${Firstname} ${Lastname} from ${City}")
    }
}

class Employee(override val fname: String, override val lname: String, override val city: String, 
    val doj: String, val salary: Int) 
    extends Person(fname: String, lname: String, city: String) {
    
    var DOJ = doj
    var Salary = salary

    def employmentDetails(): Unit = {
        println(s" Joined on $DOJ with a salary of $Salary")
    }
}

object Exercise1 {
    def main(args: Array[String]): Unit = {
        val emp1 = new Employee("John", "Smith", "Boston", "2022-01-01", 5000)
        // emp1.printDetails()
        // emp1.employmentDetails()
        val emp2 = new Employee("Mary", "Jane", "Dallas", "2021-10-01", 5300)
        val emp3 = new Employee("Joe", "Crew", "Reston", "2019-09-10",4500)

        val employees = List(emp1, emp2, emp3)

        val emp4 = new Employee("Ajay", "Singala", "Seattle", "2020-12-05", 5300)
        val empList2 = emp4 :: employees    // pre-pend the new item to the list.

        for( e <- empList2) {
            e.printDetails()
            e.employmentDetails()
        }

        println("Only Boston Employees...")
        for( e <- empList2) {
            if(e.city == "Boston") {
                e.printDetails()
                e.employmentDetails()
            }
        }

    }
}