from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# --------------------------
# ✅ COMPANY INFO
# --------------------------
COMPANY_NAME = "LAZENDA DEVELOPMENT SDN. BHD."
CIDB_REG = "1971017-LB043916"
GRADE = "G7"
LOCATION = "Wilayah Persekutuan Labuan, Malaysia"
PHONE = "+60 11-6567 6997"
EMAIL = "info@lazendadev.com"

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html',
                           company_name=COMPANY_NAME,
                           cidb_reg=CIDB_REG,
                           grade=GRADE,
                           location=LOCATION,
                           phone=PHONE,
                           email=EMAIL)

if __name__ == '__main__':
    app.run(debug=True)
