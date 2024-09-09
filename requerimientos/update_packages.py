import subprocess
import pkg_resources

def uninstall_package(package_name):
    try:
        subprocess.check_call(['pip', 'uninstall', '-y', package_name])
        print(f"Paquete {package_name} desinstalado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al desinstalar {package_name}: {e}")

def install_requirements(file_path):
    try:
        subprocess.check_call(['pip', 'install', '-r', file_path])
        print(f"Paquetes instalados desde {file_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar paquetes desde {file_path}: {e}")

def get_installed_packages():
    return {pkg.key for pkg in pkg_resources.working_set}

def main():
    # Paquete de requisitos
    requirements_file = 'requirements.txt'

    # Obtener paquetes instalados
    installed_packages = get_installed_packages()

    # Desinstalar paquetes existentes
    for package in installed_packages:
        uninstall_package(package)

    # Instalar paquetes desde requirements.txt
    install_requirements(requirements_file)

if __name__ == '__main__':
    main()
