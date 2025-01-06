from baixa_video import *
from resume_video import *
from transcreve_video import *
from flask import Flask, request, render_template
import time

app = Flask(__name__)

def main(url, caminho='audio.mp3'):
    inicio = time.time()
    baixa_audio(url)
    texto = transcrever_audio_whisper(caminho_audio=caminho)
    resumo = resumir_texto(texto)
    final = time.time()
    tempo = final - inicio
    print(f'o tempo de execução é de {tempo} segundos.')
    return resumo

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/resumir', methods=['GET'])
def resumir():
    url = request.args['url']
    resumo = main(url)
    return resumo

if __name__ == '__main__':
    app.run(debug=True)
