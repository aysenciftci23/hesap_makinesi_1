from flask import Flask, render_template_string, request, jsonify
import math
import re
import webbrowser
from threading import Timer

app = Flask(__name__)


# ==========================================
# HESAPLAMA MOTORU (Senin Altyapın)
# ==========================================

from bilimsel import bilimsel_fonksiyon_ekle

class HesapMotoru:
    def _guvenli_ortam(self):
        return {"sqrt": math.sqrt, "pow": pow, "abs": abs, "pi": math.pi, "e": math.e, "math": math}

    def _cevir(self, ifade):
        ifade = bilimsel_fonksiyon_ekle(ifade)
        ifade = re.sub(r"√(\d+)", r"sqrt(\1)", ifade)
        degisimler = {"×": "*", "÷": "/", "^": "**", "√": "sqrt", "π": "pi"}
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
        if ifade.count("(") != ifade.count(")"):
            return "Eksik parantez"
        if not ifade.strip():
            return ""
        try:
            temiz = self._cevir(ifade)
            sonuc = eval(temiz, {"__builtins__": {}}, self._guvenli_ortam())
            return self._bicimlendir(sonuc)
        except ZeroDivisionError:
            return "Sıfıra bölünemez"
        except Exception:
            return "Geçersiz ifade"


motor = HesapMotoru()

# ==========================================
# HTML, CSS VE JAVASCRIPT ARAYÜZÜ (Tek String)
# ==========================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hesap Makinesi UI_1</title>
    <style>
        body {
            background-color: #121212;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .calculator {
            background-color: #1e1e1e;
            padding: 24px;
            border-radius: 20px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
            width: 340px;
            border: 1px solid #2d2d2d;
        }
        #display {
            width: 100%;
            height: 70px;
            background-color: #141414;
            border: 2px solid #2d2d2d;
            border-radius: 12px;
            color: #ffffff;
            font-size: 28px;
            text-align: right;
            padding: 15px;
            box-sizing: border-box;
            margin-bottom: 20px;
            font-family: monospace;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }
        .scientific-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
            margin-bottom: 15px;
        }
        button {
            padding: 16px;
            font-size: 18px;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            background-color: #2a2a2a;
            color: #e0e0e0;
            transition: all 0.15s ease;
        }
        button:hover { 
            background-color: #3a3a3a; 
            transform: scale(1.02);
        }
        button:active { transform: scale(0.98); }
        .sci-btn { background-color: #1a2b3c; font-size: 14px; padding: 12px 5px; color: #8ab4f8; }
        .sci-btn:hover { background-color: #243b53; }
        .op-btn { background-color: #ff9f0a; color: white; }
        .op-btn:hover { background-color: #cc7f08; }
        .clear-btn { background-color: #ff453a; color: white; }
        .clear-btn:hover { background-color: #d63629; }
        .equal-btn { grid-column: span 2; background-color: #34c759; color: white; }
        .equal-btn:hover { background-color: #28a146; }
    </style>
</head>
<body>

<div class="calculator">
    <input type="text" id="display" readonly value="" placeholder="0">

    <div class="scientific-grid">
        <button class="sci-btn" onclick="ekle('sin(')">sin</button>
        <button class="sci-btn" onclick="ekle('cos(')">cos</button>
        <button class="sci-btn" onclick="ekle('tan(')">tan</button>
        <button class="sci-btn" onclick="ekle('log(')">log</button>
        <button class="sci-btn" onclick="ekle('ln(')">ln</button>
        <button class="sci-btn" onclick="ekle('sqrt(')">√</button>
        <button class="sci-btn" onclick="ekle('^')">^</button>
        <button class="sci-btn" onclick="ekle('pi')">π</button>
        <button class="sci-btn" onclick="ekle('e')">e</button>
        <button class="sci-btn" onclick="ekle('e^')">e^</button>
    </div>

    <div class="grid">
        <button class="clear-btn" onclick="temizle()">C</button>
        <button onclick="ekle('(')">(</button>
        <button onclick="ekle(')')">)</button>
        <button class="op-btn" onclick="ekle('÷')">÷</button>

        <button onclick="ekle('7')">7</button>
        <button onclick="ekle('8')">8</button>
        <button onclick="ekle('9')">9</button>
        <button class="op-btn" onclick="ekle('×')">×</button>

        <button onclick="ekle('4')">4</button>
        <button onclick="ekle('5')">5</button>
        <button onclick="ekle('6')">6</button>
        <button class="op-btn" onclick="ekle('-')">-</button>

        <button onclick="ekle('1')">1</button>
        <button onclick="ekle('2')">2</button>
        <button onclick="ekle('3')">3</button>
        <button class="op-btn" onclick="ekle('+')">+</button>

        <button onclick="ekle('0')">0</button>
        <button onclick="sil()">⌫</button>
        <button class="equal-btn" onclick="hesapla()">=</button>
    </div>
</div>

<script>
    const display = document.getElementById('display');

    function ekle(deger) {
        display.value += deger;
    }

    function temizle() {
        display.value = '';
    }

    function sil() {
        display.value = display.value.slice(0, -1);
    }

    async function hesapla() {
        const ifade = display.value;
        if (!ifade) return;

        try {
            const cevap = await fetch('/hesapla', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ ifade: ifade })
            });
            const veri = await cevap.json();
            display.value = veri.sonuc;
        } catch (error) {
            display.value = "Bağlantı Hatası";
        }
    }
</script>

</body>
</html>
"""


# ==========================================
# FLASK YOLLARI (Routes)
# ==========================================

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/hesapla', methods=['POST'])
def hesapla_api():
    veri = request.get_json()
    ifade = veri.get('ifade', '')
    sonuc = motor.hesapla(ifade)
    return jsonify({'sonuc': sonuc})


def tarayiciyi_ac():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == '__main__':
    # Kod çalışınca tarayıcıda otomatik açılması için küçük bir zamanlayıcı
    Timer(1, tarayiciyi_ac).start()
    app.run(debug=True, port=5000, use_reloader=False)