Gerador de Senhas Seguras com HMAC e Interface Gráfica

Este é um gerador de senhas seguras utilizando HMAC (SHA-256) para criar senhas baseadas no site informado pelo usuário, combinadas com uma chave secreta e, opcionalmente, o endereço MAC do dispositivo. O programa possui uma interface gráfica simples desenvolvida com Tkinter.

Funcionalidades

Gera senhas seguras usando HMAC (SHA-256) e codifica o resultado em Base64.

Interface gráfica amigável para inserção de dados.

Opção de personalizar a senha utilizando checkboxes.

Possibilidade de usar o endereço MAC do dispositivo como fator adicional.

Senha gerada é automaticamente copiada para a área de transferência.

Opção de gerar uma nova senha ou encerrar o programa após cada geração.

Dependências

Para executar o script, é necessário instalar as seguintes bibliotecas Python:

Como Executar

Basta rodar o script em um ambiente Python:

Como Funciona

O programa solicita o nome do site para o qual a senha será gerada.

O usuário pode escolher se deseja usar checkboxes personalizadas e/ou o endereço MAC do dispositivo.

O programa solicita uma chave secreta do usuário para gerar a senha.

A senha gerada é exibida na tela e copiada automaticamente para a área de transferência.

O usuário pode optar por gerar outra senha ou sair do programa.

Estrutura do Código

get_mac_address(): Obtém o endereço MAC do dispositivo.

generate_password_hmac(site, secret_key, checkbox_selection, use_mac): Gera uma senha usando HMAC com SHA-256.

show_checkbox_screen(): Exibe uma interface para seleção de checkboxes.

generate_password_gui(): Gerencia a interface inicial para entrada de dados.

generate_password(site, use_checkboxes, use_mac): Lida com a geração da senha baseada nas entradas do usuário.

show_generated_password_screen(site, password): Mostra a senha gerada e permite ao usuário gerar outra ou sair.

Autor

Este projeto foi desenvolvido para auxiliar na criação de senhas seguras de forma fácil e intuitiva, aproveitando a criptografia HMAC para garantir maior segurança.