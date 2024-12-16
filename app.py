from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista global de notas
notas = []

@app.route('/')
def index():
    return render_template('index.html', notas=notas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nueva_nota = request.form['nota']
        if nueva_nota:
            notas.append(nueva_nota)
        return redirect(url_for('index'))
    return render_template('agregar_nota.html')  # Cambiar el nombre del archivo aquí

@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar(index):
    if 0 <= index < len(notas):
        if request.method == 'POST':
            nueva_nota = request.form['nota']
            if nueva_nota:
                notas[index] = nueva_nota
            return redirect(url_for('index'))
        return render_template('editar_nota.html', nota=notas[index], index=index)  # Cambiar el nombre del archivo aquí
    return redirect(url_for('index'))

@app.route('/eliminar/<int:index>')
def eliminar(index):
    if 0 <= index < len(notas):
        del notas[index]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
