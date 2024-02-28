// This is without SMS library
// It's the Eli's tutorial
// https://github.com/elifieldsteel/SuperCollider-Tutorials/blob/master/full%20video%20scripts/19_script.scd
// https://youtu.be/_NpivsEva5o?si=sCme4WUqVXArHrYz&t=772

Quarks.gui;

SerialPort.listDevices
~port = SerialPort.new("COM6", 115200, crtscts:true);
~port.read;
~port.close;

~serial_monitor = [ ];
//read 10bit serial data sent from Arduino's Serial.println
(
r = Routine({
    var byte, str, res;
    99999.do{|i|
		    str = "";
		    // Read characters from the serial port until a newline character (ASCII 13) is encountered
            while({byte = ~port.read; byte !=13 }, {
                str= str++byte.asAscii;
            });
            res= str.asInteger;
            ("read value:"+res).postln;
    };
}).play;
)
r.stop

(
// Create a routine to continuously read from the serial port
~r = Routine({
    var byte, str = "", res;
    inf.do {
        // Read characters from the serial port until a newline character (ASCII 13) is encountered
        while({ byte = ~port.read; byte != 13 }, {
            str = str ++ byte.asAscii; // Append each character to the string
        });

        // Remove leading and trailing whitespace
        str = str.trim;
		("string:"+str).postln
        // Check if the string starts and ends with square brackets
        if (str.startsWith("[") && str.endsWith("]")) {
            // Remove the brackets
            str = str.copyRange(1, str.size - 2);

            // Split the string by spaces and parse as integers
            res = str.split(" ").collect(_.asInteger);

            // Post the read values
			("read value:"+res).postln
        }
    };
});
)

// Start the routine
~r.play;

// Stop the routine when finished
// ~r.stop;


(
~serial_monitor = [ ];
15.do{~serial_monitor = ~serial_monitor.add(~port.read)};
~serial_monitor = ~serial_monitor.collect(_.asAscii);
)

~serial_monitor.collect(_.class);


(
~charArray = [];
~getValues = Routine.new({
	var ascii;
	{
		ascii = ~port.read.asAscii;
		if(ascii.isDecDigit, {~charArray = ~charArray.add(ascii)});
		if(ascii == $H, {
			~val = ~charArray.collect(_.digit).convertDigits;
			~charArray = [];

		});
	}.loop;
}).play
)

(
r = Routine({
    inf.do{|i|
        ~port.put(i.fold(0, 100).linexp(0, 100, 1, 255).asInteger.postln);
        0.9.wait;
    };
}).play;
)

r.stop;
s.boot;  // start sound synthesis engine

(
SynthDef.new(\saw, {
	arg cutoff=1000;
	var sig;
	sig = Saw.ar([50,51]);
	sig = RLPF.ar(sig, cutoff.lag(0.02), 0.25, 0.2);
	Out.ar(0, sig);
}).add;
)

// Start synth sound
~synth = Synth(\saw);


// control the synth with the sensor
(
~control = Routine.new({
	{
		~synth.set(\cutoff, ~val.linexp(0,1023,80,4000));
		0.01.wait;
	}.loop
}).play
)

(
~control.stop;
~synth.free;
)