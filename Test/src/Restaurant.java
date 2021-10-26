package Aufgabe_1;

public class Restaurant {
	protected String name;
	protected Address address;
	protected PizzaOven pizzaOven;
	protected Person owner;
	
	public Restaurant(String name) {
		this.name = name;
	}
	
	public Restaurant(String name, Address address) {
		this.name = name;
		this.address = address;
	}
	
	public Restaurant(String name, Address address, PizzaOven oven) {
		this.name = name;
		this.address = address;
		this.pizzaOven = oven;
	}
	
	public Restaurant(String name, Address address, PizzaOven oven, Person owner) {
		this.name = name;
		this.address = address;
		this.pizzaOven = oven;
		this.owner = owner;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void rename(String name) {
		this.name = name;
	}
	
	public Address getAddress() {
		return this.address;
	}
	
	public void relocate(Address address) {
		this.address = address;
	}
	
	public void installOven(PizzaOven oven) {
		this.pizzaOven = oven;
	}
}
