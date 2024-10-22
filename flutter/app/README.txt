#Pra rodar o preview no vscode

-> primeiro instalar as dependencias:

sudo dnf install git curl unzip
curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.7.0-stable.tar.xz
tar -xf flutter_linux_3.7.0-stable.tar.xz
sudo mv flutter /opt/flutter
echo 'export PATH="/opt/flutter/bin:$PATH"' >> ~/.bashrc
flutter doctor


-> depois subir o servidor:

cd flutter/app/
flutter run -d web-server --web-port 5555 -t lib/main.dart