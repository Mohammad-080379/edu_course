 if (currentUID == authorizedUID) {
    Serial.println("دسترسی مجاز است.");
    digitalWrite(OUTPUT_PIN, HIGH);
    delay(3000);
    digitalWrite(OUTPUT_PIN, LOW);
