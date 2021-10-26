package Aufgabe_1;

public class Main {

	public static void main(String[] args) {
		Person louis = new Person("Louis", "Dittmann");
//		System.out.println(louis.toString());
		Address addresse = new Address("Am Schützenplatz", "Lehrte", "1b");
//		System.out.println(addresse.toString());
		PizzaOven ofen = new PizzaOven(250);
		Pizza salami = new Pizza(26);
//		System.out.println(salami.isCooked());
//		ofen.insert(salami);
//		ofen.takeOut();
//		System.out.println(salami.isCooked());
		Restaurant goldeneMoewe = new Restaurant("Goldene Möwe", addresse, ofen, louis);
//		System.out.println(goldeneMoewe.getName());
//		System.out.println(goldeneMoewe.getAddress());
//		goldeneMoewe.rename("Peter");
//		System.out.println(goldeneMoewe.getName());
	}

}
