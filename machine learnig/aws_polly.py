
"""
synthesize_speech: Esta función toma un texto como entrada y utiliza el cliente de Polly 
para sintetizar el discurso. Puedes especificar el formato de salida (por defecto, MP3) y
 la voz a utilizar (por defecto, Joanna).

save_audio: Esta función guarda los datos de audio en un archivo de salida. Por defecto, 
el archivo se llama "output.mp3".

main: En la función principal, proporciona el texto que deseas convertir en voz. Luego,
 llama a synthesize_speech para obtener los datos de audio y a save_audio para guardarlos en un 
 archivo.                          """

import boto3


# Configura el cliente de Polly
client = boto3.client('polly')

def synthesize_speech(text, output_format='mp3', voice_id='Joanna'):
    response = client.synthesize_speech(
        Text=text,
        OutputFormat=output_format,
        VoiceId=voice_id
    )
    return response['AudioStream'].read()

def save_audio(audio_data, output_file='output.mp3'):
    with open(output_file, 'wb') as audio_file:
        audio_file.write(audio_data)
    print(f"Audio guardado en '{output_file}'")

def main():
    text_to_convert = "Hola, esto es un ejemplo de cómo utilizar Amazon Polly para convertir texto en voz."

    audio_data = synthesize_speech(text_to_convert)
    save_audio(audio_data)

if __name__ == "__main__":
    main()
