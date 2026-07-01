import math

class HesapMotoru:
    def __init__(self, ekstra_fonksiyonlar=None):
        #bilimsel.py buraya kendi fonksiyonlarını gönderecek (sin, cos, log ...)eval için 
        self.ekstra = ekstra_fonksiyonlar or {}

    def _guvenli_ortam(self):
        ortam = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "pi": math.pi,
            "e": math.e
        }
        ortam.update(self.ekstra)
        return ortam
    
    def _cevir(self, ifade):
        degisimler = {
            "×": "*",
            "÷": "/",
            "^": "**",
            "√": "sqrt",
            "π": "pi"}
        for eski, yeni in degisimler.items():
            ifade = ifade.replace(eski, yeni)
        
        return ifade
    
    def _bicimlendir(self, sonuc):
        if isinstance(sonuc, float):
            sonuc = round(sonuc, 12)
            if sonuc.is_integer():
                sonuc = int(sonuc)
        
        return str(sonuc)
    
    def hesapla(self, ifade):
        if not ifade.strip():
            return ""
        try:
            temiz = self._cevir(ifade)

            #güvenlik için builtins
            sonuc = eval(temiz, {"__builtins__": {}}, self._guvenli_ortam())
            return self._bicimlendir(sonuc)    
    
        except ZeroDivisionError:
            return "sıfıra bölünemez"
        except SyntaxError:
            return "geçersiz ifade"
        except Exception as e:
            return "Hata: " + str(e)
    
    
if __name__ == "__main__":
    m = HesapMotoru()
    testler = ["2+3×4", "(2+3)×4", "2^10", "√(16)", "10÷0", "2++", "π×2"]
    for t in testler:
        print(f"{t:12} = {m.hesapla(t)}")