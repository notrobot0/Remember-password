Sometimes it happens that you don’t remember a couple of letters in your password. This script allows you to make a list of passwords.
Suppose I remember that my password is Справедливость. But I'm definitely not sure about the first letter. I remember what it is "С" or "c" or "S". 
In this case, I open this script and enter:
<code>arr=[['S','s','с','С'],['п'],['р'],['а'],['в'],['е'],['д'],['л'],['и'],['в'],['о'],['с'],['т'],['ь']] </code>
Then I run the script:
python3 main.py >pass.txt
In this case, the pass.txt file will contain the following:
Sправедливость
sправедливость
справедливость
Справедливость
The same thing can be done with any number of letters!
