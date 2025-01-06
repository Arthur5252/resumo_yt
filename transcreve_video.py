import whisper

def transcrever_audio_whisper(caminho_audio):
    """
    Transcreve um arquivo de áudio usando o modelo Whisper.
    """
    modelo = whisper.load_model('tiny')
    resultado = modelo.transcribe(caminho_audio)
    print('---------------Audio transcrito---------------')
    return resultado['text']
