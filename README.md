# encryptImage


## Codigo original obtenido de https://www.thesecuritybuddy.com/cryptography-and-python/how-to-encrypt-and-decrypt-an-image-using-python/

### Ese fue la pagina que usé para obtener el ejemplo, lo que hace es cifrar una imagen utilizando el algoritmo AES en modo CBC (Cipher Block Chaining). Solo que tuve que modificar y agregar ciertas cosas para que el código funcione bien.

### Primero importamos los módulos necesarios (os y Crypto.Cipher.AES).

### Luego, al guardar y leer datos binarios tenemos que abrir los archivos en modo binario, wb para escritura y rb para lectura.

### Agregamos una función pad para que los datos se ajusten al tamaño de bloque requerido por AES.

### Implementé la funcion de decrypt porque no estaba definida en el ejemplo
