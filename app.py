from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Chuyển đổi chiều cao từ cm sang m
    bmi = weight / (height_m ** 2)  # Công thức tính BMI chính xác
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "You are underweight\nYou need a more reasonable diet"
    elif 18.5 <= bmi <= 24.9:
        return "Your body is normal\nYou are a person with a reasonable diet"
    elif 25 <= bmi <= 29.9:
        return "You are an overweight person\nYou need to fix just a few parts of your diet"
    else:
        return "You are an obese person\nYou need to immediately correct your diet"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        bmi = calculate_bmi(weight, height_cm)
        category = get_bmi_category(bmi)
    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
