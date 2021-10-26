package Aufgabe_1;

public class Address {
	private String street;
	private String city;
	private String houseNumber;
	
	public Address(String street, String city, String houseNumber) {
		super();
		this.street = street;
		this.city = city;
		this.houseNumber = houseNumber;
	}

	public String getStreet() {
		return street;
	}

	public String getCity() {
		return city;
	}

	public String getHouseNumber() {
		return houseNumber;
	}

	@Override
	public String toString() {
		return "Address [street=" + street + ", city=" + city + ", houseNumber=" + houseNumber + "]";
	}
		
}
