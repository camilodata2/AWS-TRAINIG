import boto3

# Configura el cliente de Rekognition
client = boto3.client('rekognition')

# Carga la imagen a analizar
with open('imagen.jpg', 'rb') as image_file:
    image_bytes = image_file.read()

# Llama a la función detect_labels para detectar objetos en la imagen
response_labels = client.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=10,
    MinConfidence=50
)

# Imprime los resultados de detección de objetos
print('Objetos detectados:')
for label in response_labels['Labels']:
    print(f"{label['Name']}: {label['Confidence']}%")

# Llama a la función detect_faces para detectar rostros en la imagen
response_faces = client.detect_faces(
    Image={'Bytes': image_bytes},
    Attributes=['ALL']
)

# Imprime los resultados de detección de rostros
print('\nRostros detectados:')
for face in response_faces['FaceDetails']:
    print(f"Edad: {face['AgeRange']['Low']} - {face['AgeRange']['High']}")
    print(f"Emoción más alta: {face['Emotions'][0]['Type']} ({face['Emotions'][0]['Confidence']}%)")
    print(f"Género: {face['Gender']['Value']} ({face['Gender']['Confidence']}%)")
    print("---")
