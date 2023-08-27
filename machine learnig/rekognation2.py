import boto3
import json

def detect_objects(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=50
    )
    return response['Labels']

def detect_faces(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_faces(
        Image={'Bytes': image_bytes},
        Attributes=['ALL']
    )
    return response['FaceDetails']

def print_objects(labels):
    print('Objetos detectados:')
    for label in labels:
        print(f"{label['Name']}: {label['Confidence']}%")

def print_faces(faces):
    print('\nRostros detectados:')
    for i, face in enumerate(faces, start=1):
        print(f"Rostro {i}:")
        print(f"Edad: {face['AgeRange']['Low']} - {face['AgeRange']['High']}")
        print(f"Género: {face['Gender']['Value']} ({face['Gender']['Confidence']}%)")
        print(f"Emoción más alta: {face['Emotions'][0]['Type']} ({face['Emotions'][0]['Confidence']}%)")
        print("---")

def save_results(results):
    with open('resultados.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)
    print("Resultados guardados en 'resultados.json'")

def main():
    with open('imagen.jpg', 'rb') as image_file:
        image_bytes=image_file.read()

    object_labels = detect_objects(image_bytes)
    face_details = detect_faces(image_bytes)

    print_objects(object_labels)
    print_faces(face_details)

    results = {
        'Labels': object_labels,
        'Faces': face_details
    }

    save_results(results)

if __name__ == "__main__":
    main()
