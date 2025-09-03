from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import replicate

app = Flask(__name__)
CORS(app)

# Pastikan variabel lingkungan sudah diatur
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

def call_granite_model(expression):
    """
    Mengirimkan ekspresi matematika ke Granite Model melalui Replicate API.
    """
    try:
        # Menyiapkan prompt untuk model AI
        prompt = f"Hitung hasil dari ekspresi matematika ini: {expression}. Berikan hanya angka hasilnya saja."

        # Memanggil model Granite di Replicate
        output = replicate.run(
            "ibm-granite/granite-3.3-8b-instruct:a325a0cacfb0aa9226e6bad1abe5385f1073f4c7f8c36e52ed040e5409e6c034",
            input={"prompt": prompt}
        )
        
        # Menggabungkan hasil keluaran dari model menjadi satu string
        result_string = "".join(output)
        
        # Membersihkan output (menghapus karakter non-angka, selain titik)
        cleaned_result = "".join(filter(lambda x: x.isdigit() or x == '.', result_string.strip()))
        
        # Periksa apakah hasil yang dibersihkan adalah angka valid
        if not cleaned_result or cleaned_result.count('.') > 1:
            return {"result": "Error", "status": "error", "message": "Invalid number format from AI"}
        
        return {"result": cleaned_result, "status": "success"}
    except Exception as e:
        print(f"Error: {e}")
        return {"result": "Error", "status": "error", "message": str(e)}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')
    
    if not expression:
        return jsonify({"result": "Error", "status": "error", "message": "No expression provided"}), 400
    
    # Menghapus karakter yang tidak diperlukan dari ekspresi (misalnya, tanda '=' atau spasi)
    # Ini memastikan bahwa hanya ekspresi matematika yang valid yang diproses.
    cleaned_expression = re.sub(r'[^0-9\+\-\*\/\.]', '', expression)
    
    # Memanggil fungsi yang berinteraksi dengan model AI dengan ekspresi yang sudah dibersihkan
    ai_response = call_granite_model(cleaned_expression)
    
    return jsonify(ai_response)

if __name__ == '__main__':
    # Pastikan kunci API sudah disiapkan sebelum menjalankan aplikasi
    if not REPLICATE_API_TOKEN:
        print("Error: REPLICATE_API_TOKEN is not set.")
        exit(1)
    
    app.run(debug=True)
