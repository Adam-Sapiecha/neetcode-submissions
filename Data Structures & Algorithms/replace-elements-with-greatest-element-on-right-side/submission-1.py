from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 1. Ustalamy startowy punkt dla "największego elementu po prawej".
        # Z treści zadania wiemy, że dla ostatniego elementu po prawej stronie 
        # nie ma już nic, więc jego wynikiem zawsze musi być -1.
        maks_po_prawej = -1
        
        # 2. Uruchamiamy pętlę OD KOŃCA do początku.
        # range(start, stop, krok)
        # start: len(arr) - 1  -> indeks ostatniego elementu
        # stop:  -1            -> pętla zatrzyma się przed -1, czyli wykona się dla indeksu 0
        # krok:  -1            -> idziemy w tył (zmniejszamy indeks o 1 w każdym kroku)
        for i in range(len(arr) - 1, -1, -1):
            
            # 3. KROK REZERWACJI
            # Zaraz nadpiszemy element pod arr[i], ale jego pierwotna wartość 
            # będzie nam potrzebna w kolejnym kroku, żeby zaktualizować 'maks_po_prawej'.
            # Dlatego chowamy ją na chwilę do bezpiecznej „szuflady”.
            stara_wartosc = arr[i]
            
            # 4. KROK ZAMIANY
            # Wpisujemy dotychczasowy największy znaleziony z prawej strony element
            # na aktualną pozycję. W pierwszym kroku (dla końca) wskoczy tu nasze -1.
            arr[i] = maks_po_prawej
            
            # 5. KROK AKTUALIZACJI
            # Sprawdzamy, czy wartość, którą właśnie schowaliśmy do szuflady (stara_wartosc),
            # jest większa niż nasz dotychczasowy król (maks_po_prawej).
            # Jeśli tak, to ona zostaje nowym maksymalnym elementem dla liczb po lewej stronie.
            if stara_wartosc > maks_po_prawej:
                maks_po_prawej = stara_wartosc
                
        # 6. Zwracamy zmodyfikowaną w miejscu, gotową tablicę.
        return arr
