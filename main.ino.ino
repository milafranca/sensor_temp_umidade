void setup() {
  Serial.begin(9600);
}

void loop() {
  int leituraTemp = analogRead(A0);
  float tensao = leituraTemp * (5.0 / 1023.0);
  float temperaturaC = (tensao - 0.5) * 100.0;

  int leituraUmidade = analogRead(A1);
  float umidadePercentual = map(leituraUmidade, 0, 1023, 0, 100);  

  Serial.print("Temperatura: ");
  Serial.print(temperaturaC);
  Serial.print(" °C | Umidade (simulada): ");
  Serial.print(umidadePercentual);
  Serial.println(" %");

  delay(2000);
}