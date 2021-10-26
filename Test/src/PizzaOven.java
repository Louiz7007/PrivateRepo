package Aufgabe_1;

public class PizzaOven {
	protected double temperature;
	protected Pizza baking;
	
	public PizzaOven(double temperature) {
		super();
		this.temperature = temperature;
	}

	public double getTemperature() {
		return temperature;
	}
	
	public static PizzaOven create() {
		return new PizzaOven(0);
	}
	
	public void increaseTemperature(double to) {
		this.temperature = to;
	}
	
	public void insert(Pizza pizza) {
		this.baking = pizza;
		baking.cook();
	}
	
	public Pizza takeOut() {
		baking.isCooked();
		return baking;
		
	}
}
