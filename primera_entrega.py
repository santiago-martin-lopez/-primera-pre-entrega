#creacion de diccionario vacio para simular base de datos, y almacenar usuarios
db_usuarios={}
#funcion para almacenar un nuevo registro de usuario
def almacenar():
    nombre_usuario=input('ingrese su nombre de usuario \n  ')
    while nombre_usuario.isnumeric():
        print('no puedes utilizar caracteres numericos ')
        nombre_usuario=input('ingrese su nombre de usuario \n  ')
        
    contrasenia=input('ingrese una contraseña ')
    while len(contrasenia)<8:
        print(f'tu contraseña solo cuenta con {len(contrasenia)} caracteres, al menos debe tener al menos 8 caracteres')
        contrasenia=input('ingrese nuevamente una contraseña: ')
    else:
        db_usuarios[nombre_usuario]=contrasenia
        print('contraseña registrada con exito')
            
    if nombre_usuario in db_usuarios:
        print('El nombre de usuario ingresado ya se encuentra registrado')
        return
#funcion para mostrar los nombres de los usuarios registrados     
def view():
    if not db_usuarios:
        print('no hay usuarios registrados')
    else:
        for nombre in db_usuarios.keys():
            print(f'el nombre de usuario registrado {nombre}')
#funcion para loguearse, constatando si existe dicho usuario y contraseña registrados en el diccionario
#funcion principal
def login():
    nombre=input('ingrese su nombre de usuario para iniciar sesion: ')
    contrasenia=input('ingrese su contraseña para iniciar sesion: ')
    if (nombre in db_usuarios) and (db_usuarios[nombre]==contrasenia):
        print(f'bienvenido {nombre}!')
    else:
        print(f'usuario y contraseña incorrectos')
        
    
def main():
    while True:
        print("\n1. Registrar Usuario. \n2. Mostrar Usuarios. \n3. Iniciar Sesión. \n4. Salir.")
        opcion=input('ingrese una opcion \n')
        if opcion=='1':
            almacenar()
        elif opcion=='2':
            view()
        elif opcion=='3':
            login()
        elif opcion=='4':
            print('finalizo la ejecuccion del programa')
            break
        else:
            print('elegiste una opcion incorrecta')
                
if __name__=='__main__':
    main()