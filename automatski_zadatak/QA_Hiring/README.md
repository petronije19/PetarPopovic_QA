Pred tobom je kostur web UI framework-a koji je potrebno da dopuniš testom za navigaciju i osnovnu validaciju kroz naš vebsajt. Kostur je pisan u Pythonu (pytest), ali zadatak mozeš raditi u jeziku po tvom izboru. Možeš koristiti PyCharm, VS Code ili bilo koji drugi tekstualni editor.

*Kako se pokreće test?*

- U terminalu, pozicioniraj se u korenski direktorijum projekta
- Kreiraj virtuelno okruženje komandom python -m venv venv
- Aktiviraj virtuelno okruženje: 
  - Ukoliko koristiš Linux/MacOS: source venv/bin/activate
  - Ukoliko koristiš Windows: venv\Scripts\activate
- Instaliraj sve neophodne pakete (pytest i selenium): pip install -r requirements.txt
- Nakon uspešne instalacije neophodnih paketa, test možeš pokretati iz terminala sa komandom:  pytest tests/test_navigation.py


*Test je potrebno da odradi sledeće korake:*
 - Visit sitemap page
   - Poseti sitemap stranicu i proveri da li se ona uspešno učitala - ovo je već implementirano u kosturu.
 - Visit homepage
    - Poseti homepage stranicu i proveri da li se ona uspešno učitala
    - Na homepage strani klikni na drugu karticu u “Amazing destinations” sekciji
    - Kada se otvori nova strana, validiraj da URL sadrži tekst “destinations/location”
 - Validacija
   - Nakon uspešno učitane strane, potvrdi da se na toj stranici nalazi element “strelica desno” u okviru sekcije {location} Fishing Seasons (primer naziva sekcije "Destin Fishing Seasons")
   - Klikni na strelicu
   - Nakon uspešnog klika na strelicu, potrebno je proveriti da se novi element (mesec) uspešno učitao


Od trenutka kada ti pošaljemo zadatak, imaćeš 5 dana da ga završiš. Ukoliko iz bilo kog razloga ne možeš da završiš zadatak u tom roku, piši nam, pa ćemo se dogovoriti oko produžetka roka.
Ne ustručavaj se da nam pišeš ukoliko imaš bilo kakva pitanja, stojimo ti na raspolaganju.

Srećno!



