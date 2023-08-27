"""Este es un ejemplo fiticio de como usar aws sagemaker.
Supongamos que tenemos un conjunto de datos que incluye información médica de pacientes, 
como resultados de pruebas y diagnósticos previos. El objetivo es construir un modelo de machine learning 
que clasifique a los pacientes en dos categorías: "con cáncer" y "sin cáncer" """

import boto3

# Configuración de AWS
region = 'us-virginia-2'
bucket = 'first_sagemaker_bucket'
prefix = 'sagemaker/random-forest'

# Nombre del trabajo de entrenamiento y el modelo
training_job_name = 'random-forest-training-job'
model_name = 'random-forest-cancer-detection'

# Crea el cliente de SageMaker
sagemaker = boto3.client('sagemaker', region_name=region)

# Carga tus datos de pacientes con cáncer a S3
data_key = 'patients.csv'
data_location = f's3://{bucket}/{prefix}/{data_key}'

# Configuración de entrada y salida de datos
input_data_config = [
    {
        'ChannelName': 'train',
        'DataSource': {
            'S3DataSource': {
                'S3DataType': 'S3Prefix',
                'S3Uri': data_location,
                'S3DataDistributionType': 'FullyReplicated'
            }
        },
        'ContentType': 'text/csv',
        'CompressionType': 'None'
    }
]

# Hiperparámetros del modelo
hyperparameters = {
    'num_classes': '2',
    'num_features': '10',
    'num_trees': '100'
}

# Crea un trabajo de entrenamiento en SageMaker
sagemaker.create_training_job(
    TrainingJobName=training_job_name,
    AlgorithmSpecification={
        'TrainingImage': '174872318107.dkr.ecr.us-west-2.amazonaws.com/randomcutforest:latest',
        'TrainingInputMode': 'File'
    },
    RoleArn='arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_ROLE',
    InputDataConfig=input_data_config,
    OutputDataConfig={
        'S3OutputPath': f's3://{bucket}/{prefix}/output'
    },
    ResourceConfig={
        'InstanceType': 'ml.m4.xlarge',
        'InstanceCount': 1,
        'VolumeSizeInGB': 30
    },
    HyperParameters=hyperparameters,
    StoppingCondition={
        'MaxRuntimeInSeconds': 3600
    }
)

# Crea el modelo a partir del trabajo de entrenamiento
sagemaker.create_model(
    ModelName=model_name,
    PrimaryContainer={
        'Image': '174872318107.dkr.ecr.us-west-2.amazonaws.com/randomcutforest:latest',
        'ModelDataUrl': f's3://{bucket}/{prefix}/output/{training_job_name}/output/model.tar.gz'
    },
    ExecutionRoleArn='arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_ROLE'
)

# Crea un punto de enlace (endpoint) para el modelo
endpoint_config_name = 'random-forest-endpoint-config'
sagemaker.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[
        {
            'VariantName': 'AllTraffic',
            'ModelName': model_name,
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.m4.xlarge'
        }
    ]
)

# Crea el punto de enlace
endpoint_name = 'random-forest-endpoint'
sagemaker.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name
)
