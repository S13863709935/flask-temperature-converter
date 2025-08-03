from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Display temperature converter homepage."""
    return render_template("base.html")

@app.route('/convert/<celsius>')
def convert(celsius):
    """
    Convert Celsius to Fahrenheit.
    Example: /convert/25 → 77°F
    """
    try:
        fahrenheit = float(celsius) * 9/5 + 32
        return f"{celsius}°C = {fahrenheit:.1f}°F"
    except ValueError:
        return "Error: Please enter a valid number"

if __name__ == '__main__':
    app.run(debug=True)