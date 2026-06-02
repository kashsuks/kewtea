# kewtea
A 30% low profile ortholinear keyboard.

I've recently found that normal keyboards just have too much going on, so it's time to make things simple.

<img width="838" height="731" alt="image" src="https://github.com/user-attachments/assets/8d477375-29ca-4509-8c90-9bbe58a6f40c" />

## Bill of Materials

| Name                                        | Quantity | Purpose                                 | Link                                                                  | Cost (CAD) | Cost (USD) |
|---------------------------------------------|----------|-----------------------------------------|-----------------------------------------------------------------------|------------|------------|
| Kailh Choc Low Profile Switches (set of 10) | 3        | Switches for the keys                   | https://typeractive.xyz/products/choc-switches?variant=51038935122151 | 24.00      | 17.40      |
| DO-35 Diodes (set of 50)                    | 1        | Diodes for the keys grid                | https://www.aliexpress.com/item/1005006711895793.html                 | 3.89       | 2.82       |
| 0.91 Inch 128x32 I2C OLED Display           | 1        | OLED display                            | https://www.aliexpress.com/item/1005008640132638.html                 | 3.27       | 2.37       |
| Pro Micro NRF52840                          | 1        | Cheaper alternative to nice!nano v2 mcu | https://www.aliexpress.com/item/1005009026511947.html                 | 5.67       | 4.11       |
| MBK Choc Keycaps (set of 10)                | 3        | Keycaps needed for the switches         | https://typeractive.xyz/products/mbk-keycaps                          | 15.00      | 10.87      |
| JLCPCB PCB Manufacturing                    | 1        | The actual pcb board                    | https://jlcpcb.com/                                                   | N/A        | 10.02      |
## Code

I used [kmk](https://github.com/KMKfw/kmk_firmware) along with the circuitpython Nice!nano `.UF2`. They can be used interchangeably with the Pro Micro NRF52840 since it's based off the nice!nano.

The code is yet to be thoroughly tested and will be done so after recieving the board :)

## Schematic

<img width="953" height="542" alt="image" src="https://github.com/user-attachments/assets/73f790ab-3837-4290-9b86-d57643231f0d" />

## PCB

<img width="795" height="375" alt="image" src="https://github.com/user-attachments/assets/021c36b4-704f-4129-a958-c0908bc9a700" />
<img width="638" height="293" alt="image" src="https://github.com/user-attachments/assets/c3c6f4df-e387-4f67-a625-993439510f01" />

