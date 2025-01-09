from baixa_video import *
from resume_video import *
from transcreve_video import *
from flask import Flask, request, render_template, jsonify
import time
import os

app = Flask(__name__)

def main(url, caminho='audio.wav'):
    inicio = time.time()
    baixa_audio(url)
    texto = transcrever_audio_whisper(caminho_audio=caminho)
    resumo = resumir_texto(texto)
    final = time.time()
    tempo = final - inicio
    os.remove('audio.wav')
    print(f'o tempo de execução é de {tempo} segundos.')
    return resumo

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/resumir', methods=['POST'])
def resumir():
    url = request.json['url']
    resumo = main(url)
    response_data={
        "resumo":resumo
    }
    return jsonify(response_data)