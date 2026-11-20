from functools import lru_cache #$ Permite usar el decorador @lru_cache este es util para que las funciones no sean recalculadas si ya se han calculado antes, es decir, guarda en cache el resultado

from pydantic import Field, SecretStr 
#$ Field permite definir reglas de validacion para los atributos de la clase, SecretStr permite definir atributos que contienen informacion sensible como contraseñas o tokens
#$ Si se imprime una variable de tipo SecretStr, se mostrara como "*********" en lugar de mostrar el valor real

from pydantic_settings import BaseSettings, SettingsConfigDict
#$ Clase para crear configuraciones de la app, SettingsConfigDict permite establecer cómo se obtienen las variables de configuración.


#Creamos la clase Settings con la base herencia de BaseSettings este tiene la capacidad de leer variables de entorno y archivos de configuración, 
class Settings(BaseSettings):

    #Configuracion general de la aplicacion
    APP_NAME: str = "3Print QuicklyD"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False #Permite que no se muestren errores detallados en produccion solo se mostraran los codigos de error y mensajes genericos

    #Configuracion de la base de datos
    DATABASE_URL: SecretStr #permite que la url de la base de datos no se muestre en los logs

    #Configuracion de la seguridad
    FERNET_KEY: SecretStr #Cifra y descifra datos de manera segura
    JWT_SECRET_KEY: SecretStr #Clave secreta para firmar y verificar tokens JWT
    JWT_ALGORITHM: str = "HS256" #Algoritmo de firma para tokens JWT 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, gt=0, description="Tiempo de expiracion del token de acceso en minutos")
    #evita que se establezcan tiempos negativos de expiracion para el token

    #configuracion de .env
    model_config = SettingsConfigDict(
        env_file=".env", #se obtiene la variable del archivo .env
        env_file_encoding="utf-8", #el encoding del archivo .env es utf-8
        case_sensitive=True, #asegura que las variables de entorno sean sensibles a mayusculas y minusculas
        extra="ignore" #ignora variables de entorno adicionales que no estén definidas en la clase
    )

@lru_cache() #decorador para reutilizar la instancia de la clase Settiings y no crear una nueva cada vez que se llame a la funcion get_settings
def get_settings() -> Settings: #Crea una funcion que devuelve la instancia de Settings (Con las configuraciones de la app)
    return Settings() #$ usar -> hace que sepamos que tipo de variable devuelve la funcion al pasar el mouse por encima de la funcion

settings = get_settings() #Se usa por comodidad para no tener que llamar la funcion get_settings().DEBUG si no settings.DEBUG lo cual hace el codigo limpio y mas legible