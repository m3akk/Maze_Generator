# Generator labirinta

Izrada labirinta u deklarativnom stilu, koristenjem: 
- Immutable varijable (bez varijabli koje mijenjaju vrijednost).
- Komponente koda su deterministične (isti inputi uvijek daju iste outpute).

Program koristi Pygame biblioteku za grafički prikaz labirinta, crtanje linija koje predstavljaju zidove između ćelija i upravljanje događajima poput zatvaranja prozora. Algoritam "Recursive Backtracker" se koristi za generiranje labirinta odabirom nasumičnih susjednih ćelija i uklanjanje zidova između njih sve dok se ne obiđu sve ćelije.

Programski jezik: Python
