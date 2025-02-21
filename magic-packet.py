import socket
def wake_on_lan(mac_address):
    # Rimuove potenziali separatori (due punti o trattini) e trasforma il MAC in formato esadecimale
    mac_address = mac_address.replace(":", "").replace("-", "")
   
    # Controllo di validità su lunghezza MAC
    if len(mac_address) != 12:
        raise ValueError("Indirizzo MAC non valido.")
   
    # Costruisce il Magic Packet: 6 byte di 0xFF seguiti da 16 ripetizioni dell'indirizzo MAC
    magic_packet = bytes.fromhex("FF" * 6 + mac_address * 16)
   
    # Invia il pacchetto in broadcast sulla porta 9 (UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ("<broadcast>", 9))
if __name__ == "__main__":
    # Esempio di utilizzo: inserire il MAC da risvegliare
    wake_on_lan("00:11:22:33:44:55")
