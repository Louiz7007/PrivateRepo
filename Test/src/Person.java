package Aufgabe_1;

public class Person {
	protected String firstName;
	protected String lastName;
	
	public Person(String first, String last) {
		this.firstName = first;
		this.lastName = last;
	}
	
	@Override
	public String toString() {
		return "Person [firstName=" + firstName + ", lastName=" + lastName + "]";
	}
}
