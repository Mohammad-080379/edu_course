MFRC522 rfid(SS_PIN, RST_PIN);

// کد کارت مجاز خود را پس از اولین تست در این خط جایگزین کنید
String authorizedUID = "A1 B2 C3 D4"; 

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();