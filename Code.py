
from pythonosc import udp_client

MA3_IP = "192.168.1.12"  # Replace with your GrandMA3 console's IP address
MA3_OSC_PORT = 8000    # Standard OSC port for GrandMA3


client = udp_client.SimpleUDPClient(MA3_IP, MA3_OSC_PORT)

# Basic OSC message structure
Fixture = 402
tilt = 0
pan = 0
# Example: Turning on fixture 1

#client.send_message("/gma3/Page1/Fader201",0)

client.send_message("/gma3/cmd", f'Fixture {Fixture} At {tilt} Attribute "Tilt"')
print(f'{Fixture} At Tilt {tilt}')
client.send_message("/gma3/cmd", f'Fixture {402} At {pan} Attribute "Pan"')
print(f'{Fixture} At Pan {pan}')