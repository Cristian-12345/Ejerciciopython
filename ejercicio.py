
users_database = {
    "cristian123": {"password": "cristianpass", "role": "user"},
    "admin456": {"password": "adminpass", "role": "admin"},
    "superuser789": {"password": "superpass", "role": "superuser"}
}


def authenticate(func):
    def wrapper(username, password, *args, **kwargs):
        if username in users_database and users_database[username]["password"] == password:
            return func(username, *args, **kwargs)
        else:
            return "Autenticación fallida"
    return wrapper


def authorize(role):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            if username in users_database and users_database[username]["role"] == role:
                return func(username, *args, **kwargs)
            else:
                return "Acceso no autorizado"
        return wrapper
    return decorator


@authenticate
@authorize("user")
def user_function(username):
    return f"Bienvenido, Cristian ({username})"

@authenticate
@authorize("admin")
def admin_function(username):
    return f"Bienvenido, Administrador Cristian ({username})"

@authenticate
@authorize("superuser")
def superuser_function(username):
    return f"Bienvenido, Superusuario Cristian ({username})"


print(user_function("cristian123", "cristianpass"))   
print(admin_function("admin456", "adminpass"))        
print(superuser_function("superuser789", "superpass"))  

print(user_function("admin456", "wrongpass"))          
print(admin_function("cristian123", "cristianpass"))  