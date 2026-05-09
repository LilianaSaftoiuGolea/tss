T1 – Testare unitară în Python 
Săftoiu (Golea) Genica - Liliana
An 3, grupa 2, Informatica ID
 1. Introducere
Clasa aleasă pentru testare este `OrderCalculator`, implementată în fișierul `src/order_calculator.py`. Aceasta calculează totalul final al unei comenzi pe baza unor liste de prețuri și cantități, a statutului premium al clientului, a unui cupon de reducere și a opțiunii de transport urgent. În plus, clasa oferă o metodă de clasificare a comenzilor în funcție de valoarea totală.
În proiect au fost construite:
- o suita de teste
- o suita de teste generata de AI
- rapoarte de coverage
- rapoarte de mutation testing
- diagrame, etc.
2. Cerința proiectului
Tema = utilizarea unui framework de testare unitară din Python pentru testarea funcționalităților unei clase:
- partiționare în clase de echivalență
- analiza valorilor de frontieră
- acoperire la nivel de instrucțiune, de decizie, de conditie
- analiză a raportului generat de un generator de mutanți
- teste suplimentare pentru eliminarea mutanților neechivalenți rămași în viață
 3. Descrierea aplicației testate
3.1. Clasa testată
Clasa testată este:
class OrderCalculator:


Aceasta conține:
- un atribut:
  - `urgent_shipping_fee`
- două metode publice:
  - `calculate_final_total(...)`
  - `classify_order(...)`
 3.2. Funcționalitatea metodei `calculate_final_total`
Metoda `calculate_final_total` primește următorii parametri:
- `prices` – listă de prețuri unitare;
- `quantities` – listă de cantități;
- `is_premium` – indică dacă utilizatorul este premium;
- `coupon_percent` – procentul cuponului de reducere;
- `urgent_shipping` – indică dacă se aplică transport urgent.
Metoda implementează următoarele reguli:
1. validează lungimea listelor;
2. validează intervalul permis pentru cupon;
3. parcurge fiecare pereche `(price, qty)` printr-o instrucțiune repetitivă;
4. validează prețurile și cantitățile;
5. aplică discount bulk pentru `qty >= 10`;
6. aplică discount premium dacă `is_premium` este `True` și `total >= 500`;
7. adaugă taxa de transport urgent, dacă este necesar;
8. aplică un discount suplimentar dacă există cel puțin două linii bulk;
9. aplică reducerea prin cupon;
10. returnează totalul final rotunjit la 2 zecimale.
3.3. Funcționalitatea metodei `classify_order`
Metoda `classify_order(final_total)`:
- ridică `ValueError` dacă valoarea este negativă;
- returnează:
  - `"small"` pentru valori sub 200;
  - `"medium"` pentru valori între 200 și 500 inclusiv;
  - `"large"` pentru valori mai mari de 500.
- instrucțiune repetitivă: parcurgerea perechilor `(price, qty)` cu `for`
- condiție simplă: `qty >= 10`;
- condiție compusă: `is_premium and total >= 500`.
 4. Structura proiectului
Structura proiectului este următoarea:
t1_testare_unitara_python/
├── src/
│   └── order_calculator.py
├── tests/
│   ├── test_functional.py
│   ├── test_structural.py
│   ├── test_mutation.py
│   ├── test_functional_ai.py
│   ├── test_structural_ai.py
│   └── test_mutation_ai.py
│   ├── class_diagram.png
│   └── control_flow_diagram.png
├── raport_ai.md
├── cosmic-ray.toml
├── README.docx
 5. Configurația hardware și software
5.1. Configurație hardware
- Procesor: Intel Core i7-11800H
- Memorie RAM: 32 GB
5.2. Configurație software
- Sistem de operare: Windows
- Limbaj de programare:Python 3.12.7
- Framework de testare:`unittest`
- Tool pentru coverage: `coverage.py`
- Tool pentru mutation testing:`Cosmic Ray`
- Editor:Visual Studio Code
5.3. Mașină virtuală
Proiectul a fost realizat fără utilizarea unei mașini virtuale.
6. Suita de teste
Suita de teste este alcătuită din:
- `tests/test_functional.py`
- `tests/test_structural.py`
- `tests/test_mutation.py`
Aceasta reprezintă partea principală a proiectului.
7. Strategii de testare funcțională
Testarea funcțională a fost realizată în fișierul `tests/test_functional.py`.
7.1. Partiționarea în clase de echivalență
Au fost definite clase de echivalență valide și invalide.
Clase valide
- comandă obișnuită, fără reduceri;
- comandă cu discount bulk;
- comandă premium cu prag atins;
- comandă cu transport urgent;
- comandă cu cel puțin două linii bulk.
 Clase invalide
- liste vide;
- liste cu lungimi diferite;
- preț negativ;
- cantitate zero;
- cupon negativ;
- cupon peste limita permisă.
7.2. Analiza valorilor de frontieră
Au fost urmărite frontierele relevante pentru:
- `qty = 9` / `qty = 10`
- `coupon_percent = -1, 0, 30, 31`
- `total = 499.99` / `500`
- clasificare la `199.99`, `200`, `500`, `500.01`
 8. Strategii de testare structurală
Testarea structurală a fost realizată în fișierul `tests/test_structural.py`.
8.1. Statement coverage
Au fost create teste care execută toate instrucțiunile importante din:
- `calculate_final_total`
- `classify_order`
8.2. Decision coverage
Pentru principalele decizii din cod am proiectat teste, astfel încât fiecare decizie să fie evaluată atât cu `True`, cât și cu `False`.
Exemple de decizii urmărite:
- validarea lungimii listelor;
- validarea cuponului;
- validarea valorilor individuale;
- `qty >= 10`
- `is_premium and total >= 500`
- `urgent_shipping`
- `bulk_discount_lines >= 2`
- `final_total < 0`
8.3. Circuite independente
Au fost create teste care urmăresc căi independente prin program:
- cale normală fără discounturi;
- cale cu discount bulk;
- cale cu discount premium;
- cale cu transport urgent;
- cale cu două linii bulk;
- căi de eroare care duc la `ValueError`.
9. Mutation testing pentru suita proprie
În fișierul `tests/test_mutation.py` au fost introduse teste suplimentare pentru mutanții rămași în viață.
 9.1. Scop
După prima evaluare cu Cosmic Ray au fost identificați mutanți supraviețuitori. Pe baza raportului au fost adăugate teste suplimentare pentru cazuri sensibile, de exemplu:
- `qty > 10`
- `total > 500`
- `bulk_discount_lines > 2`
- `classify_order(0)`
- lungimi mari egale pentru liste
- cantități negative
9.2. Rezultat final
După îmbunătățirea suitei proprii:
- `total jobs: 153`
- `surviving mutants: 2 (1.31%)`
 
10. Rezultatele obținute pentru suita proprie
 10.1. Rularea tuturor testelor
Comanda utilizată:
py -m unittest discover -s tests -v
Rezultat:
- 63 teste
- toate trecute cu succes
Test_functional
 
 
Test_structural
 
 
 


 

 
 10.2. Coverage
Comenzile utilizate:
py -m coverage erase
py -m coverage run --branch -m unittest discover -s tests -v
py -m coverage report -m
py -m coverage html
Rezultatul principal pentru suita proprie:
- `src/order_calculator.py` – 100% coverage
- coverage total – 98%
 
10.3. Mutation testing
Comenzile utilizate:
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray.toml
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
Rezultatul final:
- 153 mutanți
- 2 mutanți rămași în viață
 
 
 
 
 
 
 
 
11. Suita generată cu AI
Suita generata cu AI este alcătuită din:
- `tests/test_functional_ai.py`
- `tests/test_structural_ai.py`
- `tests/test_mutation_ai.py`
12. Rezultatele obținute pentru suita AI
 12.1. Rularea testelor AI
Comenzile utilizate:
py -m unittest -v tests.test_functional_ai
py -m unittest -v tests.test_structural_ai
py -m unittest -v tests.test_mutation_ai
Rezultate:
- `test_functional_ai.py` – 6 teste, toate trecute;
- `test_structural_ai.py` – 4 teste, toate trecute;
- `test_mutation_ai.py` – 4 teste, toate trecute.
În total:
- 14 teste
- toate trecute cu succes
12.2. Coverage pentru suita AI
Comenzile utilizate:
py -m coverage erase
py -m coverage run --branch -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
py -m coverage report -m
Rezultatul obținut:
Name                          Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------
src\order_calculator.py          36      0     22      0   100%
tests	est_functional_ai.py      38      1     10      1    96%   138
tests	est_mutation_ai.py        28      1      6      1    94%   58
tests	est_structural_ai.py      37      1      8      1    96%   97
-------------------------------------------------------------------------
TOTAL                           139      3     46      3    97%
Concluzii:
- `src/order_calculator.py` – 100% coverage
- coverage total pentru suita AI – 97%
12.3. Mutation testing pentru suita AI
A fost utilizată o configurație separată:
cosmic-ray init cosmic-ray-ai.toml session_ai.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ai.toml
cosmic-ray exec cosmic-ray-ai.toml session_ai.sqlite
cr-report session_ai.sqlite
Rezultatul final:
- 153 mutanți
- 2 mutanți rămași în viață
13. Comparație între suita proprie și suita AI
Criteriu:  Suita proprie / Suita generată cu AI 
  Număr de teste: 63 / 14 
  Framework utilizat: `unittest` / `unittest` 
  Fișiere de test: 3 / 3 
  Coverage pe `src/order_calculator.py` : 100% / 100% 
  Coverage total: 98% / 97% 
  Mutation testing: 2 mutanți rămași din 153 / 2 mutanți rămași din 153 
  Teste funcționale: detaliate / prezente, dar mai concentrate 
  Teste structurale: urmărite explicit / urmărite mai sintetic 
  Teste pentru mutanți: țintite / prezente, dar mai puține 
13.1. Interpretare
Deși suita AI este mult mai mică decât suita proprie, ea a obținut rezultate apropiate:
- 100% coverage pe fișierul sursă;
- același număr de mutanți rămași în viață.
Suita AI este utilă:
- ca sursă alternativă de idei;
- ca bază de comparație.
14. Bucăți reprezentative de cod
14.1. Exemplu din implementare
if is_premium and total >= 500:
    total *= 0.90
else:
    total *= 1.0
Acest fragment este relevant deoarece conține:
- condiție compusă;
- ramură `if`;
- ramură `else`.
14.2. Exemplu din suita funcțională
def test_boundary_coupon_30(self):
    result = self.calc.calculate_final_total(
        prices=[100],
        quantities=[1],
        is_premium=False,
        coupon_percent=30,
        urgent_shipping=False,
    )
    self.assertEqual(result, 70.0)
 14.3. Exemplu din suita de mutații
def test_mutation_classify_zero(self):
    self.assertEqual(self.calc.classify_order(0), "small")
Acest test este important pentru detectarea mutanților sensibili la pragul `0`.
 15. Diagrame
În proiect sunt incluse două diagrame:
- `class_diagram.png`
 
- `control_flow_diagram.png`

 
15.1. Diagrama UML
Diagrama UML prezintă:
- clasa `OrderCalculator`;
- atributul `urgent_shipping_fee`;
- metodele publice testate.
15.2. Diagrama de control / flowchart
Flowchart-ul descrie logica metodei `calculate_final_total`:
- validări;
- bucla principală;
- aplicarea reducerilor;
- condițiile de ieșire și returnarea rezultatului.
16. Utilizarea unui tool AI
În raport_ai.docx sunt prezentate:
- promptul folosit;
- răspunsul AI;
- capturi de ecran;
- comparația dintre suita proprie și suita generată;
- interpretarea rezultatelor.
17. Cerințe de rulare
 17.1. Rularea suitei proprii
py -m unittest discover -s tests -v
17.2. Rularea suitei AI
py -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
17.3. Coverage pentru suita proprie
py -m coverage erase
py -m coverage run --branch -m unittest discover -s tests -v
py -m coverage report -m
py -m coverage html
 17.4. Coverage pentru suita AI
py -m coverage erase
py -m coverage run --branch -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
py -m coverage report -m
17.5. Mutation testing pentru suita proprie
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray.toml
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
17.6. Mutation testing pentru suita AI
cosmic-ray init cosmic-ray-ai.toml session_ai.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ai.toml
cosmic-ray exec cosmic-ray-ai.toml session_ai.sqlite
cr-report session_ai.sqlite
18. Concluzii finale
Proiectul a demonstrat aplicarea practică a strategiilor de testare unitară în Python asupra unei clase reale. 
Suita de teste:
- este mai amplă;
- este mai bine documentată;
- urmărește explicit cerințele academice ale temei.
Suita de teste AI:
- este mai compactă;
- a oferit o bază alternativă utilă;
- a obținut rezultate apropiate după validare.
Concluzia generală este că un tool AI poate fi foarte util ca instrument auxiliar în testare, dar nu înlocuiește analiza umană. 
19. Referințe bibliografice
[1] Python Software Foundation, `unittest` — Unit testing framework, https://docs.python.org/3/library/unittest.html, Data ultimei accesări: 9 mai 2026.  
[2] Ned Batchelder, Coverage.py, https://coverage.readthedocs.io/, Data ultimei accesări: 9 mai 2026.  
[3] Cosmic Ray Documentation, https://cosmic-ray.readthedocs.io/, Data ultimei accesări: 9 mai 2026.  
[4] OpenAI, ChatGPT, https://chatgpt.com/, Data generării: 9 mai 2026.  
[5] Glenford J. Myers, Corey Sandler, Tom Badgett, The Art of Software Testing, John Wiley & Sons, 2011.  
[6] Paul Ammann, Jeff Offutt, Introduction to Software Testing, Cambridge University Press, 2016.
