package Aufgabe_1;

public class Pizza {
	protected double diameter;
	protected boolean cooked;
	protected SecretPizzaSauce sauce;
	protected Topping[] topping;
	
	public Pizza(double diameter) {
		super();
		this.diameter = diameter;
	}
	
	public void cook() {
		this.cooked = true;
	}
	
	public boolean isCooked() {
		return cooked;
	}
	
	public void addPizzaSauce(SecretPizzaSauce sauce) {
		this.sauce = sauce;
	}
	
	public void addTopping(Topping[] topping) {
		for (int i = 0; i < topping.length; i++) {
			this.topping[i] = topping[i];
		}
	}
}
