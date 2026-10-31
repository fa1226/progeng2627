
  int notes[] = {262, 294, 330, 349};
//setting up an array of four notes of above frequencies

  void setup() {
    Serial.begin(9600);
  //beginning serial communication
  }

  void loop() {
    int keyVal = analogRead(A0);
    //setting up a local variable to read signal sent from each switch to A0 terminal
    Serial.println(keyVal);
    //optional - to see what value each button corresponds to
    if(keyVal >= 1015 && keyVal <= 1045){
    //if signal is around 1023, play note of frequency 262Hz. 
      tone(8, notes[0]);
    }
    else if(keyVal >= 990 && keyVal <= 1010){
      tone(8, notes[1]);
    }
    else if(keyVal >= 505 && keyVal <= 515){
      tone(8, notes[2]);
    }
    else if(keyVal >= 5 && keyVal <= 10){
      tone(8, notes[3]);
    }
    else{
    noTone(8);
  
    }
  } 