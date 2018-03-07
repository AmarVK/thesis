
set chan [socket 192.167.1.7 12345]         ;# Open the connection
puts $chan hello                         ;# Send a string
flush $chan                              ;# Flush the output buffer
puts "10.0.0.2:12345 says [gets $chan]"  ;# Receive a string
close $chan                              ;# Close the socket