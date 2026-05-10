# T1 – Testare unitară în Python pentru clasa `OrderCalculator`

**Săftoiu (Golea) Genica – Liliana**  
**An 3, grupa 2, Informatica ID**

## 1. Introducere

Clasa aleasă pentru testare este `OrderCalculator`, implementată în fișierul `src/order_calculator.py`. Aceasta calculează totalul final al unei comenzi pe baza unor liste de prețuri și cantități, a statutului premium al clientului, a unui cupon de reducere și a opțiunii de transport urgent. În plus, clasa oferă o metodă de clasificare a comenzilor în funcție de valoarea totală.

În proiect au fost construite:
- o suită de teste;
- o suită de teste generată de AI;
- rapoarte de coverage;
- rapoarte de mutation testing;
- diagrame și capturi de ecran.

## 2. Cerința proiectului

Tema presupune utilizarea unui framework de testare unitară din Python pentru testarea funcționalităților unei clase și ilustrarea strategiilor predate la curs:
- partiționare în clase de echivalență;
- analiza valorilor de frontieră;
- acoperire la nivel de instrucțiune, decizie și condiție;
- analiza raportului generat de un generator de mutanți;
- teste suplimentare pentru eliminarea mutanților neechivalenți rămași în viață.

## 3. Descrierea aplicației testate

### 3.1. Clasa testată

Clasa testată este:

```python
class OrderCalculator:
```

Aceasta conține:
- atributul `urgent_shipping_fee`;
- metodele publice `calculate_final_total(...)` și `classify_order(...)`.

### 3.2. Funcționalitatea metodei `calculate_final_total`

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

### 3.3. Funcționalitatea metodei `classify_order`

Metoda `classify_order(final_total)`:
- ridică `ValueError` dacă valoarea este negativă;
- returnează:
  - `"small"` pentru valori sub 200;
  - `"medium"` pentru valori între 200 și 500 inclusiv;
  - `"large"` pentru valori mai mari de 500.

### 3.4. De ce este potrivită această clasă pentru T1

Implementarea respectă cerințele temei:
- are mai mult de 3 parametri în metoda principală;
- conține o instrucțiune repetitivă (`for`);
- conține un `if` cu `else`;
- conține un `if` fără `else`;
- conține o condiție simplă (`qty >= 10`);
- conține o condiție compusă (`is_premium and total >= 500`).

## 4. Structura proiectului

```text
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
├── diagrams/
│   ├── class_diagram.png
│   └── control_flow_diagram.png
├── reports/
│   └── raport_ai.md
├── cosmic-ray.toml
├── cosmic-ray-ai.toml
├── README.md
└── requirements.txt
```

## 5. Configurația hardware și software

### 5.1. Configurație hardware
- **Procesor:** Intel Core i7-11800H
- **Memorie RAM:** 32 GB

### 5.2. Configurație software
- **Sistem de operare:** Windows
- **Limbaj de programare:** Python 3.12.7
- **Framework de testare:** `unittest`
- **Tool pentru coverage:** `coverage.py`
- **Tool pentru mutation testing:** `Cosmic Ray`
- **Editor:** Visual Studio Code

### 5.3. Mașină virtuală
Proiectul a fost realizat fără utilizarea unei mașini virtuale.

## 6. Suita de teste

Suita proprie de teste este alcătuită din:
- `tests/test_functional.py`
- `tests/test_structural.py`
- `tests/test_mutation.py`

Aceasta reprezintă partea principală a proiectului.

## 7. Strategii de testare funcțională

Testarea funcțională a fost realizată în fișierul `tests/test_functional.py`.

### 7.1. Specificația funcțională a metodelor testate

Metoda `calculate_final_total(prices, quantities, is_premium, coupon_percent, urgent_shipping)` calculează valoarea finală a unei comenzi pe baza liniilor de produs și a regulilor comerciale definite în implementare.

**Precondiții:**  
`prices` și `quantities` trebuie să fie liste nevide, cu aceeași lungime; fiecare `price` trebuie să fie strict pozitiv; fiecare `qty` trebuie să fie strict pozitiv; `coupon_percent` trebuie să aparțină intervalului `[0, 30]`.

**Postcondiții:**  
dacă datele sunt valide, metoda returnează totalul final rotunjit la 2 zecimale, după aplicarea reducerii bulk, a reducerii premium, a taxei de transport urgent, a reducerii suplimentare pentru minimum două linii bulk și a cuponului. Dacă datele sunt invalide, metoda ridică `ValueError`.

Metoda `classify_order(final_total)` primește totalul final al unei comenzi și îl clasifică în una dintre categoriile `small`, `medium` sau `large`. Pentru valori negative se ridică `ValueError`.

### 7.2. Domeniul de intrări și domeniul de ieșiri

Domeniul de intrări pentru `calculate_final_total` este format din cinci parametri: două liste numerice (`prices`, `quantities`) și trei parametri de control (`is_premium`, `coupon_percent`, `urgent_shipping`). Domeniul de ieșiri are două forme: valoare numerică validă sau excepție `ValueError`.

Domeniul de intrări pentru `classify_order` este un număr real `final_total`. Domeniul de ieșiri este `{small, medium, large}` sau excepție `ValueError` pentru valori negative.

### 7.3. Clase de echivalență individuale

Pentru lungimea listelor:
- `L1 = {(prices, quantities) | len(prices) = len(quantities) și len(prices) > 0}`
- `L2 = {(prices, quantities) | len(prices) ≠ len(quantities)}`
- `L3 = {(prices, quantities) | len(prices) = len(quantities) = 0}`

Pentru prețuri:
- `P1 = {p | p > 0}`
- `P2 = {p | p ≤ 0}`

Pentru cantități:
- `Q1 = {q | q > 0}`
- `Q2 = {q | q ≤ 0}`

Pentru cupon:
- `CP1 = {c | 0 ≤ c ≤ 30}`
- `CP2 = {c | c < 0}`
- `CP3 = {c | c > 30}`

Pentru client premium:
- `PR1 = {True}`
- `PR2 = {False}`

Pentru transport urgent:
- `U1 = {True}`
- `U2 = {False}`

Pentru clasificarea ieșirii:
- `R1 = {total valid}`
- `R2 = {ValueError}`

Pentru `classify_order`:
- `K1 = {x | x < 0}`
- `K2 = {x | 0 ≤ x < 200}`
- `K3 = {x | 200 ≤ x ≤ 500}`
- `K4 = {x | x > 500}`

### 7.4. Clase de echivalență globale

Clasele globale au fost construite prin combinarea claselor individuale relevante pentru comportamentul funcției:

- `G1 = {L1, P1, Q1, CP1, PR2, U2, fără bulk, fără premium}` – comandă validă obișnuită
- `G2 = {L1, P1, Q1, CP1, PR2, U2, cu bulk}` – comandă validă cu discount bulk
- `G3 = {L1, P1, Q1, CP1, PR1, U2, total ≥ 500}` – comandă premium validă cu reducere premium
- `G4 = {L1, P1, Q1, CP1, PR2, U1}` – comandă validă cu transport urgent
- `G5 = {L1, P1, Q1, CP1, PR2, U2, minimum două linii bulk}` – comandă validă cu reducere suplimentară de 3%
- `G6 = {L2}` – intrări invalide prin lungimi diferite
- `G7 = {L3}` – intrări invalide prin liste vide
- `G8 = {L1, P2}` – intrări invalide prin preț nevalid
- `G9 = {L1, Q2}` – intrări invalide prin cantitate nevalidă
- `G10 = {L1, CP2}` – intrări invalide prin cupon sub limită
- `G11 = {L1, CP3}` – intrări invalide prin cupon peste limită

### 7.5. Tabel – reprezentanți pentru partiționarea în clase de echivalență

| Clasa globală | prices | quantities | is_premium | coupon_percent | urgent_shipping | Rezultat așteptat |
|---|---|---|---:|---:|---:|---|
| G1 | `[10, 20]` | `[2, 1]` | False | 0 | False | `40.0` |
| G2 | `[15]` | `[10]` | False | 0 | False | `142.5` |
| G3 | `[250, 100]` | `[2, 1]` | True | 0 | False | `540.0` |
| G4 | `[100]` | `[1]` | False | 0 | True | `125.0` |
| G5 | `[10, 30]` | `[10, 10]` | False | 0 | False | `368.6` |
| G6 | `[10, 20]` | `[1]` | False | 0 | False | `ValueError` |
| G7 | `[]` | `[]` | False | 0 | False | `ValueError` |
| G8 | `[-10]` | `[1]` | False | 0 | False | `ValueError` |
| G9 | `[10]` | `[0]` | False | 0 | False | `ValueError` |
| G10 | `[10]` | `[1]` | False | -1 | False | `ValueError` |
| G11 | `[10]` | `[1]` | False | 31 | False | `ValueError` |

### 7.6. Analiza valorilor de frontieră – mulțimi, margini și valori alese

Pentru `coupon_percent`, mulțimea validă este `[0, 30]`, iar marginile relevante sunt `0` și `30`. Valorile testate la frontieră au fost: `-1`, `0`, `30` și `31`.

Pentru pragul bulk, mulțimea relevantă este dată de condiția `qty ≥ 10`; marginile analizate au fost `9` și `10`.

Pentru reducerea premium, frontiera relevantă este `total = 500`; au fost analizate valorile imediat sub prag și chiar pe prag.

Pentru `classify_order`, frontierele relevante sunt `0`, `200` și `500`; au fost testate valorile `-0.01`, `0`, `199.99`, `200`, `500` și `500.01`.

| Parametru / condiție | Mulțimea validă | Margini | Valori de test |
|---|---|---|---|
| `coupon_percent` | `[0, 30]` | `0`, `30` | `-1`, `0`, `30`, `31` |
| `qty` pentru bulk | `qty ≥ 10` | `9`, `10` | `9`, `10` |
| prag premium | `total ≥ 500` | `499.99`, `500` | `499.99`, `500` |
| `classify_order` | `[0, ∞)` | `0`, `200`, `500` | `-0.01`, `0`, `199.99`, `200`, `500`, `500.01` |

### 7.7. Tabel – teste reprezentative pentru boundary value analysis

| Test | prices / total | quantities | is_premium | coupon | urgent | Expected |
|---|---|---|---:|---:|---:|---|
| BVA1 qty=9 | `[15]` | `[9]` | False | 0 | False | `135.0` |
| BVA2 qty=10 | `[15]` | `[10]` | False | 0 | False | `142.5` |
| BVA3 coupon=-1 | `[100]` | `[1]` | False | -1 | False | `ValueError` |
| BVA4 coupon=0 | `[100]` | `[1]` | False | 0 | False | `100.0` |
| BVA5 coupon=30 | `[100]` | `[1]` | False | 30 | False | `70.0` |
| BVA6 coupon=31 | `[100]` | `[1]` | False | 31 | False | `ValueError` |
| BVA7 premium sub prag | `[499.99]` | `[1]` | True | 0 | False | `499.99` |
| BVA8 premium pe prag | `[500]` | `[1]` | True | 0 | False | `450.0` |
| BVA9 classify 199.99 | `199.99` | `-` | `-` | `-` | `-` | `small` |
| BVA10 classify 200 | `200` | `-` | `-` | `-` | `-` | `medium` |
| BVA11 classify 500 | `500` | `-` | `-` | `-` | `-` | `medium` |
| BVA12 classify 500.01 | `500.01` | `-` | `-` | `-` | `-` | `large` |

### 7.8. Rezumatul suitei funcționale

Au fost definite clase de echivalență valide și invalide.

**Clase valide**
- comandă obișnuită, fără reduceri;
- comandă cu discount bulk;
- comandă premium cu prag atins;
- comandă cu transport urgent;
- comandă cu cel puțin două linii bulk.

**Clase invalide**
- liste vide;
- liste cu lungimi diferite;
- preț negativ;
- cantitate zero;
- cupon negativ;
- cupon peste limita permisă.

Frontiere urmărite:
- `qty = 9 / 10`
- `coupon_percent = -1, 0, 30, 31`
- `total = 499.99 / 500`
- clasificare la `199.99`, `200`, `500`, `500.01`

## 8. Strategii de testare structurală

Testarea structurală a fost realizată în fișierul `tests/test_structural.py`.

### 8.1. Realizarea grafului asociat programului

Graful de flux de control (CFG) a fost construit pentru metoda `calculate_final_total`, deoarece aceasta concentrează cea mai mare parte a logicii: validări inițiale, bucla principală, condițiile de discount și ramurile de eroare. Pentru completitudine, au fost luate în considerare și ramurile din `classify_order`.

### 8.2. Instrucțiuni / noduri relevante reprezentate în graf

| ID nod | Instrucțiune / decizie reprezentată |
|---|---|
| I1 | Intrare în `calculate_final_total` |
| I2 | Verificare lungimi liste / liste vide |
| I3 | Ridicare `ValueError` pentru lungimi invalide |
| I4 | Verificare interval cupon |
| I5 | Ridicare `ValueError` pentru cupon invalid |
| I6 | Inițializare `total` și `bulk_discount_lines` |
| I7 | Intrare în bucla `for` |
| I8 | Verificare `price <= 0 or qty <= 0` |
| I9 | Ridicare `ValueError` pentru linie invalidă |
| I10 | Calcul `line_total = price * qty` |
| I11 | Decizie `qty >= 10` |
| I12 | Aplicare discount bulk și incrementare contor |
| I13 | Adăugare `line_total` la `total` |
| I14 | Ieșire / reluare buclă |
| I15 | Decizie `is_premium and total >= 500` |
| I16 | Aplicare discount premium |
| I17 | Decizie `urgent_shipping` |
| I18 | Adăugare taxă urgentă |
| I19 | Decizie `bulk_discount_lines >= 2` |
| I20 | Aplicare discount suplimentar de 3% |
| I21 | Aplicare cupon |
| I22 | `return round(total, 2)` |
| K1 | Intrare în `classify_order` și verificare `final_total < 0` |
| K2 | Decizie `final_total < 200` |
| K3 | Decizie `final_total <= 500` |

### 8.3. Tabel pentru statement coverage

| Test | Intrări reprezentative | Rezultat așteptat | Instrucțiuni parcurse |
|---|---|---|---|
| SC1 | `prices=[30,25], quantities=[10,10], premium=True, coupon=10, urgent=True` | `432.35` | `I1, I2, I4, I6–I22` |
| SC2 | `prices=[10], quantities=[1,2]` | `ValueError` | `I1, I2, I3` |
| SC3 | `prices=[10], quantities=[1], coupon=-1` | `ValueError` | `I1, I2, I4, I5` |
| SC4 | `prices=[10,-3], quantities=[1,2]` | `ValueError` | `I1, I2, I4, I6, I7, I8, I9` |
| SC5 | `classify_order(-0.01)` | `ValueError` | `K1` |
| SC6 | `classify_order(50), classify_order(350), classify_order(800)` | `small / medium / large` | `K2, K3` |

### 8.4. Deciziile enumerate în cadrul testării structurale

- `D1: len(prices) != len(quantities) or len(prices) == 0`
- `D2: coupon_percent < 0 or coupon_percent > 30`
- `D3: price <= 0 or qty <= 0`
- `D4: qty >= 10`
- `D5: is_premium and total >= 500`
- `D6: urgent_shipping`
- `D7: bulk_discount_lines >= 2`
- `D8: final_total < 0`
- `D9: final_total < 200`
- `D10: final_total <= 500`

### 8.5. Tabel pentru decision coverage

| Test | Intrări | Rezultat | Decizii acoperite |
|---|---|---|---|
| DC1 | liste vide | `ValueError` | `D1=True` |
| DC2 | cupon -1 | `ValueError` | `D1=False, D2=True` |
| DC3 | `price=-5` | `ValueError` | `D2=False, D3=True` |
| DC4 | `qty=10` | `142.5` | `D3=False, D4=True` |
| DC5 | `qty=9` | `135.0` | `D4=False` |
| DC6 | `premium=True și total=500` | `450.0` | `D5=True` |
| DC7 | `premium=False și total=500` | `500.0` | `D5=False` |
| DC8 | `urgent=True` | `125.0` | `D6=True` |
| DC9 | `urgent=False` | `100.0` | `D6=False` |
| DC10 | două linii bulk | `368.6` | `D7=True` |
| DC11 | o singură linie bulk | `115.0` | `D7=False` |
| DC12 | `classify: -0.01 / 50 / 350 / 800` | `ValueError / small / medium / large` | `D8, D9, D10` |

### 8.6. Condițiile individuale urmărite în condition coverage

- `C1: len(prices) != len(quantities)`
- `C2: len(prices) == 0`
- `C3: coupon_percent < 0`
- `C4: coupon_percent > 30`
- `C5: price <= 0`
- `C6: qty <= 0`
- `C7: is_premium`
- `C8: total >= 500`

### 8.7. Tabel pentru condition coverage

| Test | Intrări | Rezultat | Condiții individuale acoperite |
|---|---|---|---|
| CC1 | liste vide | `ValueError` | `C1=False, C2=True` |
| CC2 | lungimi diferite | `ValueError` | `C1=True, C2=False` |
| CC3 | `cupon=-1` | `ValueError` | `C3=True, C4=False` |
| CC4 | `cupon=31` | `ValueError` | `C3=False, C4=True` |
| CC5 | `price=-5` | `ValueError` | `C5=True, C6=False` |
| CC6 | `qty=0` | `ValueError` | `C5=False, C6=True` |
| CC7 | `premium=True și total=500` | `450.0` | `C7=True, C8=True` |
| CC8 | `premium=False și total=500` | `500.0` | `C7=False, C8=True` |
| CC9 | `premium=True și total=499.99` | `499.99` | `C7=True, C8=False` |

### 8.8. Calculul numărului de circuite independente

Pentru graful asociat metodelor testate au fost identificate 10 noduri de decizie relevante (`D1`–`D10`). Pentru un graf conectat asociat unei singure unități testate, complexitatea ciclomatică poate fi exprimată prin relația:

`V(G) = D + 1`

Deci:

`V(G) = 10 + 1 = 11`

Echivalent, dacă se consideră 25 noduri relevante și 34 arce în CFG-ul agregat, se obține:

`V(G) = e - n + 2 = 34 - 25 + 2 = 11`

Prin urmare, setul de bază conține **11 circuite / căi independente**.

### 8.9. Circuite / căi independente enumerate

- `P1` – cale nominală fără bulk, fără premium, fără transport urgent, fără discount suplimentar
- `P2` – cale de eroare pentru liste vide sau lungimi diferite (`D1=True`)
- `P3` – cale de eroare pentru cupon în afara intervalului `[0, 30]` (`D2=True`)
- `P4` – cale de eroare pentru `price <= 0 or qty <= 0` în interiorul buclei (`D3=True`)
- `P5` – cale validă cu activarea ramurii `qty >= 10` pentru o singură linie (`D4=True, D7=False`)
- `P6` – cale validă cu activarea reducerii premium (`D5=True`)
- `P7` – cale validă cu activarea transportului urgent (`D6=True`)
- `P8` – cale validă cu două linii bulk și activarea reducerii suplimentare de 3% (`D7=True`)
- `P9` – cale de clasificare invalidă, `final_total < 0` (`D8=True`)
- `P10` – cale de clasificare `small`, respectiv `0 ≤ final_total < 200` (`D9=True`)
- `P11` – cale de clasificare `medium` și `large`, prin evaluarea ramurilor `D9=False` și `D10=True / False`

### 8.10. Rezumatul acoperirilor structurale

- **Statement coverage:** au fost create teste care execută toate instrucțiunile importante din `calculate_final_total` și `classify_order`.
- **Decision coverage:** au fost create teste astfel încât principalele decizii să fie evaluate atât cu `True`, cât și cu `False`.
- **Circuite independente:** au fost create teste pentru calea normală, calea cu bulk, calea cu premium, calea cu transport urgent, calea cu două linii bulk și căile de eroare care duc la `ValueError`.

## 9. Mutation testing pentru suita proprie

În fișierul `tests/test_mutation.py` au fost introduse teste suplimentare pentru mutanții rămași în viață.

### 9.1. Scop

După prima evaluare cu Cosmic Ray au fost identificați mutanți supraviețuitori. Pe baza raportului au fost adăugate teste suplimentare pentru cazuri sensibile, de exemplu:
- `qty > 10`
- `total > 500`
- `bulk_discount_lines > 2`
- `classify_order(0)`
- lungimi mari egale pentru liste
- cantități negative

### 9.2. Exemple de 2 mutanți neechivalenți eliminați prin teste suplimentare

| Mutant | Modificare indusă | Test suplimentar care îl omoară | Motivul eliminării |
|---|---|---|---|
| M1 | Înlocuire prag `qty >= 10` cu `qty > 10` | `test_mutation_bulk_discount_for_qty_greater_than_10` | Cazul cu `qty = 10` trebuie să primească discount bulk; mutantul nu îl mai acordă. |
| M2 | Înlocuire prag `bulk_discount_lines >= 2` cu `bulk_discount_lines > 2` | `test_mutation_bulk_lines_greater_than_2` | Cazul cu exact două linii bulk trebuie să primească reducerea suplimentară; mutantul o omite. |

### 9.3. Rezultat final

După îmbunătățirea suitei proprii:
- `total jobs: 153`
- `surviving mutants: 2 (1.31%)`

## 10. Rezultatele obținute pentru suita proprie

### 10.1. Rularea tuturor testelor

Comanda utilizată:

```powershell
py -m unittest discover -s tests -v
```

Rezultat:
- 63 teste;
- toate trecute cu succes.

#### Capturi – rularea testelor

**Teste funcționale**

### 10.2. Coverage

Comenzile utilizate:

```powershell
py -m coverage erase
py -m coverage run --branch -m unittest discover -s tests -v
py -m coverage report -m
py -m coverage html
```

Rezultatul principal pentru suita proprie:
- `src/order_calculator.py` – 100% coverage
- coverage total – 98%

### 10.3. Mutation testing

Comenzile utilizate:

```powershell
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray.toml
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
```

Rezultatul final:
- 153 mutanți
- 2 mutanți rămași în viață

## 11. Suita generată cu AI

Suita generată cu AI este alcătuită din:
- `tests/test_functional_ai.py`
- `tests/test_structural_ai.py`
- `tests/test_mutation_ai.py`

## 12. Rezultatele obținute pentru suita AI

### 12.1. Rularea testelor AI

Comenzile utilizate:

```powershell
py -m unittest -v tests.test_functional_ai
py -m unittest -v tests.test_structural_ai
py -m unittest -v tests.test_mutation_ai
```

Rezultate:
- `test_functional_ai.py` – 6 teste, toate trecute;
- `test_structural_ai.py` – 4 teste, toate trecute;
- `test_mutation_ai.py` – 4 teste, toate trecute.

În total:
- 14 teste
- toate trecute cu succes

### 12.2. Coverage pentru suita AI

Comenzile utilizate:

```powershell
py -m coverage erase
py -m coverage run --branch -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
py -m coverage report -m
```

Rezultatul obținut:

```text
Name                          Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------
src\order_calculator.py          36      0     22      0   100%
tests\test_functional_ai.py      38      1     10      1    96%   138
tests\test_mutation_ai.py        28      1      6      1    94%   58
tests\test_structural_ai.py      37      1      8      1    96%   97
-------------------------------------------------------------------------
TOTAL                           139      3     46      3    97%
```

Concluzii:
- `src/order_calculator.py` – 100% coverage
- coverage total pentru suita AI – 97%

### 12.3. Mutation testing pentru suita AI

A fost utilizată o configurație separată:

```powershell
cosmic-ray init cosmic-ray-ai.toml session_ai.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ai.toml
cosmic-ray exec cosmic-ray-ai.toml session_ai.sqlite
cr-report session_ai.sqlite
```

Rezultatul final:
- 153 mutanți
- 2 mutanți rămași în viață

## 13. Comparație între suita proprie și suita AI

| Criteriu | Suita proprie | Suita generată cu AI |
|---|---:|---:|
| Număr de teste | 63 | 14 |
| Framework utilizat | `unittest` | `unittest` |
| Fișiere de test | 3 | 3 |
| Coverage pe `src/order_calculator.py` | 100% | 100% |
| Coverage total | 98% | 97% |
| Mutation testing | 2 mutanți rămași din 153 | 2 mutanți rămași din 153 |
| Teste funcționale | detaliate | prezente, dar mai concentrate |
| Teste structurale | urmărite explicit | urmărite mai sintetic |
| Teste pentru mutanți | țintite | prezente, dar mai puține |

### 13.1. Interpretare

Deși suita AI este mult mai mică decât suita proprie, ea a obținut rezultate apropiate:
- 100% coverage pe fișierul sursă;
- același număr de mutanți rămași în viață.

Suita AI este utilă:
- ca sursă alternativă de idei;
- ca bază de comparație.

## 14. Bucăți reprezentative de cod

### 14.1. Exemplu din implementare

```python
if is_premium and total >= 500:
    total *= 0.90
else:
    total *= 1.0
```

Acest fragment este relevant deoarece conține:
- condiție compusă;
- ramură `if`;
- ramură `else`.

### 14.2. Exemplu din suita funcțională

```python
def test_boundary_coupon_30(self):
    result = self.calc.calculate_final_total(
        prices=[100],
        quantities=[1],
        is_premium=False,
        coupon_percent=30,
        urgent_shipping=False,
    )
    self.assertEqual(result, 70.0)
```

### 14.3. Exemplu din suita de mutații

```python
def test_mutation_classify_zero(self):
    self.assertEqual(self.calc.classify_order(0), "small")
```

Acest test este important pentru detectarea mutanților sensibili la pragul `0`.

## 15. Diagrame

În proiect sunt incluse două diagrame:
- `class_diagram.png`
- `control_flow_diagram.png`

### 15.1. Diagrama UML

Diagrama UML prezintă:
- clasa `OrderCalculator`;
- atributul `urgent_shipping_fee`;
- metodele publice testate.

### 15.2. Diagrama de control / flowchart

Flowchart-ul descrie logica metodei `calculate_final_total`:
- validări;
- bucla principală;
- aplicarea reducerilor;
- condițiile de ieșire și returnarea rezultatului.

## 16. Utilizarea unui tool AI

În `raport_ai.md` sunt prezentate:
- promptul folosit;
- răspunsul AI;
- capturi de ecran;
- comparația dintre suita proprie și suita generată;
- interpretarea rezultatelor.

## 17. Cerințe de rulare

### 17.1. Rularea suitei proprii

```powershell
py -m unittest discover -s tests -v
```

### 17.2. Rularea suitei AI

```powershell
py -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
```

### 17.3. Coverage pentru suita proprie

```powershell
py -m coverage erase
py -m coverage run --branch -m unittest discover -s tests -v
py -m coverage report -m
py -m coverage html
```

### 17.4. Coverage pentru suita AI

```powershell
py -m coverage erase
py -m coverage run --branch -m unittest -v tests.test_functional_ai tests.test_structural_ai tests.test_mutation_ai
py -m coverage report -m
```

### 17.5. Mutation testing pentru suita proprie

```powershell
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray.toml
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
```

### 17.6. Mutation testing pentru suita AI

```powershell
cosmic-ray init cosmic-ray-ai.toml session_ai.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ai.toml
cosmic-ray exec cosmic-ray-ai.toml session_ai.sqlite
cr-report session_ai.sqlite
```

## 18. Concluzii finale

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

## 19. Referințe bibliografice

[1] Python Software Foundation, `unittest` — Unit testing framework, https://docs.python.org/3/library/unittest.html, Data ultimei accesări: 9 mai 2026.  
[2] Ned Batchelder, Coverage.py, https://coverage.readthedocs.io/, Data ultimei accesări: 9 mai 2026.  
[3] Cosmic Ray Documentation, https://cosmic-ray.readthedocs.io/, Data ultimei accesări: 9 mai 2026.  
[4] OpenAI, ChatGPT, https://chatgpt.com/, Data generării: 9 mai 2026.  
[5] Glenford J. Myers, Corey Sandler, Tom Badgett, *The Art of Software Testing*, John Wiley & Sons, 2011.  
[6] Paul Ammann, Jeff Offutt, *Introduction to Software Testing*, Cambridge University Press, 2016.
