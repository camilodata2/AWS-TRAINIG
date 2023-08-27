"""
Vamo a realizar un ejemplo más completo y personalizado de cómo utilizar Amazon Polly 
para convertir un texto en voz. En este ejemplo, vamos a generar un archivo de audio en formato WAV, 
aplicar diferentes efectos de voz y guardar el resultado: """ 
import boto3

# Configura el cliente de Polly
client = boto3.client('polly')

def synthesize_speech(text, voice_id='Joanna', output_format='pcm', sample_rate='16000'):
    response = client.synthesize_speech(
        Text=text,
        OutputFormat=output_format,
        VoiceId=voice_id,
        SampleRate=sample_rate
    )
    return response['AudioStream'].read()

def save_audio(audio_data, output_file='output.wav'):
    with open(output_file, 'wb') as audio_file:
        audio_file.write(audio_data)
    print(f"Audio guardado en '{output_file}'")

def main():
    text_to_convert = "¡Hola! hoy estoy muy cansado y de verdad solo quiero nadar y tomar el sol ."

    # Genera el discurso sintetizado con efectos de voz
    audio_data = synthesize_speech(text_to_convert, voice_id='Matthew', sample_rate='22050')

    # Guarda el archivo de audio
    save_audio(audio_data, output_file='output.wav')

if __name__ == "__main__":
    main()
